# https://orac2.info/problem/267/
def solve():
    import sys
    input = sys.stdin.read().splitlines()
    r, c = map(int, input[0].split())
    grid = input[1:r+1]
    
    max_length = 0
    best_coords = None
    
    # Check horizontal sequences
    for i in range(r):
        current_length = 0
        start_j = 0
        for j in range(c):
            if grid[i][j] == '.':
                current_length += 1
                if current_length > max_length:
                    max_length = current_length
                    best_coords = (i+1, j - current_length + 2, i+1, j+1)
            else:
                current_length = 0
        # Check if the entire row is residential
        if current_length > max_length:
            max_length = current_length
            best_coords = (i+1, c - current_length + 1, i+1, c)
    
    # Check vertical sequences
    for j in range(c):
        current_length = 0
        start_i = 0
        for i in range(r):
            if grid[i][j] == '.':
                current_length += 1
                if current_length > max_length:
                    max_length = current_length
                    best_coords = (i - current_length + 2, j+1, i+1, j+1)
            else:
                current_length = 0
        # Check if the entire column is residential
        if current_length > max_length:
            max_length = current_length
            best_coords = (r - current_length + 1, j+1, r, j+1)
    
    print(' '.join(map(str, best_coords)))

solve()
