# firstly , import the Image from pil 
# then if you want to draw import ImageDraw
from PIL import Image, ImageDraw

# then make variable to load the image, use open() method
img = Image.open("assets/anime.jpg")
img1 = img.crop((200,100,500,200))

# then show the image
img1.show()

# now, we will make canvas to use that , we will use new() method
#img = Image.new(mode="RGBA", size=(500,500), color=(157,221,200,300))

# then, use Image.Draw() then the parameter is the new canvas
#draw = ImageDraw.Draw(img)

# to draw rectangle you can call rectangle parameters is the x and y the outline, and fill
#draw.rectangle([100,200,150,250], outline="black", fill="white")
#img.show()

# to draw polygon or triangle
#draw.polygon([(200, 50), (200,100), (50,100)], outline="black", fill="white")
#img.show()

# to draw circle/ellipsis
#draw.ellipse([100, 200, 300, 400], outline="black", fill="white")
#img.show()
