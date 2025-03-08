# https://orac2.info/problem/1102/
N, K = map(int, input().split())
d = []

for i in range(N):
    d.append(int(input()))
 
d.sort()
 
last = -1000000000
ans = 0
 
for x in d:
    if x - last >= K:
        last = x
        ans += 1

print(ans)