# Write a program to append another line of text in the text file
# (created in the 2nd question) and display the text file.
with open("example.txt", 'a+') as file:
    input_text = input("Enter the text you want to append in the file: ")
    file.write(input_text + "\n")
    file.seek(0)

    file_reader_text = file.read()

    print("Printing the contents of the file:")
    print(file_reader_text)
