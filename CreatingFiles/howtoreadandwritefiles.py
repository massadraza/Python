fw = open("example.txt", 'w') 
fw.write("I am testing to see if you can edit files using Python\n")
fw.write('Testing, testing, 1,2,3')
fw.close() 

fr = open('example.txt', 'r')
text = fr.read()
print (text) 
#   Learning how to read and write files using Python Code.