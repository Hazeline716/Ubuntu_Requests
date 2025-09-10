import requests
import os
import sys
from urllib.parse import urlparse

# Prompt the user for the image URL
url = input("Enter the URL of the image to download: ")

# Define the directory to save the images
save_directory = "Fetched_Images"

# Create the directory if it doesn't already exist
try:
    os.makedirs(save_directory, exist_ok=True)
    print(f"Directory '{save_directory}' created or already exists.")
except OSError as e:
    print(f"Error creating directory: {e}")
    sys.exit(1)

# Extract the filename from the URL
parsed_url = urlparse(url)
filename = os.path.basename(parsed_url.path)

# Handle cases where the URL doesn't have a filename
if not filename or '.' not in filename:
    print("URL does not contain a valid filename. A default filename will be used.")
    # Assign a default filename with a common image extension
    filename = "downloaded_image.jpg"

full_path = os.path.join(save_directory, filename)

# Attempt to download the image
print(f"Attempting to download image from {url}")
try:
    # Use stream=True to handle larger files efficiently
    response = requests.get(url, stream=True, timeout=10)
    # Raise an HTTPError for bad responses (4xx or 5xx)
    response.raise_for_status()

    # Save the image content in binary mode
    with open(full_path, 'wb') as f:
        # Write the content in chunks to save memory
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"Successfully downloaded and saved the image to {full_path}")

except requests.exceptions.RequestException as e:
    # Catch any request-related errors (e.g., connection errors, timeouts, bad status codes)
    print(f"An error occurred during the download: {e}")
except IOError as e:
    # Catch errors that occur while trying to save the file
    print(f"An error occurred while saving the file: {e}")
