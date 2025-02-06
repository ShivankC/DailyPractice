# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters. 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

maap = {
"2": "abc",
"3": "def",
"4": "ghi",
"5": "jkl",
"6": "mno",
"7": "pqrs",
"8": "tuv",
"9": "wxyz"
}

digits = list((input("Enter the number combination: ")))

ans = []
for i in range(len(maap[digits[0]])):
    if len(digits) > 1:
        for j in range(len(maap[digits[1]])):
            if len(digits) > 2:
                for k in range(len(maap[digits[2]])):
                    if len(digits) > 3:
                        for l in range(len(maap[digits[3]])):
                            ans.append(maap[digits[0]][i] + maap[digits[1]][j] + maap[digits[2]][k] + maap[digits[3]][l])
                    else:
                        ans.append(maap[digits[0]][i] + maap[digits[1]][j] + maap[digits[2]][k])
            else:
                ans.append(maap[digits[0]][i] + maap[digits[1]][j])
    else:
        ans.append(maap[digits[0]][i])

print(ans)