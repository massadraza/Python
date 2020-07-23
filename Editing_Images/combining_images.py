from PIL import Image

macOS = Image.open("/Users/massadraza/Desktop/Python/Editing_Images/macOS.jpg")
Windows = Image.open("/Users/massadraza/Desktop/Python/Editing_Images/Windows.png")

area = (256, 256)    
macOS.paste(Windows, area)
macOS.show() 

# Learning how to combine images into one image. 

