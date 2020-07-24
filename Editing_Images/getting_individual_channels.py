from PIL import Image

macOS = Image.open("/Users/massadraza/Desktop/Python/Editing_Images/macOS.jpg")
r, g, b = macOS.split() 
r.show()
g.show()
b.show() 

 # print(macOS.mode)

 # Learning how to divide image colors and print each image color out. 