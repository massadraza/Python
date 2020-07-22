from PIL import Image

img = Image.open("/Users/massadraza/Desktop/Python/Editing_Images/macOS.png") 
area = (300, 400, 600, 800 ) 
cropped_img = img.crop(area)
img.show()
cropped_img.show()

# Learning how to crop images using Python Code

