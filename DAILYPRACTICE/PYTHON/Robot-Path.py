# A robot starts at (0,0). It moves based on a given string of directions ("U", "D", "L", "R"). Determine if it returns to the origin.
# Input: "UDLR"
# Output: True

U = 0
D = 0
L = 0
R = 0

path = input("Enter inputs: ")

for char in path:
    if char == "U":
        U += 1
    elif char == "D":
        D += 1
    elif char == "L":
        L += 1
    elif char == "R":
        R += 1

if U == D and L == R:
    print("True")
else:
    print("False")