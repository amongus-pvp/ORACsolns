# https://orac2.info/problem/211/
N, K = [int(s) for s in input().split()]
ans = {}
for i in range(N):
    X, T = [int(s) for s in input().split()]
    s = T - X * K
    if s not in ans:
        ans[s] = 0
    ans[s] += 1
print(max(ans.values()))
