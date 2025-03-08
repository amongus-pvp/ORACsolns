# https://orac2.info/problem/240/
def min_fences_to_remove(n, widths):
    left, right = 0, n - 1
    left_sum, right_sum = widths[left], widths[right]
    fences_removed = 0
 
    while left < right:
        if left_sum == right_sum:
            # Move both pointers inward
            left += 1
            right -= 1
            if left < right:  # Only update sums if pointers haven’t crossed
                left_sum = widths[left]
                right_sum = widths[right]
        elif left_sum < right_sum:
            # Merge left side
            left += 1
            left_sum += widths[left]
            fences_removed += 1
        else:
            # Merge right side
            right -= 1
            right_sum += widths[right]
            fences_removed += 1
 
    return fences_removed


n = int(input())
widths = list(map(int, input().split()))
print(min_fences_to_remove(n, widths))