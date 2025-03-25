# https://orac2.info/problem/221/
import sys
sys.setrecursionlimit(10**7)
 
r, c = map(int, input().split())
tx, ty = map(int, input().split())
target = (tx - 1, ty - 1)  # starting square
 
at = []  # at stands for atlantis
 
def get_neighbours(x, y):
    adjacent = []
    
    # North
    if x > 0:
        adjacent.append((x - 1, y))
    
    # South
    if x < r - 1:
        adjacent.append((x + 1, y))
    
    # West
    if y > 0:
        adjacent.append((x, y - 1))
    
    # East
    if y < c - 1:
        adjacent.append((x, y + 1))
    
    return adjacent
 
memo = {}
def maxlength(node):
    global memo
 
    if node in memo:
        return memo[node]
 
    children = get_neighbours(node[0], node[1])
    val = at[node[0]][node[1]]
    maxLength = 1  # The current square is part of the path
 
    for i in children:
        if at[i[0]][i[1]] < val:  # check for valid children
            maxLength = max(maxLength, 1 + maxlength(i))
 
    memo[node] = maxLength
    return maxLength
 
for i in range(r):
    at.append(list(map(int, input().split())))  # taking in the map of the city
 
print(maxlength(target))
