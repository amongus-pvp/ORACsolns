# https://orac2.info/problem/1532/
N, K, X = map(int, input().split())
H = list(map(int, input().split()))
seen = set() # keep track of every value before the current one that we have seen, that is far away
 
for i in range(K, N):
    seen.add(H[i - K])
    need1 = H[i] - X
    need2 = H[i] + X
    if need1 in seen or need2 in seen:
        print("YES")
        exit()
print("NO")
