from PIL import Image, ImageFilter
import os
import sys

image_folder = sys.argv[1]
image_output = sys.argv[2]

if(not os.path.exists(image_output)):
    os.makedirs(image_output)

for filename in os.listdir(image_folder):
    if(filename.endswith("jpg")):
        img = Image.open(f"{image_folder}{filename}")
        name = os.path.splitext(filename)[0]
        img = img.convert("L")
        img.save(f"{image_output}{name}.png", 'png')
        print("done")
