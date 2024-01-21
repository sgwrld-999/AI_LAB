'''4. Write a function in python to count the number of lines from a text file "text.txt"
which is not starting with an alphabet "T".
i. Example: The file "text.txt" contains the following lines:
A girl is playing there badminton.
The scenary is beautiful.
The birds are flying in the sky.
The sky is cloudy.
Alphabets consists of vowels and consonants.
Display the output. '''

# Define the file path
file_path = "The_T_Checking_File.txt"

# Open the file for writing and allow the user to input data
with open(file_path, 'w') as file:
    file.write(input("Enter the file data"))

# Open the file for reading
with open(file_path, 'r') as fileReader:

    lines = fileReader.readlines()

    count = 0

    for line in lines:
        if not line.strip().lower().startswith('t'):
            count += 1

    print("Number of lines not starting with 'T': " + str(count))
