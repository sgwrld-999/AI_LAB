list1 = [10, 12, 56, 23, 2, 5, 6, 1]
print(len(list1))
list2 = [1, 56, 100, 4, 75, 10, 1, 12]
print(len(list2))

result = []
for i in range(len(list1)):
    result.append(max(list1[i],list2[i]))

print(result)