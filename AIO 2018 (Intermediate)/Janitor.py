# https://orac2.info/problem/53/
import sys
sys.setrecursionlimit(1000000000)
# solution by JustinWang
# my ahh too lazy to refactor C++
 
# Read the values of r, c, and q from the input file.
r, c, q = map(int, input().split())
 
# Initialize the grid.
grid = []
for i in range(r):
    grid.append(list(map(int, input().split())))
 
# Initialize the changes list.
changes = []
for i in range(q):
    changes.append(list(map(int, input().split())))
 
# Initialize result and top set.
res = 0
top = set()
 
# Function to determine if a cell is a peak.
def com(i, j):
    cur = grid[i][j]
    if i != r - 1 and grid[i + 1][j] > cur:
        return 0
    if i != 0 and grid[i - 1][j] > cur:
        return 0
    if j != c - 1 and grid[i][j + 1] > cur:
        return 0
    if j != 0 and grid[i][j - 1] > cur:
        return 0
    return 1
 
# Calculate initial number of peaks.
for i in range(r):
    for j in range(c):
        if com(i, j):
            top.add((i, j))
        res += com(i, j)
 
print(res)
 
# Define movements for adjacent cells.
movements = [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0]]
 
# Process each change.
for row, col, h in changes:
    row, col = row - 1, col - 1
    grid[row][col] = h
    for i, j in movements:
        newr, newc = row + i, col + j
        if not (0 <= newr < r and 0 <= newc < c):
            continue
        t = com(newr, newc)
        if (newr, newc) in top and not t:
            res -= 1
            top.remove((newr, newc))
        if t and (newr, newc) not in top:
            res += 1
            top.add((newr, newc))
    print(res)
