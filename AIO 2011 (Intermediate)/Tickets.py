# https://orac2.info/problem/246/
def solve():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    cost1, validity1 = int(input[idx]), int(input[idx+1])
    idx += 2
    cost2, validity2 = int(input[idx]), int(input[idx+1])
    idx += 2
    D = int(input[idx])
    idx += 1
    days = []
    for _ in range(D):
        days.append(int(input[idx]))
        idx += 1
    
    # Initialize DP array
    dp = [float('inf')] * (D + 1)
    dp[0] = 0  # Base case: 0 cost to cover 0 days
    
    for i in range(1, D + 1):
        current_day = days[i-1]
        # Try to cover current_day with a ticket bought on a previous day
        # We need to find the earliest day j such that days[j-1] + validity > current_day
        # Then, the cost is dp[j-1] + cost of the ticket
        # We can use binary search to find j efficiently
        
        # For ticket type 1
        left = 0
        right = i - 1
        best_j1 = i
        while left <= right:
            mid = (left + right) // 2
            if days[mid] + validity1 > current_day:
                best_j1 = mid
                right = mid - 1
            else:
                left = mid + 1
        # The ticket covers from best_j1 to i-1
        cost_candidate1 = dp[best_j1] + cost1
        if cost_candidate1 < dp[i]:
            dp[i] = cost_candidate1
        
        # For ticket type 2
        left = 0
        right = i - 1
        best_j2 = i
        while left <= right:
            mid = (left + right) // 2
            if days[mid] + validity2 > current_day:
                best_j2 = mid
                right = mid - 1
            else:
                left = mid + 1
        cost_candidate2 = dp[best_j2] + cost2
        if cost_candidate2 < dp[i]:
            dp[i] = cost_candidate2
    
    print(dp[D])

solve()
