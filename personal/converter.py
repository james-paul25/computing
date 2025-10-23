from PIL import Image

img = Image.open("assets/SCHOOL_CLEARANCE.jpg")
img.save("out/SCHOOL_CLEARANCE_BISU_BAL.pdf", format="PDF", resolution=100.0)