from PIL import Image, ImageFilter

def blur_image(input_image_path, output_image_path, radius):
    img = Image.open(input_image_path)
    img_blurred = img.filter(ImageFilter.GaussianBlur(radius=radius))
    img_blurred.save(output_image_path)
    return img_blurred

def sharpen_image(input_image_path, output_image_path):
    img = Image.open(input_image_path)
    img_sharpened = img.filter(ImageFilter.SHARPEN)
    img_sharpened.save(output_image_path)
    return img_sharpened

sharpen_image('assets/original3.jpg', 'out/sharpen3.jpg')
