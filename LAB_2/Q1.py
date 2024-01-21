#Create a file called “example.txt” with some text in it. Save the file in the same folder
# as that of the Python file. Read this text file using Python.
with open("/Users/siddhantgond/AI_LAB/LAB_2/example.txt","r") as fileReader :
    lines = fileReader.read()
print(lines)

