from rembg import remove
from PIL import Image

def remove_bg(input_image):

    input_image = Image.open(input_image)
    output_image = remove(input_image)
    
    return output_image