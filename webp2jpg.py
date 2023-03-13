from pathlib import Path
from PIL import Image

# Source directory with webp images
src_dir = Path("d:/webp/")

# Destination directory for jpeg images
dst_dir = Path("d:/trusti/")

# Make sure the destination directory exists
dst_dir.mkdir(parents=True, exist_ok=True)

# Iterate over all files in the source directory
for file in src_dir.glob("*.webp"):
    # Open the file using PIL
    with Image.open(file) as img:
        # Convert to jpeg format
        jpeg_img = img.convert("RGB")
        
        # Save the jpeg image to the destination directory
        jpeg_img.save(dst_dir / (file.stem + ".jpg"))
