from PIL import Image

# Each pixel represents a single color.
# Each color is created by the RGB model mixing the intensity of red, green and blue
# Each amount of red, green, blue can be from 0 to 255. (Representing each r/g/b needs 8 bits or 1 byte. Each pixels needs 3 bytes)
# Q1. How many different digital colors in total?

#img = Image.new('RGB', (1, 1), color = 'red')
img = Image.new('RGB', (1, 1), (250, 100, 100))

# Save the image to an image file named one_pixel
img.save('one_pixel.png')

img.show()
img.close()