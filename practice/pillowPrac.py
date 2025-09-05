# firstly , import the Image from pil 
# then if you want to draw import ImageDraw
from PIL import Image, ImageDraw

# then make variable to load the image, use open() method
img = Image.open("assets/anime.jpg")

# then show the image
img.show()

# now, we will make canvas to use that , we will use new() method
img = Image.new(mode="RGBA", size=(500,500), color=(157,221,200,300))

# then, use Image.Draw() then the parameter is the new canvas
draw = ImageDraw.Draw(img)
# to draw rectangle you can call rectangle parameters is the x and y the outline, and fill
draw.rectangle([100,200,150,250], outline="black", fill="white")
img.show()



