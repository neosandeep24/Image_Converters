import os
from PIL import Image
import pillow_heif

pillow_heif.register_heif_opener()

def convert_heic_to_png(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".heic"):
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + ".png"
            output_path = os.path.join(output_folder, output_filename)

            try:
                image = Image.open(input_path)
                image.save(output_path, "PNG")
                print(f"✅ Converted: {filename} -> {output_filename}")
            except Exception as e:
                print(f"❌ Failed to convert {filename}: {e}")

# Update these paths based on your requirement 
# verified working
input_dir = ""
output_dir = ""
convert_heic_to_png(input_dir, output_dir)
