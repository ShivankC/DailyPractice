# Given an array of size n-1 containing numbers from 1 to n in random order, find the missing number.
# Input: [3, 7, 1, 2, 8, 4, 5] (for n=8)
# Output: 6

n = int(input("Enter length of array: "))
arr = input("Enter an array seperated by spaces: ").split(" ")
arr.sort()

for i in range(n - 2):
    if int(arr[i]) + 1 != int(arr[i + 1]):
        print(int(arr[i]) + 1)