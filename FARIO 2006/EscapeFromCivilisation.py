# https://orac2.info/problem/206/
import sys
from collections import deque

def main():
    w, h = map(int, sys.stdin.readline().split())
    grid = []
    for _ in range(h):
        row = list(map(int, sys.stdin.readline().split()))
        grid.append(row)
    
    # Initialize distance matrix with infinity
    dist = [[float('inf')] * (w + 1) for _ in range(h + 1)]
    q = deque()
    
    # Find all starting points (cells with value 1)
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if grid[i-1][j-1] == 1:
                dist[i][j] = 0
                q.append((i, j))
    
    # Directions: up, down, left, right (no diagonals)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Check boundaries
            if 1 <= nx <= h and 1 <= ny <= w:
                if dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    
    max_dist = 0
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if dist[i][j] > max_dist:
                max_dist = dist[i][j]
    
    print(max_dist)

if __name__ == "__main__":
    main()
