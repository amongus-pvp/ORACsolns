# https://orac2.info/problem/176/
import sys
 
def main():
    sys.setrecursionlimit(1000000)
    with open('labin.txt', 'r') as fin: # sorry i wrote this solution a long time ago and I am too lazy to change my file reading
        n = int(fin.readline())
        p = int(fin.readline())
        adj = [[] for _ in range(n + 1)]
        for _ in range(p):
            a, b = map(int, fin.readline().split())
            adj[b].append(a)
 
    dp = [-1] * (n + 1)
 
    def dfs(u):
        if dp[u] != -1:
            return dp[u]
        if not adj[u]:
            dp[u] = 1
            return 1
        max_len = 0
        for v in adj[u]:
            max_len = max(max_len, dfs(v))
        dp[u] = max_len + 1
        return dp[u]
 
    ans = 0
    for u in range(1, n + 1):
        ans = max(ans, dfs(u))
 
    with open('labout.txt', 'w') as fout:
        fout.write(str(ans))
 
if __name__ == '__main__':
    main()