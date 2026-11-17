"""
By using Python Imaging Library (PIL), we can see the images properly
and process them easily

To install PIL(pillow), try type the following command in your terminal:
pip install Pillow
or: pip3 install Pillow
"""
from PIL import Image
img = Image.open("rick_and_morty.png")

print(f"Image format: {img.format}")
print(f"Image size: {img.size}")
print("Image width:", img.width)
print("Image height:", img.height)

img.show()
img.close()
