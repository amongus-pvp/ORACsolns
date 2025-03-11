# https://orac2.info/problem/210/
Finished judging!

Source Code
from bisect import bisect_left
 
 
n, k, q = map(int, input().split())
p = list(map(int, input().split()))
d = list(map(int, input().split()))
 
b = {}
b[p[0]] = p[k - 1] - p[0]
 
for i in range(1, n):
    if k + i <= len(p):
        b[p[i]] = min(p[k - 1 + i] - p[i], p[i] - p[i - 1] + b[p[i - 1]])
    else:
        b[p[i]] = p[i] - p[i - 1] + b[p[i - 1]]
 
p.reverse()
f = {}
f[p[0]] = p[0] - p[k - 1]
 
for i in range(1, n):
    if k + i - 1 < len(p):
        f[p[i]] = min(-(p[k - 1 + i] - p[i]), -(p[i] - p[i - 1] - f[p[i - 1]]))
    else:
        f[p[i]] = -(p[i] - p[i - 1] - f[p[i - 1]])
 
final = {}
for i in range(n):
    final[p[i]] = min(f[p[i]], b[p[i]])
 
p.reverse()
ans = []
 
for drop in d:
    idx = bisect_left(p, drop)
    if idx >= len(p):
        idx = len(p) - 1
    if idx != 0:
        lower = idx - 1
        if p[idx] - drop + final[p[idx]] < drop - p[lower] + final[p[lower]]:
            close = p[idx]
        else:
            close = p[lower]
    else:
        close = p[idx]
    ans.append(final[close] + abs(drop - close))
 
print(" ".join(map(str, ans)))
