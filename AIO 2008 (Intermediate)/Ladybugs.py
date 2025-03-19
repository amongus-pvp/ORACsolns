# https://orac2.info/problem/309/
N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
print(max(arr)-min(arr) + 1)
