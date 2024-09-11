# Scripts
All scripts for different purposes

## Share Your Experiences

If you have any experiences or feedback related to this script, we would love to hear from you! Whether it's a suggestion, improvement, or even if the script didn't quite meet your needs, sharing your thoughts can contribute to the overall development of the project.

**Note:** Your experiences may or may not be applicable to others, but they could still be valuable. So, don't hesitate to share!

To share your experiences, please consider:

- Opening an issue in this GitHub repository.
- Providing details about your use case, any challenges faced, and how the script performed.
- Any suggestions or improvements you have in mind.

Your feedback is greatly appreciated! If you find the script useful or it meets your requirements, we also encourage you to star the project on GitHub to show your support.

Thank you for your contribution to the project!

### 1 - Elasticsearch Index Deletion Script

[Script Source](./bash/clear-elastic-index.sh)

This Bash script is designed to delete indices in Elasticsearch based on a specific date pattern. It utilizes the Elasticsearch API and the `curl` command-line tool.

#### Prerequisites

- Bash environment
- `curl` command-line tool
- Access to an Elasticsearch cluster
- Elasticsearch credentials (username and password)


### 2 - Nexus Nuget Components Downloader

[Script Source](./python/get-nuget-components.py)

This script enables you to download assets from a Nexus repository. It fetches a list of components from the specified Nexus repository and downloads the associated assets to a local directory.

#### Prerequisites

- Python 3.x
- `requests` library (install using `pip install requests`)

### 3 - Change docker image Registry

[Script Source](./python/change-image-repo.py)

The script will read the image names from image_list.txt, process each image, and migrate it to the destination registry.

#### Prerequisites

- Python 
- Docker

### 4 - webp contverter to jpg on minio storage

[Script Source](./python/webp-converter.py)

This script allows you to download webp images from a MinIO bucket, convert them from RGBA to RGB mode, and upload the converted images back to the bucket in JPEG format.

#### Prerequisites

- Python 3.x
- minio library (install with pip install minio)
- PIL (Python Imaging Library) library (install with pip install pillow)

### 5 - Excel Webp Image Downloader and Converter

[Script Source](./python/web-converter-excel.py)

This Python script reads image URLs from an Excel file with images.xlsx file name and ImageURL column , downloads the images, converts them to JPEG format, and saves them in separate directories. The original image names are preserved during the process.

#### Prerequisites

- Python 3.x
- pandas library (`pip install pandas`)
- requests library (`pip install requests`)
- Pillow library (`pip install pillow`)
- openpyxl library (`pip install openpyxl`)

#### Run the script

```
pip install -r requirement-webp-excel-converter.txt
python web-converter-excel.py
```

### 6 - Latency Monitoring Script 

[Script Source](./python/report-from-elastic.py)

This script monitors the latency of specific request URIs on an Elasticsearch server and sends alerts to a Telegram webhook if latency exceeds a specified threshold.


#### Prerequisites

- Python 3.x
- requests library (`pip install requests`)

#### Configuration

- schema: The protocol to use (e.g., https).

- elastic_address: The address of your Elasticsearch server.

- index_name: The name of the Elasticsearch index.

- api: The Elasticsearch API endpoint (default is _count).

- auth: The authorization token for Elasticsearch.

- telegram_url: The URL of your Telegram webhook.

- server_name_1 and server_name_2: The server names to monitor.

#### Request URIs

The script monitors the following request URIs:
- request_uris_1s: URIs for 1-second latency checks.

- request_uris_2s: URIs for 2-second latency checks.

- request_uris_3s: URIs for 3-second latency checks.

- request_uris_5s: URIs for 5-second latency checks.

#### Functions

- get_count(query)
Sends a GET request to Elasticsearch with the specified query and returns the count of matching documents.

- calculate_percentage(total, gte_2s)
Calculates the percentage of documents with latency greater than or equal to the specified threshold.

- send_to_telegram(alert_data)
Sends an alert to the specified Telegram webhook.

- run_query(latency_second, upper_than_percentage)
Runs the latency query for the specified latency threshold and sends an alert if the percentage of high-latency requests exceeds the specified threshold.

#### Run the script

```
python script_name.py
```