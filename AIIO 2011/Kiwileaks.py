# https://orac2.info/problem/248/
from math import gcd # too lazy to write the freaky gdc definition 
from functools import reduce
import sys

sys.stdin = open("leakin.txt", "r")
sys.stdout = open("leakout.txt", "w")

def lcm(a, b):
    return a * b // gcd(a, b)

N, K = map(int, input().split())
mapping = list(map(int, input().split()))
recipe = list(map(int, input().split()))

# Convert mapping to 1-indexed for convenience
mapping = [0] + mapping  # index 0 unused

# Compute cycle lengths
visited = [False] * (N + 1)
cycle_length = [0] * (N + 1)

for i in range(1, N + 1):
    if not visited[i]:
        current = i
        cycle = []
        while not visited[current]:
            visited[current] = True
            cycle.append(current)
            current = mapping[current]
        length = len(cycle)
        for x in cycle:
            cycle_length[x] = length

# For each symbol in the recipe, get its cycle length
recipe_cycle_lengths = [cycle_length[sym] for sym in recipe]

# Compute LCM of these lengths
total_lcm = reduce(lcm, recipe_cycle_lengths)

print(total_lcm)
