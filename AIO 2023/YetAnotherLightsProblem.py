# https://orac2.info/problem/1300/
def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)
 
def ee(grid, toggles, r, c):
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '.':
                for k in range(r):
                    toggles[k][j] = (toggles[k][j] + 1) % 2
                for k in range(c):
                    toggles[i][k] = (toggles[i][k] + 1) % 2
                toggles[i][j] = (toggles[i][j] + 1) % 2
    count = sum(sum(row) for row in toggles)
    print(count)
    for i in range(r):
        for j in range(c):
            if toggles[i][j] == 1:
                print(i, j)
 
def oo(grid, toggles, r, c):
    for i in range(r - 1):
        for j in range(c - 1):
            if grid[i][j] == '.':
                toggles[i][j] ^= 1
                toggles[i + 1][j] ^= 1
                toggles[i][j + 1] ^= 1
                toggles[i + 1][j + 1] ^= 1
                grid[i][j] = '*'
                grid[i + 1][j] = '*' if grid[i + 1][j] == '.' else '.'
                grid[i][j + 1] = '*' if grid[i][j + 1] == '.' else '.'
                grid[i + 1][j + 1] = '*' if grid[i + 1][j + 1] == '.' else '.'
    
    on = sum(grid[i][c - 1] == '*' for i in range(r)) + sum(grid[r - 1][i] == '*' for i in range(c - 1))
    if on == 0 or on == r + c - 1:
        if on == 0:
            toggles[r - 1][c - 1] = 1
        count = sum(sum(row) for row in toggles)
        print(count)
        for i in range(r):
            for j in range(c):
                if toggles[i][j] == 1:
                    print(i, j)
    else:
        print(-1)
 
def oe(grid, toggles, r, c):
    for i in range(c):
        for j in range(r - 1):
            if grid[j][i] == '.':
                grid[j][i] = '*'
                grid[j + 1][i] = '*' if grid[j + 1][i] == '.' else '.'
                for k in range(c):
                    if k != i:
                        toggles[j][k] ^= 1
                        toggles[j + 1][k] ^= 1
    on = sum(grid[r - 1][i] == '*' for i in range(c))
    if on == 0 or on == c:
        if on == 0:
            for i in range(c - 1):
                toggles[r - 1][i] ^= 1
            for i in range(r - 1):
                toggles[i][c - 1] ^= 1
        count = sum(sum(row) for row in toggles)
        print(count)
        for i in range(r):
            for j in range(c):
                if toggles[i][j] == 1:
                    print(i, j)
    else:
        print(-1)
 
def eo(grid, toggles, r, c):
    for i in range(r):
        for j in range(c - 1):
            if grid[i][j] == '.':
                grid[i][j] = '*'
                grid[i][j + 1] = '*' if grid[i][j + 1] == '.' else '.'
                for k in range(r):
                    if k != i:
                        toggles[k][j] ^= 1
                        toggles[k][j + 1] ^= 1
    on = sum(grid[i][c - 1] == '*' for i in range(r))
    if on == 0 or on == r:
        if on == 0:
            for i in range(r - 1):
                toggles[i][c - 1] ^= 1
            for i in range(c - 1):
                toggles[r - 1][i] ^= 1
        count = sum(sum(row) for row in toggles)
        print(count)
        for i in range(r):
            for j in range(c):
                if toggles[i][j] == 1:
                    print(i, j)
    else:
        print(-1)
 
r, c = map(int, input().split())
grid = [list(input().strip()) for _ in range(r)]
toggles = [[0] * c for _ in range(r)]
if r % 2 == 0 and c % 2 == 0:
    ee(grid, toggles, r, c)
elif r % 2 == 1 and c % 2 == 1:
    oo(grid, toggles, r, c)
elif r % 2 == 0 and c % 2 == 1:
    eo(grid, toggles, r, c)
elif r % 2 == 1 and c % 2 == 0:
    oe(grid, toggles, r, c)