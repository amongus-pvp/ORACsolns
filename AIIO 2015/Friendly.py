# https://orac2.info/problem/219/
# dynamic programming :D
class Offer:
    def __init__(self, rtype, gtype, chocs):
        self.rtype = rtype
        self.gtype = gtype
        self.chocs = chocs

N, K = map(int, input().split())
offers = []
for _ in range(N):
    A, B, C = map(int, input().split())
    offers.append(Offer(A, B, C))

dp = [0 for i in range(K + 1)]

for i in range(N - 1, -1, -1):
    a, b, c = offers[i].rtype, offers[i].gtype, offers[i].chocs
    dp[a] = max(dp[a], dp[b] + c)

maxchocs = max(dp)

cnt = 0

for i in range(1, K + 1):
    if dp[i] == maxchocs:
        cnt += 1


print(maxchocs)
print(cnt)
