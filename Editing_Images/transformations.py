from PIL import Image

macOS = Image.open("/Users/massadraza/Desktop/Python/Editing_Images/macOS.jpg")
full_resolution_macOS = macOS.resize((2560, 1600)) 
flip_macOS = macOS.transpose(Image.FLIP_LEFT_RIGHT)
flip_macOS2 = macOS.transpose(Image.FLIP_TOP_BOTTOM) 
spin_macOS = macOS.transpose(Image.ROTATE_180)
spin_macOS2 = macOS.transpose(Image.ROTATE_90)
spin_macOS3 = macOS.transpose(Image.ROTATE_270) 

macOS.show()
full_resolution_macOS.show()
flip_macOS.show()
flip_macOS2.show()
spin_macOS.show()
spin_macOS2.show()
spin_macOS3.show() 

# Learning about image transformations.
