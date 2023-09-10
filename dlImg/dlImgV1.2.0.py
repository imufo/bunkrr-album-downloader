import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from tqdm import tqdm

# Gallery URL
gallery_url = input("Enter gallery URL: ")

# Send an HTTP GET request to the gallery URL
response = requests.get(gallery_url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all anchor tags with href attributes
    # anchor_tags = soup.find_all("a", href=True)
    # Find all anchor tags with href attributes containing "/i/"
    anchor_tags = soup.find_all("a", href=lambda href: href and "/i/" in href)
    print(f"Almost {len(anchor_tags)} files will be downloaded!")
    input("Wanna continue?")

    # Create a folder to save the downloaded images
    download_folder = "downloaded_images"
    os.makedirs(download_folder, exist_ok=True)

    # Initialize a progress bar for downloading images
    progress_bar = tqdm(total=len(anchor_tags), unit="image")

    # Download the images linked in href attributes of anchor tags
    for i, anchor_tag in enumerate(anchor_tags):
        href = anchor_tag["href"]
        if "/i/" in href:  # Check if it's an image link
            image_page_url = f"https://bunkrr.su{href}"  # Construct the image page URL
            image_page_response = requests.get(image_page_url)
            if image_page_response.status_code == 200:
                image_soup = BeautifulSoup(image_page_response.text, "html.parser")
                img_tags = image_soup.find_all("img", src=True)  # Find all img tags with src attribute

                for img_tag in img_tags:
                    if "bunkr.ru" in img_tag["src"]:
                        direct_image_link = img_tag["src"]

                        # Extract the filename from the direct image link
                        filename = os.path.basename(urlparse(direct_image_link).path)

                        # Check if the file already exists in the download folder
                        if not os.path.exists(os.path.join(download_folder, filename)):
                            image_response = requests.get(direct_image_link, stream=True)
                            if image_response.status_code == 200:
                                # Get the total file size to track progress
                                total_size = int(image_response.headers.get('content-length', 0))

                                # Save the image to the download folder with a progress bar
                                with open(os.path.join(download_folder, filename), "wb") as image_file:
                                    with tqdm(total=total_size, unit='B', unit_scale=True, desc=f"Downloading image {i + 1}: {filename}", leave=False) as pbar:
                                        for data in image_response.iter_content(chunk_size=1024):
                                            pbar.update(len(data))
                                            image_file.write(data)

                                print(f"\nDownloaded image {i + 1}: {filename}")
                            else:
                                print(f"Download failed for image {i + 1}: {filename}")
                        else:
                            print(f"\nFile exists: {filename}")

            progress_bar.update(1)  # Update the progress bar

    progress_bar.close()  # Close the progress bar for downloading images

else:
    print(f"Failed to fetch the gallery page. Status code: {response.status_code}")

