from PIL import Image, ImageDraw, ImageFont

canvas = Image.new("RGBA", (800,600), (100,101,100,400))
font = ImageFont.truetype("Ubuntu-B.ttf", 50)

draw = ImageDraw.Draw(canvas)

img1 = Image.open("assets/anime.jpg")
img2 = Image.open("assets/jap.jpg")

img1.resize((200,200))
croppedImg2 = img2.crop((1300,1500,1600,2000))

canvas.paste(img1, (10,10))
canvas.paste(croppedImg2, (300,100))

draw.text((200,100), "Multi Image in canvas", fill="white", font=font)

canvas.show()


#text size comes from the ImageFont