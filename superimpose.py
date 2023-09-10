import cv2
from PIL import Image

def superimpose_image(segmented_image, background_image) :
    
    background_image = background_image.resize((segmented_image.width, segmented_image.height))
    
    x = (background_image.width - segmented_image.width)//2
    y = (background_image.height - segmented_image.height)//2
    
    mask = segmented_image.convert("L")
    mask = mask.point(lambda p: p > 0 and 255)
    
    background_image.paste(segmented_image, (x,y), mask)
    
    return background_image