# https://orac2.info/problem/101/
def solve():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    S = int(input[ptr])
    ptr += 1
    stacks = list(map(int, input[ptr:ptr + S]))
    
    left = 0
    right = S - 1
    left_sum = 0
    right_sum = 0
    count = 0
    
    while left < right:
        left_sum += stacks[left]
        right_sum += stacks[right]
        
        while left_sum != right_sum and left < right:
            if left_sum < right_sum:
                left += 1
                left_sum += stacks[left]
                count += 1
            else:
                right -= 1
                right_sum += stacks[right]
                count += 1
        
        left += 1
        right -= 1
        left_sum = 0
        right_sum = 0
    
    print(count)
 
solve()
