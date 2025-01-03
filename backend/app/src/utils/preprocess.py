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










import os

from PIL import Image, ImageOps
def preprocess_all_images():
   
    """
    Preprocess all images in the 'backend/app/data/raw' directory (including subdirectories)
    and save them into the 'backend/app/data/processed' directory while preserving the subdirectory structure.
    """
    # Define absolute paths for the raw and processed directories
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    RAW_DIR = os.path.join(BASE_DIR, "../../data/raw")
    PROCESSED_DIR = os.path.join(BASE_DIR, "../../data/processed")


    # Initialize counters
    processed_counter = 0
    skipped_counter = 0
    error_counter = 0


    # Walk through all subdirectories and files in the raw directory
    for root, _, files in os.walk(RAW_DIR):
        #print(f"Searching in: {root}")
        for file in files:
           

            if file.lower().endswith(('jpg', 'jpeg', 'png')):
                input_path = os.path.join(root, file)

                # Calculate the relative path from RAW_DIR to the current file's folder
                relative_path = os.path.relpath(root, RAW_DIR)

                # Create the corresponding subdirectory in the processed directory
                sub_dir = os.path.join(PROCESSED_DIR, relative_path)

                # Construct the output path for the processed image
                output_path = os.path.join(sub_dir, f"{os.path.splitext(file)[0]}_preprocessed.jpg")

                # Ensure the subdirectory in the processed directory exists
                os.makedirs(sub_dir, exist_ok=True)

                # Skip already preprocessed files
                if os.path.exists(output_path):
                    
                    skipped_counter += 1
                    continue

                # Preprocess the image
                try:
                    preprocess_single_image(input_path, output_path)
                    processed_counter += 1
                except Exception as e:
                    error_counter += 1
                    print(f"Error processing {input_path}: {e}")

    # Summary
    print(f"Processed {processed_counter} files successfully.")
    print(f"Skipped {skipped_counter} files already processed.")
    print(f"Encountered errors processing {error_counter} files.")
