# https://orac2.info/problem/119/
import sys
sys.setrecursionlimit(10 ** 7)
sys.stdin = open("snurgle.in", "r")
sys.stdout = open("snurgle.out", "w")

MAXN = 100005 # lol doing the cf template ah
children = [[] for _ in range(MAXN)]
dp = [[0, 0] for _ in range(MAXN)]  # dp[i][0] = not taken, dp[i][1] = taken

def dfs(node):
    dp[node][0] = 0
    dp[node][1] = 1  # take the current node

    for child in children[node]:
        dfs(child)
        dp[node][0] += max(dp[child][0], dp[child][1])
        dp[node][1] += dp[child][0]

n = int(input())

if n == 1:
    print(1)
    exit()

for i in range(1, n):
    j = int(input())
    children[j].append(i)

dfs(n)

print(max(dp[n][0], dp[n][1]))
