# Creating a file and writing some text to it
file_path = "Ex.txt"
with open(file_path, 'w') as file:
    file.write("This is an example text file to demonstrate character counting in Python.\n")

# Reading a specific number of characters from the file and printing them
with open("Ex.txt", 'r') as f:
    textReader = f.read()

# The characters to search for
characters_to_search = "is"
count = 0

# Loop through each character in the textReader
for char in textReader:
    # Check if the current character or the next two characters form the specified sequence
    if char == characters_to_search[0] and textReader[textReader.index(char):textReader.index(char) + len(characters_to_search)] == characters_to_search:
        count += 1

print(f"The number of occurrences of the characters '{characters_to_search}' is: {count}")
