# https://orac2.info/problem/283/
n = int(input())
left = 0
right = 9999999999
for i in range(n):
    x, w = map(int, input().split())
    if x < left:
        left = x
        right = x + w
        ans = i
    elif x + w > left and x < right:
        left = x
        right = x + w
        ans = i
print(ans + 1)
