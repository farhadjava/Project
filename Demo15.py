file = open("Demo15.txt",'w')
file.write("This is text written to the file")
file.close()

file = open("Demo15.txt",'r')
contain = file.read()
print(contain)
file.close()

file = open("Demo15.txt",'w')
file.write("This is the new line")
file.close()