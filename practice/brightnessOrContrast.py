from PIL import Image, ImageEnhance

def adjust_brightness(input_image_path, output_image_path, factor):
    img = Image.open(input_image_path)
    enhancer = ImageEnhance.Brightness(img)
    img_enhanced = enhancer.enhance(factor)
    img_enhanced.save(output_image_path)
    return img_enhanced

def adjust_contrast(input_image_path, output_image_path, factor):
    img = Image.open(input_image_path)
    enhancer = ImageEnhance.Contrast(img)
    img_enhanced = enhancer.enhance(factor)
    img_enhanced.save(output_image_path)
    return img_enhanced

adjust_brightness('assets/original2.jpg', 'out/brightness2.jpg', 1.5)
