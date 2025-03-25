# https://orac2.info/problem/268/
def max_abducted_humans(N, W, positions):
    left = 0
    max_count = 0
 
    for right in range(N):
        # Move the left pointer if the window exceeds W
        while positions[right] - positions[left] >= W:
            left += 1
        # Update the maximum count
        max_count = max(max_count, right - left + 1)
 
    return max_count
 
N, W = map(int, input().split())
positions = [int(input()) for _ in range(N)]
 
# Compute the result
result = max_abducted_humans(N, W, positions)
 
print(result)
