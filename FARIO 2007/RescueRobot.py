# https://orac2.info/problem/46/
w, h = map(int, input().split())
 
grid = []
ux, uy = -1, -1
 
for i in range(h):
    row = input()
    grid.append(row)
    if 'U' in row:
        uy = i
        ux = row.index('U')
 
p = int(input())
steps = []
 
for i in range(p):
    steps.append(input())
 
# Direction map: N, E, S, W
dx = {'N': 0, 'E': 1, 'S': 0, 'W': -1}
dy = {'N': -1, 'E': 0, 'S': 1, 'W': 0}
 
visited = [[False for _ in range(w)] for _ in range(h)]
visited[uy][ux] = True
 
for step in reversed(steps):
    next_visited = [[False for _ in range(w)] for _ in range(h)]
    dx1 = dx[step]
    dy1 = dy[step]
    
    for y in range(h):
        for x in range(w):
            if not visited[y][x]:
                continue
            
            # Case 1: robot moved from previous cell
            px = x - dx1
            py = y - dy1
            if 0 <= px < w and 0 <= py < h and grid[py][px] != 'T':
                next_visited[py][px] = True
            
            # Case 2: robot tried to move forward but failed (tree or out of bounds)
            fx = x + dx1
            fy = y + dy1
            if not (0 <= fx < w and 0 <= fy < h) or (grid[fy][fx] == 'T'):
                next_visited[y][x] = True
    
    visited = next_visited
 
result = 0
for y in range(h):
    for x in range(w):
        if visited[y][x] and grid[y][x] != 'T':
            result += 1
 
print(result)
