from PIL import Image

macOS = Image.open("/Users/massadraza/Desktop/Python/Editing_Images/macOS.jpg")
Windows = Image.open("/Users/massadraza/Desktop/Python/Editing_Images/Windows10.jpg")
r1, g1, b1 = macOS.split()  
r2, g2, b2 = Windows.split() 

new_img = Image.merge("RGB", (r2, g1, b2))  
new_img.show() 

# Merging different channels from different images into one.
