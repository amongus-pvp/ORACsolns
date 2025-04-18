# https://orac2.info/problem/259/
n, h = map(int, input().split())
boxes = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0] * (h + 1)
dp[0] = 1

for a, b in boxes:
    temp = []
    for j in range(h, -1, -1):
        if j - a >= 0 and dp[j - a] == 1:
            temp.append(j)
        if j - b >= 0 and dp[j - b] == 1:
            temp.append(j)
    for k in temp:
        dp[k] = 1

for i in range(h, -1, -1):
    if dp[i] == 1:
        print(i)
        exit()
