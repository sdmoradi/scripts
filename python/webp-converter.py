from minio import Minio
from io import BytesIO
from PIL import Image
import os

# Set up MinIO client
minio_client = Minio(
    "minio-api-address",
    access_key="",
    secret_key="",
    secure=True
)

# Set the name of the bucket to search
bucket_name = "stage"

# Set the output format to convert to (e.g., JPEG)
output_format = "JPEG"

# Set the directory paths
webp_dir = "webp-images"
converted_dir = "webptojpg-images"

# Create directories if they don't exist
os.makedirs(webp_dir, exist_ok=True)
os.makedirs(converted_dir, exist_ok=True)

# Search for .webp files in the specified bucket
objects = minio_client.list_objects(bucket_name, recursive=True)
webp_files = [obj.object_name for obj in objects if obj.object_name.endswith(".webp")]


# Write webp file list to a text file
with open("webp-list.txt", "w") as file:
    file.write("\n".join(webp_files))

# Initialize a list to store the addresses of images that cannot be converted
not_convertible_images = []

# with open("webp-list.txt", "r") as file:
#     webp_files = file.read().splitlines()

# Iterate over the .webp files, download, convert, and upload
for webp_file in webp_files:
    # Download the .webp file as bytes
    data = minio_client.get_object(bucket_name, webp_file)
    webp_bytes = BytesIO(data.read())

    # Save the .webp file to the webp-images directory
    webp_path = os.path.join(webp_dir, os.path.basename(webp_file))
    with open(webp_path, "wb") as file:
        file.write(webp_bytes.getvalue())

    try:
        # Open the .webp image using PIL
        image = Image.open(webp_path)

        # Convert the image to RGB mode if it is RGBA
        if image.mode == "RGBA":
            image = image.convert("RGB")
        # Convert the image to .jpg format
        jpg_path = os.path.join(converted_dir, os.path.splitext(os.path.basename(webp_file))[0] + ".jpg")
        image.save(jpg_path, format=output_format)

        # Upload the converted .jpg file to MinIO
        with open(jpg_path, "rb") as file:
            minio_client.put_object(bucket_name, webp_file.replace(".webp", ".jpg"), file, os.stat(jpg_path).st_size)

        print(f"Converted and uploaded {webp_file}")
    except Exception as e:
        not_convertible_images.append(webp_file)
        print(f"Failed to convert {webp_file}: {e}")

# Write the addresses of images that couldn't be converted to a text file
with open("webp-notconvert.txt", "w") as file:
    file.write("\n".join(not_convertible_images))

print("Conversion and upload completed!")