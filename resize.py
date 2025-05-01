from PIL import Image
import os

# Input and Output folders
input_folder = 'input'
output_folder = 'output'

# Resize dimensions
target_size = (650, 650)

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)

    # Check if file is an image
    if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.webp')):
        try:
            # Open image and resize using Resampling.LANCZOS
            img = Image.open(input_path)
            img = img.resize(target_size, Image.Resampling.LANCZOS)

            # Save as JPG in output folder with original name (but .jpg extension)
            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(output_folder, f"{base_name}.jpg")
            img = img.convert("RGB")  # Ensure RGB for JPEG
            img.save(output_path, "JPEG")

            print(f"Resized: {filename} → {output_path}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
