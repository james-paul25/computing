# this is a meme during the mr and ms intrams pageant where ccj win and ctas and ccis is on bottom

# importing library that will use from PIL
from PIL import Image, ImageDraw, ImageFont

# i will import platform for detecting OS
# i use linux and some font are not available in linux
import platform

# detect OS
system = platform.system()

if system == "Windows":
    font_path = "C:/Windows/Fonts/arial.ttf"  # windows path from gemini
else:
    # assume Linux
    font_path = ImageFont.truetype("Ubuntu-B.ttf", 50)

# making a main canvas for the meme
canvas = Image.new("RGBA", (1080,1350), "black")

# call the ImageDraw to add the texts
draw = ImageDraw.Draw(canvas)

ccjText = "CCJ be like: "
ccisCtasText = "CTAS and CCIS: "

# make new canva for putting the image of the winner of pageant
# the color of this canva is deep strong red close to crimson
pageantWinnerCanvas = Image.new("RGBA", (540, 719), (207, 17, 17, 255))

# load image of the winner
winnerImg = Image.open("activities/asset/ccjpageant.png")
# resize the winnerImg
resizedWinnerImg = winnerImg.resize((540, 720))

# load images from ccj side
ccjImg1 = Image.open("activities/asset/ccj.png")
ccjImg2 = Image.open("activities/asset/happy.png")
ccjImg3 = Image.open("activities/asset/happy1.png")

# paste the winnerImg to pageantWinnerCanvas
pageantWinnerCanvas.paste(resizedWinnerImg, (0, -1), resizedWinnerImg)

# now we will resize the images from ccj
resizedCCJImg1 = ccjImg1.resize((1080, 719))
resizedCCJImg2 = ccjImg2.resize((836, 600))
resizedCCJImg3 = ccjImg3.resize((595, 464))

# now we will paste the images from ccj side in canvas using paste(img, (w,h)) method
# first to paste will be in the back side 
canvas.paste(resizedCCJImg1, (0, 0), resizedCCJImg1)

# paste the pageantWinnerCanvas in main canvas
canvas.paste(pageantWinnerCanvas, (0,0), pageantWinnerCanvas)

canvas.paste(resizedCCJImg3, (540, 256), resizedCCJImg3)
canvas.paste(resizedCCJImg2, (267, 164), resizedCCJImg2)

# load images from ccis and ctas side
sadImg1 = Image.open("activities/asset/opaw.png")
sadImg2 = Image.open("activities/asset/jordan.png")
sadImg3 = Image.open("activities/asset/me.png")
sadImg4 = Image.open("activities/asset/cat.png")

# now we will resize the images from ctas and ccis side
resizedSadImg1 = sadImg1.resize((581, 515))
resizedSadImg2 = sadImg2.resize((533, 711))
resizedSadImg3 = sadImg3.resize((372, 711))
resizedSadImg4 = sadImg4.resize((570, 565))

# now we will paste the images from ctas and ccis side where they are sad hahahha
canvas.paste(resizedSadImg2, (0, 639), resizedSadImg2)
canvas.paste(resizedSadImg3, (735, 639), resizedSadImg3)
canvas.paste(resizedSadImg4, (636, 1068), resizedSadImg4)
canvas.paste(resizedSadImg1, (243, 836), resizedSadImg1)

draw.text((200,100), ccjText, fill="white", font=font_path)

# to show the image
canvas.show()
