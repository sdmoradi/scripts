# Scripts
All scripts for different purposes

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