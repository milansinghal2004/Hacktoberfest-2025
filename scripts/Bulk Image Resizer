from PIL import Image
import os

folder_path = "path/to/images"
width = 800

for file in os.listdir(folder_path):
    path = os.path.join(folder_path, file)
    if file.lower().endswith(('jpg', 'jpeg', 'png')):
        img = Image.open(path)
        ratio = width / img.width
        height = int(img.height * ratio)
        img = img.resize((width, height))
        img.save(path)
        print(f"Resized: {file}")
