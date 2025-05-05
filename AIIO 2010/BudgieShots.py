# https://orac2.info/problem/188/
import sys
sys.stdin = open("shotin.txt", "r")
sys.stdout = open("shotout.txt", "w")

N = int(input())
budgies = []
for _ in range(N):
    start, end = map(int, input().split())
    budgies.append((start, end))

# Sort intervals by end time
budgies.sort(key=lambda x: x[1])

shots = 0
last_shot = -1

for start, end in budgies:
    if last_shot < start:
        # Need new shot
        shots += 1
        last_shot = end

print(shots)
