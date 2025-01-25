# You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

# Return the number of servers that communicate with any other server. 
# Example : Input: grid = [[1,1,0,0],
#                          [0,0,1,0],
#                          [0,0,1,0],
#                          [0,0,0,1]]
# Output: 4
# Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.

rows = int(input("Enter number of rows: "))

grid = []
for i in range(rows):
    row = input("Enter row " + str(i + 1) + " here: ")
    grid.append(list(row))

checked = []
ans = 0
for i in range(rows):
    rowcount = 0
    currchecked = []
    for j in range(len(grid[0])):
        if grid[i][j] == "1":
            rowcount += 1
            currchecked.append([i, j])
    if rowcount > 1:
        ans += rowcount
        for b in range(len(currchecked)):
            checked.append(currchecked[b])
for i in range(len(grid[0])):
    colcount = 0
    truecolcount = 0
    for j in range(rows):
        if grid[j][i] == "1":
            colcount += 1
            if [j, i] not in checked:
                truecolcount += 1
    if colcount > 1:
        ans += truecolcount

print(ans)