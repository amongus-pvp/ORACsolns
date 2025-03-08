# https://orac2.info/problem/57/
from collections import deque
 
R, C, K = map(int, input().split())
grid = [list(input()) for _ in range(R)]
 
# Directions for N, E, S, W
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
 
# Find oil rig position
queue = deque()
oil_rig_pos = None
 
for r in range(R):
    for c in range(C):
        if grid[r][c] == '$':
            oil_rig_pos = (r, c)  # Save position
            queue.append((r, c, 0))  # (row, col, days)
 
# BFS simulation
while queue:
    r, c, days = queue.popleft()
 
    # Stop if we reach the Kth day
    if days == K:
        break
 
    # Spread to adjacent cells
    for dr, dc in DIRECTIONS:
        nr, nc = r + dr, c + dc
 
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == '.':
            grid[nr][nc] = '*'  # Mark as oil
            queue.append((nr, nc, days + 1))  # Add to queue for next day
 
# Restore the original '$' position
if oil_rig_pos:
    r, c = oil_rig_pos
    grid[r][c] = '$'
 
# Print the final grid
for row in grid:
    print("".join(row))