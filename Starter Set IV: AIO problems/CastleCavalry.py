N = int(input())
g = {}
for i in range(N):
    c = int(input())
    if c in g:
        g[c] += 1
    else:
        g[c] = 1
 
p = True
for i in g:
    if g[i]%i != 0:
        p = False

if p:
    print("YES")
else:
    print("NO")