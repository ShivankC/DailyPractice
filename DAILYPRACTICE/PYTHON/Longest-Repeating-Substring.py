# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

txt = str(input("Enter a string: "))

curr = ""
longest = ""

i = 0
stp = 0
while i < len(txt):
    #print(txt[i], i, curr, longest, stp, len(txt), txt[len(txt) - 1])
    if txt[i] not in curr:
        if curr == "":
            stp = i
        curr += txt[i]
    else:
        if len(curr) > len(longest):
            longest = curr
        curr = ""
        i = stp
    i += 1

if len(curr) > len(longest):
    longest = curr
print(longest)