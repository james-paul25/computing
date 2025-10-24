from PIL import Image

def jpg_to_png_converter(jpg_file_path, png_file_path):
    img = Image.open(jpg_file_path)
    img.save(png_file_path, 'PNG')

jpg_to_png_converter("assets/ghost.jpg", "out/ghost_converted.png")
jpg_to_png_converter("assets/bg1.jpg", "out/bg1_converted.png")
jpg_to_png_converter("assets/bg2.jpg", "out/bg2_converted.png")
jpg_to_png_converter("assets/bg3.jpg", "out/bg3_converted.png")