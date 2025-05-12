# https://orac2.info/problem/284/
import sys
sys.stdin = open("cats.in", "r")
sys.stdout = open("cats.out", "w")

n = int(input())
k = int(input())


heads = []
tails = []
for i in range(n):
    heads.append(int(input()))
for i in range(n):
    tails.append(int(input()))
# Binary search for the answer
low = 2
high = 2 * 10**6
ans = -1

while low <= high:
    mid = (low + high) // 2
    
    # Count how many cat sizes >= mid
    count = 0
    j = n - 1
    for i in range(n):
        while j >= 0 and heads[i] + tails[j] < mid:
            j -= 1
        count += (j + 1)
    
    if count >= k:
        ans = mid      # mid is a valid answer
        low = mid + 1  # try to find a bigger one
    else:
        high = mid - 1  # too few, try smaller

print(ans)
