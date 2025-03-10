# https://orac2.info/problem/1466/
n, m = map(int, input().split())
x = list(map(int, input().split()))
 
change = [0] * n
low = [0] * n
steps = []
 
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    steps.append((a, b))
    change[a] -= 1
    change[b] += 1
    low[a] = min(low[a], change[a])
 
newx = [0] * n
flag = False
 
for i in range(n):
    newx[i] = x[i] + low[i]
    if newx[i] < 0:
        flag = True
 
if flag:
    ans = 0
    for a, b in steps:
        x[a] -= 1
        x[b] += 1
        if x[a] < 0:
            break
        ans += 1
    print(ans)
    exit()
 
# Check for infinite cycles
forever = all(c == 0 for c in change)
 
if forever:
    print("FOREVER")
    exit()
 
# Finding the most cycles that can be done
mostcycles = 10000000
if flag:
    mostcycles = 0
else:
    for i in range(n):
        if change[i] < 0:
            chng = -change[i]
            mostcycles = min(mostcycles, newx[i] // chng)
    mostcycles += 1
 
finalx = [0] * n
for i in range(n):
    finalx[i] = x[i] + mostcycles * change[i]
 
ans = mostcycles * m
 
for a, b in steps:
    finalx[a] -= 1
    finalx[b] += 1
    if finalx[a] < 0:
        break
    ans += 1
 
print(ans)
