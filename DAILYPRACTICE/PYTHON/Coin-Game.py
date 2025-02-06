# You and your friend are playing a coin game. There are n coins in a line. On each turn, a player can take either 1 or 2 coins. The player who takes the last coin wins. Given n, determine if you (starting first) can always win.
# Input: n = 5
# Output: True

n = int(input("Enter the number of coins: "))

dp = [False] * (n + 1)
if n >= 1:
    dp[1] = True
if n >= 2:
    dp[2] = True
for i in range(3, n + 1):
    dp[i] = not (dp[i - 1] and dp[i - 2])

print(dp[n])