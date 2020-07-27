from PIL import Image
from PIL import ImageFilter

macOS = Image.open("/Users/massadraza/Desktop/Python/Editing_Images/macOS.jpg")
black_white = macOS.convert("L")
blur = macOS.filter(ImageFilter.BLUR) 
detail = macOS.filter(ImageFilter.DETAIL) 
edges = macOS.filter(ImageFilter.FIND_EDGES)  

black_white.show() 
blur.show() 
detail.show()
edges.show() 
macOS.show() 

# Learning how to convert images into different filters