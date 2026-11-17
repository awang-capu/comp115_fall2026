from PIL import Image

# Create an image of 3 by 2 (width by height)
img_pixels = Image.new('RGB', (2, 1)) 

pixels = [(0, 0, 0), (0, 255, 0)]
img_pixels.putdata(pixels)

# Save the image to an image file named pixels
img_pixels.save('./two_pixels.png')

img_pixels.show()
img_pixels.close()