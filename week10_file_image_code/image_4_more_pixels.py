from PIL import Image

# Create an image of c by r (width by height)
c = 255
r = 255
img_pixels = Image.new('RGB', (c, r)) 

for i in range(r):
    for j in range(c):
        img_pixels.putpixel((j, i), (i, j, 255))

# Save the image to an image file named more_pixels
img_pixels.save('./more_pixels.png')