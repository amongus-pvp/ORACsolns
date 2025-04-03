# https://orac2.info/problem/95/
import sys
 
def solve():
    input = sys.stdin.read().split()
    ptr = 0
    X, W = map(int, input[ptr:ptr+2])
    ptr +=2
    
    audio = []
    for _ in range(X):
        audio.append(int(input[ptr]))
        ptr +=1
    
    warpers = []
    for _ in range(W):
        warpers.append(int(input[ptr]))
        ptr +=1
    
    # Compute prefix sum
    prefix = [0]*(X+1)
    for i in range(1, X+1):
        prefix[i] = prefix[i-1] + audio[i-1]
    
    # For each possible y in warpers, find the max (prefix[i] - prefix[i-y]) for i >=y
    max_sums = []
    for y in warpers:
        max_sum = -float('inf')
        for i in range(y, X+1):
            current_sum = prefix[i] - prefix[i-y]
            if current_sum > max_sum:
                max_sum = current_sum
        if max_sum > 0:
            max_sums.append(max_sum)
    
    # We should pick the top k max_sums where sum is positive, sorted in descending order
    max_sums.sort(reverse=True)
    total = prefix[X]  # initial sum without any warps
    for s in max_sums:
        if s >0:
            total += s
    print(total)
 
solve()
