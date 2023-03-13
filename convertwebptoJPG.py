from PIL import Image
import pathlib
import shutil

webp_dir = pathlib.Path('D:/webp')
jpg_dir = pathlib.Path('F:/data/trusti')

for file_path in webp_dir.glob('*.webp'):
    jpg_path = jpg_dir / (file_path.stem + '.jpg')
    if not jpg_path.exists():
        img = Image.open(file_path)
        img.save(jpg_path, 'JPEG')
        #shutil.copy2(jpg_path, jpg_dir)
        print (img, "converted")
