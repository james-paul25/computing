# this is a meme during the mr and ms intrams pageant where ccj win and ctas and ccis is on bottom

# importing library that will use from PIL
from PIL import Image, ImageDraw, ImageFont

# i will import platform for detecting OS
# i use linux and some font are not available in linux
import platform

# detect OS
system = platform.system()

if system == "Windows":
    font_path = "C:/Windows/Fonts/arial.ttf"  # windows path get the source from gemini
else:
    # assume Linux
    font_path = ImageFont.truetype("DejaVuSans-BoldOblique.ttf", 50) #font from linux

# making a main canvas for the meme
mainCanvas = Image.new("RGBA", (1080,1350), "white")

# make background canvas
bgCanvas = Image.new("RGBA", (1080,1350), "white")

# load images to use in background
bg1 = Image.open("activities/activity1/asset/3.png")
bg2 = Image.open("activities/activity1/asset/4.png")
bg3 = Image.open("activities/activity1/asset/5.png")

# now insert or paste it on bgCanvas or backgroundCanvas
bgCanvas.paste(bg1, (0,0))
bgCanvas.paste(bg2, (382,0))
bgCanvas.paste(bg1, (769,0))

# now put the background in mainCanvas
mainCanvas.paste(bgCanvas, (0,0), bgCanvas)

# call the ImageDraw to add the texts
draw = ImageDraw.Draw(mainCanvas)

# i add text here so i will just call them when added the text using Draw
ccjText = "During Paugnat ug Pasundayag \nCCJ be like: "
ccisCtasText = "CTAS and CCIS: "

# make new canva for putting the image of the winner of pageant
# the color of this canva is deep strong red close to crimson
pageantWinnerCanvas = Image.new("RGBA", (540, 719), "white")

# load image of the winner
winnerImg = Image.open("activities/activity1/asset/ccjpageant.png")
# resize the winnerImg
resizedWinnerImg = winnerImg.resize((540, 720))

# load images from ccj side
ccjImg1 = Image.open("activities/activity1/asset/ccj.png")
ccjImg2 = Image.open("activities/activity1/asset/happy.png")
ccjImg3 = Image.open("activities/activity1/asset/happy1.png")

# resize the background image contains ccj
resizedCCJBg = bg1.resize((540, 719))

# paste the resized background of CCJ logo in pageantWinnerCanvas
pageantWinnerCanvas.paste(resizedCCJBg, (10,10))

# paste the resized winnerImg to pageantWinnerCanvas
pageantWinnerCanvas.paste(resizedWinnerImg, (0, -1), resizedWinnerImg)

# now we will resize the images from ccj
resizedCCJImg1 = ccjImg1.resize((1080, 719))
resizedCCJImg2 = ccjImg2.resize((836, 600))
resizedCCJImg3 = ccjImg3.resize((595, 464))

# now we will paste the images from ccj side in canvas using paste(img, (w,h)) method
# first to paste will be in the back side 
mainCanvas.paste(resizedCCJImg1, (0, 0), resizedCCJImg1)

# paste the pageantWinnerCanvas in main canvas
mainCanvas.paste(pageantWinnerCanvas, (0,0), pageantWinnerCanvas)

mainCanvas.paste(resizedCCJImg3, (540, 256), resizedCCJImg3)
mainCanvas.paste(resizedCCJImg2, (267, 164), resizedCCJImg2)

# load images from ccis and ctas side
sadImg1 = Image.open("activities/activity1/asset/opaw.png")
sadImg2 = Image.open("activities/activity1/asset/jordan.png")
sadImg3 = Image.open("activities/activity1/asset/me.png")
sadImg4 = Image.open("activities/activity1/asset/cat.png")

# now we will resize the images from ctas and ccis side
resizedSadImg1 = sadImg1.resize((581, 515))
resizedSadImg2 = sadImg2.resize((533, 711))
resizedSadImg3 = sadImg3.resize((372, 711))
resizedSadImg4 = sadImg4.resize((570, 565))

# now we will paste the images from ctas and ccis side where they are sad hahahha
mainCanvas.paste(resizedSadImg2, (0, 639), resizedSadImg2)
mainCanvas.paste(resizedSadImg3, (735, 639), resizedSadImg3)
mainCanvas.paste(resizedSadImg4, (636, 1068), resizedSadImg4)
mainCanvas.paste(resizedSadImg1, (243, 836), resizedSadImg1)

# add text here in bottom of the code, coz the first you put will put in the back - i think hahaha
draw.text((30,21), ccjText, fill="black", font=font_path)
draw.text((30,742), ccisCtasText, fill="black", font=font_path)

# to show the image
mainCanvas.show()

# to save the output in out folder in jpg format
mainCanvas.save("activities/activity1/out/CSELEC3_BSCS3A_DacaldacalJamesPaul_Activity1.png")


