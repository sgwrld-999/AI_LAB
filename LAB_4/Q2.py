list1 = []

print("Enter the numbers separated by spaces:")
input_numbers = input().split()

# Convert the input numbers from string to integers and add them to list1
for num in input_numbers:
    list1.append(int(num))

print("Enter the number you want to find the frequency of:")
num_to_find = int(input())

count = 0
for i in range(len(list1)):
    if num_to_find == list1[i]:
        count += 1

print("The frequency of", num_to_find, "is:", count)

# Input : 1 56 100 4 75 10 1 12
