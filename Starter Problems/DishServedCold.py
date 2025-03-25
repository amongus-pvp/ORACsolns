# https://orac2.info/problem/328/
import statistics
import math

n = int(input())

for i in range(n):
  arr.append(int(input()))

print(str(math.floor(min(arr))) + " " + str(math.floor(max(arr))) + " " + str(math.floor(statistics.mean(arr))))