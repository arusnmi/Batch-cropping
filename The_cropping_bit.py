# import libs, for install: pip install autocrop, pip install pillow,run sepratly 
from PIL import Image
from autocrop import Cropper
#defining function
cropper = Cropper()

# Get a Numpy array of the cropped image
image= cropper.crop('WIN_20250826_15_04_09_Pro.jpg')
# print the image array 
print(image)
# Convert the array back to an image
cropped_image = Image.fromarray(image)
# Save the cropped image
cropped_image.save('cropped_image_AW.jpg')