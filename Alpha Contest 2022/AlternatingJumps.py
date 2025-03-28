# https://orac2.info/problem/1141/
def main():
    import sys
    input = sys.stdin.read().split()
    
    idx = 0
    n = int(input[idx])
    idx += 1
    segs = []
    for _ in range(n):
        segs.append(int(input[idx]))
        idx += 1
    
    reds = []
    blues = []
    for i in range(n):
        if segs[i] == 1:
            reds.append(i)
        else:
            blues.append(i)
    
    bways = 0
    rways = 0
    dp = [0] * n
    
    if segs[0] == 1:
        dp[0] = 1
        bways = 1
    else:
        dp[0] = 1
        rways = 1
    
    MOD = 1000000007
    
    for i in range(1, n):
        if segs[i] == 1:
            dp[i] = rways % MOD
            bways = (bways + rways) % MOD
        else:
            dp[i] = bways % MOD
            rways = (rways + bways) % MOD
    
    print(dp[n-1] % MOD)

if __name__ == "__main__":
    main()
