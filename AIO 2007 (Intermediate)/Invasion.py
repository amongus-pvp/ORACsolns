# https://orac2.info/problem/257/
from collections import deque
 
# Directions for exploring neighbours: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
 
def bfs(grid, visited, r, c, nation):
    """ Use BFS to label the region of the given nation starting from (r, c). """
    rows, cols = len(grid), len(grid[0])
    queue = deque([(r, c)])
    visited[r][c] = nation  # Mark the nation
    region_cells = [(r, c)]
    
    while queue:
        x, y = queue.popleft()
        # Explore all 4 possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and visited[nx][ny] == 0 and grid[nx][ny] == grid[r][c]:
                visited[nx][ny] = nation
                queue.append((nx, ny))
                region_cells.append((nx, ny))
    
    return region_cells
 
def solve():
    # Read the input
    r, c = map(int, input().split())
    grid = [input().strip() for _ in range(r)]
    
    visited = [[0] * c for _ in range(r)]  # To track which cell belongs to which nation
    nation_count = 0
    nation_cells = {}  # Will store the cells for each nation
    
    # Step 1: Label each nation with a unique ID and store their cells
    for i in range(r):
        for j in range(c):
            if visited[i][j] == 0:
                nation_count += 1
                nation_cells[nation_count] = bfs(grid, visited, i, j, nation_count)
    
    # Step 2: Calculate the number of neighbours for each nation
    neighbour_count = {nation: set() for nation in range(1, nation_count + 1)}
    
    for nation_id, cells in nation_cells.items():
        for x, y in cells:
            # For each cell in the nation, check its 4 neighbours
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c:
                    neighbour_nation = visited[nx][ny]
                    if neighbour_nation != nation_id:
                        neighbour_count[nation_id].add(neighbour_nation)
    
    # Step 3: Find the nation with the maximum number of neighbours
    max_neighbours = max(len(neighbours) for neighbours in neighbour_count.values())
    
    # Output the result
    print(max_neighbours)
 
solve()
