# https://orac2.info/problem/56/
import sys
sys.setrecursionlimit(10**7)
 
R, C = map(int, input().split())
 
cave = [list(input().strip()) for _ in range(R)]  # Read the cave as a list of lists of characters
 
def neighbours(x, y, a, b):
    out = []
    # Check all four directions
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:  # Check if the new coordinates are within bounds
            if cave[nx][ny] == "." and (nx, ny) != (a, b):
                out.append((nx, ny))
    return out
 
answer = 1
 
def search(x, y, a, b):
    global answer
    neighbours_ = [":p"]
    
    while len(neighbours_) < 2:
        neighbours_ = neighbours(x, y, a, b)
        if len(neighbours_) == 0:
            return
        if len(neighbours_) == 1:
            a, b = x, y
            x = neighbours_[0][0]
            y = neighbours_[0][1]
        else:
            answer += len(neighbours_) - 1
            for nx, ny in neighbours_:
                search(nx, ny, x, y)
            return
 
search(0, 0, 0, 0)
 
print(answer)
