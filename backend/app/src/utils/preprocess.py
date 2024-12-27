from PIL import Image, ImageOps
import os

# Constants
TARGET_SIZE = (500, 500)  # Adjust the size as needed
PROCESSED_DIR = "./backend/app/data/processed"

def preprocess_single_image(input_path, output_path=None):
    """
    Resize and add padding to fit the target size.
    
    Args:
        input_path (str): Path to the input file.
        output_path (str, optional): Path to save the processed image. If None, save it in PROCESSED_DIR with a modified name.

    Returns:
        str: The path to the saved processed image, or None if an error occurs.
    """
    try:
        # Open the image
        img = Image.open(input_path)

        # Resize and pad the image to the target size
        processed_img = ImageOps.pad(
            img, TARGET_SIZE, method=Image.Resampling.LANCZOS, color=(0, 0, 0)
        )

        # If no output path is provided, use the default directory and naming convention
        if output_path is None:
            base_name = os.path.basename(input_path)
            file_name, _ = os.path.splitext(base_name)
            output_path = os.path.join(PROCESSED_DIR, f"{file_name}_preprocessed.jpg")

        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Save the processed image
        processed_img.save(output_path)
        print(f"Image saved to {output_path}")

        return output_path

    except Exception as e:
        print(f"Error preprocessing image {input_path}: {e}")
        return None
