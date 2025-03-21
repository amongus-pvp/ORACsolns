# https://orac2.info/problem/172/
from collections import deque
 
def bfs(grid, h, w, i, j, done):
    q = deque([(i, j)])
    done[i][j] = True
    coords = []
    vert = {}
    hor = {}
 
    while q:
        x, y = q.popleft()
        if not ((x > 0 and grid[x-1][y] == 'X' and x < h-1 and grid[x+1][y] == 'X') or 
                (y > 0 and grid[x][y-1] == 'X' and y < w-1 and grid[x][y+1] == 'X')):
            vert.setdefault(y, []).append(x)
            hor.setdefault(x, []).append(y)
 
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 'X' and not done[nx][ny]:
                q.append((nx, ny))
                done[nx][ny] = True
 
    for y, v in vert.items():
        v.sort()
        coords.extend([(v[0], y), (v[-1], y)])
    for x, v in hor.items():
        v.sort()
        coords.extend([(x, v[0]), (x, v[-1])])
 
    return coords
 
def main():
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    done = [[False] * w for _ in range(h)]
    ans = 0
 
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'X' and not done[i][j]:
                coords = bfs(grid, h, w, i, j, done)
                mx = max(abs(x1-x2) + abs(y1-y2) for x1, y1 in coords for x2, y2 in coords)
                ans = max(ans, mx)
 
    print(ans)
 
if __name__ == "__main__":
    main()
