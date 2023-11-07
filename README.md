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