# https://orac2.info/problem/33/
n = int(input())
v = [int(input()) for _ in range(n)]

if n == 1:
    print(1)
else:
    left = [{} for _ in range(n)]
    ans = 1
    
    for i in range(1, n):
        for j in range(i):
            diff = v[i] - v[j]
            left[i][diff] = left[j].get(diff, 1) + 1
            ans = max(ans, left[i][diff])
    
    print(ans)
