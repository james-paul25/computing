from PIL import Image

img = Image.open('assets/original1.jpg').convert('L')

#img.show()
img.save('out/grayscale1.jpg')