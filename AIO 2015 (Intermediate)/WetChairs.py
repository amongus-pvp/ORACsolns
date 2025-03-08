# https://orac2.info/problem/244/
C, N, K = [int(s) for s in input().split()]
chairs = [s for s in input()]
ans = C
right = 0
for left in range(C):
    if left == 0:
        num = 0
        dry = 0
    else:
        num -= 1
        if chairs[left - 1] == 'd':
            dry -= 1
    if num >= N and dry >= N - K:
        ans = min(ans, num)
    else:
        for i in range(right, C):
            right += 1
            num = right - left
            if chairs[i] == 'd':
                dry += 1
            if num >= N and dry >= N - K:
                ans = min(ans, num)
                break
print(ans)