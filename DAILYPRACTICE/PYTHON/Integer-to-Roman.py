# Seven different symbols represent Roman numerals with the following values:

# Symbol        Value
# I        1
# V        5
# X        10
# L        50
# C        100
# D        500
# M        1000
# Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

# If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
# If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
# Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
# Given an integer, convert it to a Roman numeral.

 

# Example 1:

# Input: num = 3749

# Output: "MMMDCCXLIX"

# Explanation:

# 3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
#  700 = DCC as 500 (D) + 100 (C) + 100 (C)
#   40 = XL as 10 (X) less of 50 (L)
#    9 = IX as 1 (I) less of 10 (X)
# Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
# Example 2:

# Input: num = 58

# Output: "LVIII"

# Explanation:

# 50 = L
#  8 = VIII
# Example 3:

# Input: num = 1994

# Output: "MCMXCIV"

# Explanation:

# 1000 = M
#  900 = CM
#   90 = XC
#    4 = IV
# 10 20 30 40 50 60 70 80 90
# x  xx xxx      lx lxx lxxx

ans = ""

num = list(str(input("Enter a number: ")))
for i in range(len(num)):
    num[i] = int(num[i])
    num[i] = (num[i] * 10 ** (len(num) - 1 - i))
    while num[i] != 0:
        if num[i] >= 1000:
            ans += "M"
            num[i] -= 1000
        elif num[i] >= 500:
            if num[i] != 900:
                ans += "D"
                num[i] -= 500
            else:
                ans += "CM"
                num[i] -= 900
        elif num[i] >= 100:
            if num[i] != 400:
                ans += "C"
                num[i] -= 100
            else:
                ans += "CD"
                num[i] -= 400
        elif num[i] >= 50:
            if num[i] != 90:
                ans += "L"
                num[i] -= 50
                for j in range(int(num[i] / 10)):
                    ans += "X"
                    num[i] -= 10
            else: 
                ans += "XC"
                num[i] -= 90
        elif num[i] >= 10:
            if num[i] != 40:
                for j in range(int(num[i] / 10)):
                    ans += "X"
                    num[i] -= 10
            else: 
                ans += "XL"
        elif num[i] >= 0:
            if num[i] == 4:
                ans += "IV"
                num[i] -= 4
            elif num[i] == 9:
                ans += "IX"
                num[i] -= 9
            if num[i] >= 5:
                ans += "V"
                num[i] -= 5
                for j in range(int(num[i])):
                    ans += "I"
                    num[i] -= 1
            elif num[i] >= 0:
                for i in range(int(num[i])):
                    ans += "I"
                    num[i] -= 1

print(ans)