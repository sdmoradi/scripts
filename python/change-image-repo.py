import os

source_repo="quay.io"
destination_repo="docker.hasti.co"


def replace_registry_url(image_name):
    return image_name.replace(source_repo, destination_repo)

def pull_image(image_name):
    os.system(f"docker pull {image_name}")

def push_to_registry(image_name):
    os.system(f"docker push {image_name}")

def docker_tag(image_name,new_image_name):
    os.system(f"docker tag {image_name} {new_image_name}")

# Path to the text file containing the image names
image_list_file = "image_list.txt"

# Read the image names from the text file
with open(image_list_file, "r") as file:
    image_names = file.read().splitlines()

# Process each image name
for image_name in image_names:
    # Replace the registry URL
    new_image_name = replace_registry_url(image_name)
    
    # Pull the image
    pull_image(image_name)
    
    docker_tag(image_name,new_image_name)
    #print(new_image_name)
    # Push the image to the registry
    push_to_registry(new_image_name)
