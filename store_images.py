import os
import requests

def send_images_to_api(folder_path, api_url):
    # List all files in the folder
    image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path)]

    for image_file in image_files:
        with open(image_file, "rb") as f:
            file_data = f.read()

        # Send the image file to the REST API using a POST request
        response = requests.post(
            api_url,
            files={"image": (os.path.basename(image_file), file_data)},
        )

        if response.status_code == 200:
            print(f"Successfully uploaded {image_file}: {response.json()}")
        else:
            print(f"Failed to upload {image_file}: {response.status_code} {response.text}")

def main():
    folder_path = "images"
    api_url = "http://localhost:5000/store"
    send_images_to_api(folder_path, api_url)

if __name__ == "__main__":
    main()
