# Write a python program to read a content of one file and write into an another file by
# creating a text file.

#Creating the Sample text file
file_path = "sampleText1.txt"

with open(file_path, 'w') as file :
    file.write("""A girl is playing there badminton.
        The scenary is beautiful.
        The birds are flying in the sky.
        The sky is cloudy.
        Alphabets consists of vowels and consonants.""")

with open("sampleText1.txt",'r') as fileReader :
    readFile = fileReader.read();

file_path = "sampleText2.txt"

with open(file_path, 'a+') as fileWrite :
    fileWrite.write(readFile)

    print(readFile)