import os
import base64

def encode_and_save_image(image_path, output_folder, output_filename):
    with open(image_path, "rb") as f:
        file_data = f.read()

    encoded_image = base64.b64encode(file_data).decode("utf-8")

    output_path = os.path.join(output_folder, output_filename)
    with open(output_path, "w") as f:
        f.write(encoded_image)

def process_images(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for subfolder in os.listdir(input_folder):
        subfolder_path = os.path.join(input_folder, subfolder)
        if os.path.isdir(subfolder_path):
            image_files = os.listdir(subfolder_path)
            for index, image_file in enumerate(image_files):
                image_path = os.path.join(subfolder_path, image_file)
                output_filename = f"{subfolder}_{index}.txt"
                encode_and_save_image(image_path, output_folder, output_filename)

def main():
    input_folder = "/images"
    output_folder = "/b64_images"
    process_images(input_folder, output_folder)

if __name__ == "__main__":
    main()
