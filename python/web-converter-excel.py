import pandas as pd
import requests
from PIL import Image
import os
import urllib.parse

# Read the Excel file and extract the image URLs from a specific column
excel_file = 'images.xlsx'
image_column = 'ImageURL'
df = pd.read_excel(excel_file)
image_urls = df[image_column]

# Specify the directories
webp_directory = 'webp'
jpeg_directory = 'jpeg'

# Create the directories if they don't exist
os.makedirs(webp_directory, exist_ok=True)
os.makedirs(jpeg_directory, exist_ok=True)

# Download images and convert to JPEG
for index, url in enumerate(image_urls):
    try:
        # Download the image
        response = requests.get(url)
        parsed_url = urllib.parse.urlparse(url)
        image_name = os.path.basename(parsed_url.path)
        image_path = os.path.join(webp_directory, image_name)
        with open(image_path, 'wb') as file:
            file.write(response.content)

        # Convert to RGB if image mode is RGBA
        im = Image.open(image_path)
        if im.mode == 'RGBA':
            im = im.convert('RGB')

        # Convert to JPEG
        jpeg_path = os.path.join(jpeg_directory, os.path.splitext(image_name)[0] + '.jpg')
        im.save(jpeg_path, 'JPEG')
        print(f'Successfully converted image {index}')
    except Exception as e:
        print(f'Error occurred for image {index}: {str(e)}')