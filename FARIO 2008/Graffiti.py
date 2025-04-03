# https://orac2.info/problem/302/
import sys

def main():
    sys.setrecursionlimit(1 << 25)
    n = int(sys.stdin.readline())
    
    # Initialize the array (1-based indexing)
    a = [[0] * (n + 1) for _ in range(4)]  # a[1], a[2], a[3] will be used
    
    for i in range(1, n + 1):
        values = list(map(int, sys.stdin.readline().split()))
        a[1][i], a[2][i], a[3][i] = values[0], values[1], values[2]
    
    # Initialize DP table with negative infinity
    dp = [[-float('inf')] * 2 for _ in range(n + 1)]
    dp[1][0] = 0  # Base case
    
    for i in range(1, n):
        # Update dp[i+1][0] by taking the max of previous states
        dp[i+1][0] = max(dp[i+1][0], dp[i][0])
        dp[i+1][0] = max(dp[i+1][0], dp[i][1])
        
        # Update dp[i+1][1] with the two possible transitions
        transition1 = dp[i][0] + a[1][i] + a[1][i+1] + a[2][i] + a[2][i+1]
        transition2 = dp[i][0] + a[2][i] + a[2][i+1] + a[3][i] + a[3][i+1]
        dp[i+1][1] = max(dp[i+1][1], transition1, transition2)
    
    print(max(dp[n][0], dp[n][1]))

if __name__ == "__main__":
    main()
