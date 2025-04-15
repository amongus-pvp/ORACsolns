# https://orac2.info/problem/58/
from collections import defaultdict
import sys
 
def solve():
    sys.stdin = open("nomin.txt", "r")
    sys.stdout = open("nomout.txt", "w")
    
    N = int(input())
    s = []
    for i in range(N):
        s.append(int(input()))
    
    prefix = 0
    prefix_map = defaultdict(int)
    prefix_map[0] = 0  # Initialize with prefix sum 0 at index 0
    
    max_total = 0
    
    for i in range(1, N + 1):
        prefix += s[i-1]
        # Store the first occurrence of each prefix sum
        if prefix not in prefix_map:
            prefix_map[prefix] = i
    
    # Now, iterate through the prefix sums to find the maximum sum where prefix[B] == prefix[B + J] - prefix[B]
    # Which implies prefix[B + J] = 2 * prefix[B]
    prefix = 0
    for B in range(1, N):
        prefix += s[B-1]
        target = 2 * prefix
        if target in prefix_map:
            J = prefix_map[target] - B
            if J > 0 and B + J <= N:
                if prefix > max_total:
                    max_total = prefix
    print(max_total)  
 
solve()
