def isPrime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True


def countOfOddNum(lst):
    countOdd = 0
    countPrime = 0
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            countOdd += 1
        if isPrime(lst[i]):
            countPrime += 1

    return countOdd, countPrime


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_count, prime_count = countOfOddNum(numbers)
print("Count of odd numbers:", odd_count)
print("Count of Even numbers:", len(numbers) - odd_count)
print("Count of prime numbers:", prime_count)
print("Count of Non-prime numbers:", len(numbers) - odd_count)
