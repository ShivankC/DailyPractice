# There are n prisoners and m chocolates. The chocolates are distributed sequentially, starting from prisoner 1 to n, then wrapping around. The last prisoner to receive a chocolate gets poisoned. Given n and m, determine which prisoner gets poisoned.
# Input: n = 5, m = 2
# Output: 2

n = int(input("Enter the number of prisioners: "))
m = int(input("Enter the number of chocolates: "))

# ans = 0
# while m > 0:
#     for i in range(n):
#         ans = i + 1
#         m -= 1
#         if m <= 0:
#             break

# print(ans)

if n >= m:
    print(m)
else:
    ans = 0
    while m % n > 0:
        ans += 1
        m -= 1      

    print(ans)