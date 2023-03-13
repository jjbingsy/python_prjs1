from PIL import Image
import os

# Set the path to the directory containing JPG files
dir_path = 'F:/trusti'

# Loop over all the files in the directory
for filename in os.listdir(dir_path):

    # Check if the file is a JPG image
    if filename.lower().endswith('.jpg'):

        # Set the full path to the file
        filepath = os.path.join(dir_path, filename)

        # Open the image file
        with Image.open(filepath) as img:

            # Get the dimensions of the image
            width, height = img.size

            # Calculate the center point of the image
            center = width // 2

            # Crop the image to the right-vertical half
            right_half = img.crop((center, 0, width, height))

            # Overwrite the original image file with the right-vertical half
            right_half.save(filepath)

            print(f"Right-vertical half of '{filename}' saved to '{dir_path}'.")
