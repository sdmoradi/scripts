import requests

# Variables
schema = "https"
elastic_address = "elasticsearch.example.com"
index_name = "nginxlogs-alias-production"
api = "_count"
auth = "ABCD"
telegram_url = "https://telegram.com/webhook-address"
server_name_1 = "gateway1.example.com"
server_name_2 = "gateway2.example.com"

# URL and Headers for authentication and content type
url = schema + "://" + elastic_address + "/" + index_name + "/" + api
headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic " + auth
}

# List of request_uri values 
request_uris_1s = [
    "/example/uri-1", 
    "/example/uri-2", 
    "/example/uri-3", 
    "/example/uri-4"
    ]
request_uris_2s = [
    "/example/uri-5", 
    "/example/uri-6", 
    "/example/uri-7", 
    "/example/uri-8"
    ]
request_uris_3s = [
    "/example/uri-9", 
    "/example/uri-10", 
    "/example/uri-11", 
    "/example/uri-12"
    ]
request_uris_5s = [
    "/Order/Start", 
    "/Basket/Callback"
    ]

def get_count(query):
    response = requests.get(url, headers=headers, json=query)
    return response.json()["count"]

def calculate_percentage(total, gte_2s):
    if total == 0:
        return 0
    return (gte_2s / total) * 100

def send_to_telegram(alert_data):
    url = telegram_url
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=alert_data)
    return response

def uptime_query(server_name,alert_percentage):
    uptime_query = {
        "query": {
            "bool": {
            "must": [
                { "match": { "server_name": server_name } },
                { "prefix": { "request_uri.keyword": "/" } },
                {
                "bool": {
                    "should": [
                    { "prefix": { "status": "1" } },
                    { "prefix": { "status": "2" } },
                    { "prefix": { "status": "4" } }
                    ]
                }
                },
                {
                "range": {
                    "@timestamp": {
                    "gte": "now-12h"
                    }
                }
                }
            ]
            }
        }
        }
    downtime_query = {
        "query": {
            "bool": {
            "must": [
                { "match": { "server_name": server_name } },
                { "prefix": { "request_uri.keyword": "/" } },
                {
                "bool": {
                    "should": [
                    { "prefix": { "status": "5" } },
                    ]
                }
                },
                {
                "range": {
                    "@timestamp": {
                    "gte": "now-12h"
                    }
                }
                }
            ]
            }
        }
        }
    uptime_count = get_count(uptime_query)
    print(uptime_count)
    downtime_count = get_count(downtime_query)
    print(downtime_count)
    downtime_percentage = downtime_count * 100 / uptime_count
    print(str(downtime_percentage) + "%")
    uptime_percentage = 100 - downtime_percentage
    print(str(uptime_percentage) + "%")
    if uptime_percentage <= alert_percentage:
        alert_data = {
            "status": "firing",
            "alerts": [
                {
                    "labels": {
                        "alertname": server_name + " Uptime",
                        "severity": "Critical",
                    },
                    "annotations": {
                        "summary": "Uptime Alert",
                        "description": " 🔴 " + "Uptime of " + server_name + " is " + str(uptime_percentage) + "%"
                    },
                }
            ],
        }
        print("Alert sended")
        send_to_telegram(alert_data)


def run_query(latency_second,alert_percentage):
    for request_uri in eval("request_uris_" + str(latency_second) + "s"):
        server_name = server_name_1
        if request_uri in ['/example/uri-2', '/example/uri-3']:
            server_name = server_name_2
        query_total = {
            "query": {
                "bool": {
                    "must": [
                        {"match": {"server_name": server_name}},
                        {"match": {"status": "200"}},
                        {"prefix": {"request_uri.keyword": request_uri}},
                        {"range": {"@timestamp": {"gte": "now-12h"}}},
                    ]
                }
            }
        }

        query_gte = {
            "query": {
                "bool": {
                    "must": [
                        {"match": {"server_name": server_name}},
                        {"match": {"status": "200"}},
                        {"prefix": {"request_uri.keyword": request_uri}},
                        {"range": {"@timestamp": {"gte": "now-12h"}}},
                    ],
                    "filter": {"range": {"request_time": {"gt": latency_second}}},
                }
            }
        }


        total_count = get_count(query_total)
        print("Total Count of " + request_uri + " = " + str(total_count))
        gte_count = get_count(query_gte)
        print("Latency Count of " + request_uri + " = " + str(gte_count))


        percentage = calculate_percentage(total_count, gte_count)
        print("Percentage of " + request_uri + " = " + str(percentage) + "%")
        print("---------------------------------------------------------------------------------")
        if percentage >= alert_percentage:
            alert_data = {
                "status": "firing",
                "alerts": [
                    {
                        "labels": {
                            "alertname": "ApplicationMetrics-" + str(latency_second) +"s",
                            "severity": "Critical",
                        },
                        "annotations": {
                            "summary": "Latency on " + str(latency_second) +"s",
                            # "description": " 🟠 " + request_uri + " Percentage of Latency is upper than " + str(alert_percentage) +"%"
                            "description": " 🟠 " + request_uri + " Percentage of Latency is " + str(percentage) +"%"
                        },
                    }
                ],
            }
            send_to_telegram(alert_data)

response = run_query(1,5)
response = run_query(2,5)
response = run_query(3,5)
response = run_query(5,5)
response = uptime_query("example.com", 99 )