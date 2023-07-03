# images with python
from PIL import Image, ImageFilter


image = Image.open('./Pokedex/pikachu.jpg')
filtered_image = image.convert('L')
filtered_image = image.filter(ImageFilter.BLUR)
filtered_image.save('grey.png', 'png')
filtered_image.show()
crooked = filtered_image.rotate(90)
crooked.save("grey.png",'png')

print(image.format)
print(image.size)

# to resize an image

img = Image.open('./astro.jpg')
img.thumbnail((400,400)) # allows the image not to be compressed.
img.save('thumbnail.jpg')
print(image.size)
