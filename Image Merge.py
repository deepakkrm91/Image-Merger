import tkinter as tk
from PIL import Image
import os

first_image_path = 'C:/Users/user/Downloads/New folder (7)/New folder (3)/New folder (3)/New folder (2)/2/New folder/WATGZNUUTJ8GHDEX.jpg'
first_image = Image.open(first_image_path)

second_folder_path = 'C:/Users/user/Downloads/New folder (7)/New folder (3)/New folder (3)/New folder (2)/2'
image_files = os.listdir(second_folder_path)

image_files = [f for f in image_files if f.endswith('.jpg')]  # Only include JPG files

for image_file in image_files:
    image_path = os.path.join(second_folder_path, image_file)
    image = Image.open(image_path)
    merged_image = Image.new('RGB', (first_image.width + image.width, max(first_image.height, image.height)))
    merged_image.paste(first_image, (0, 0))
    merged_image.paste(image, (first_image.width, 0))
    merged_image.save(os.path.join(second_folder_path, 'WATGZNUUTJ8GHDEX & ' + image_file))