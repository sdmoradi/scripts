import os
import requests

nexus_address = "nexus.test.com"

base_url = "https://" + nexus_address + "/service/rest/v1/components"
repository = "nuget"
download_directory = "./packages/"

def download_asset(url, file_path):
    response = requests.get(url)
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Asset downloaded: {file_path}")

def get_download_urls(response_json):
    component_items = response_json["items"]
    continuation_token = response_json.get("continuationToken")
    download_urls = []
    
    for item in component_items:
        component_name = item["name"]
        component_version = item["version"]
        assets = item["assets"]
        
        for asset in assets:
            download_urls.append(asset["downloadUrl"])
            asset_name = f"{component_name}.{component_version}.nupkg"
            save_file_path = os.path.join(download_directory, asset_name)
            download_asset(asset["downloadUrl"], save_file_path)
    
    return download_urls, continuation_token

def fetch_component_data(url):
    response = requests.get(url)
    return response.json()

# Initial request
initial_url = f"{base_url}?repository={repository}"
response_json = fetch_component_data(initial_url)
download_urls, continuation_token = get_download_urls(response_json)

# Fetch subsequent pages if continuation token exists
while continuation_token is not None:
    continuation_url = f"{base_url}?continuationToken={continuation_token}&repository={repository}"
    response_json = fetch_component_data(continuation_url)
    download_urls, continuation_token = get_download_urls(response_json)