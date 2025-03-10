# https://orac2.info/problem/1461/
n, k = map(int, input().split())
dists = list(map(int, input().split()))
c = list(map(int, input().split()))
 
from collections import defaultdict
 
cnt = defaultdict(int)
cnt[c[0]] = k
ans = 0
 
for i in range(n - 1):
    need = dists[i]
    cost = 1
    while need != 0:
        use = min(need, cnt[cost])
        ans += use * cost
        cnt[cost] -= use
        cost += 1
        need -= use
 
    newcost = c[i + 1]
    less = sum(cnt[j] for j in range(1, newcost))
    newamount = k - less
    cnt[newcost] = newamount
 
    for j in range(newcost + 1, 21):
        cnt[j] = 0
 
print(ans)
