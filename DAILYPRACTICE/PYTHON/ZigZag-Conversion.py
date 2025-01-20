# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:       
# P   A   H   N                                                                                                        P    A    H    N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"
 
#s  a
#h v n
#i    k

# Constraints:

# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

txt = list(input("Enter the text: "))
rows = int(input("Enter the number of rows: "))

grid = []
for i in range(rows):
    grid.append([])

count = 0
count_state = True
for i in range(len(txt)):
    grid[count].append(txt[i])
    if count + 1 == rows:
        count_state = False
    elif count == 0:
        count_state = True
    if count_state:
        count += 1
    else:
        count -= 1

ans = ""
for i in range(rows):
    for char in grid[i]:
        ans += char

print(ans)