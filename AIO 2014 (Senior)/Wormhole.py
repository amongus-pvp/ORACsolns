# https://orac2.info/problem/131/
def main():
    r, c, q = map(int, input().split())
    grid = []
    row_sums = [0] * r
    col_sums = [0] * c
    
    for i in range(r):
        row = list(input())
        grid.append([1 if ch == 'B' else 0 for ch in row])
        row_sums[i] = sum(grid[i])
    
    for j in range(c):
        col_sums[j] = sum(grid[i][j] for i in range(r))
    
    def compute_result():
        row_all_diff = True
        col_all_diff = True
        row_has_diff = False
        col_has_diff = False
        row_need = 0
        col_need = 0
        
        if r == 1:
            col_has_diff = True
        if c == 1:
            row_has_diff = True
        
        for i in range(r):
            if row_sums[i] == 0 or row_sums[i] == c:
                row_all_diff = False
                row_need += 1
            else:
                row_has_diff = True
        
        for j in range(c):
            if col_sums[j] == 0 or col_sums[j] == r:
                col_all_diff = False
                col_need += 1
            else:
                col_has_diff = True
        
        if r == 1 and c == 1:
            return 0
        elif (row_all_diff and col_has_diff) or (col_all_diff and row_has_diff):
            return 0
        elif r == 1 or c == 1:
            return 1
        elif (not row_has_diff and (col_sums[0] == 1 or col_sums[0] == r - 1)) or \
             (not col_has_diff and (row_sums[0] == 1 or row_sums[0] == c - 1)):
            return 2
        elif row_has_diff != col_has_diff:
            return 1
        else:
            return min(row_need, col_need)
    
    print(compute_result())
    
    for _ in range(q):
        x, y = map(int, sys.stdin.readline().split())
        x -= 1
        y -= 1
        
        grid[x][y] = 1 - grid[x][y]
        if grid[x][y] == 0:
            row_sums[x] -= 1
            col_sums[y] -= 1
        else:
            row_sums[x] += 1
            col_sums[y] += 1
        
        print(compute_result())
 
if __name__ == "__main__":
    main()
