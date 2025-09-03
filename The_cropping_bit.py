# import libs, for install: pip install autocrop, pip install pillow,run sepratly 
from PIL import Image
from autocrop import Cropper
#defining function
cropper = Cropper()
def crop_image(image_path):
    # Get a Numpy array of the cropped image
    image= cropper.crop(image_path)
    # print the image array 
    print(image)
    # Convert the array back to an image
    cropped_image = Image.fromarray(image)
    # Save the cropped image
    cropped_image.save('cropped_image_AW.jpg')