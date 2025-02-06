# Given an array where every element appears twice except for one, find the single element.
# Input: [4, 3, 2, 4, 1, 3, 2]
# Output: 1

arr = input("Enter an array seperated by spaces: ").split(" ")
arr.sort()

tf = False
for i in range(len(arr) - 1):
    # print(arr[i])
    if arr[i] != arr[i - 1] and arr[i] != arr[i + 1]:
        print(arr[i])
        tf = True

if not tf:
    print(arr[len(arr) - 1])