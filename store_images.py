import os
import base64
import weaviate

client = weaviate.Client("http://localhost:8080")

def set_up_batch():
   client.batch.configure(
       batch_size=100,
       dynamic=True,
       timeout_retries=3,
       callback=None,
   )

def read_and_encode_images(folder_path):
    # List all files in the folder
    image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path)]

    for image_file in image_files:
        with open(image_file, "rb") as f:
            file_data = f.read()

        # Encode the image file as base64
        encoded_image = base64.b64encode(file_data).decode("utf-8")

        client.data_object.create(
            class_name = "Animals",
            data_object = {
                "image": encoded_image,
                "text": "A random image"
            }
    )

def main():
    folder_path = "/images"
    set_up_batch()
    read_and_encode_images(folder_path)

if __name__ == "__main__":
    main()