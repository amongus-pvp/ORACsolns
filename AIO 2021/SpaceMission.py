# https://orac2.info/problem/1101/
N, F = [int(s) for s in input().split()]
C = []
for i in range(N):
    C.append(int(input()))
start = []
curr_min = 1000000000000
for i in range(N):
    if C[i] < curr_min:
        start.append([C[i], i])
        curr_min = C[i]
end = []
curr_min = 1000000000000
for i in range(N - 1, -1, -1):
    if C[i] < curr_min:
        end.append([C[i], i])
        curr_min = C[i]
end.reverse()
temp = 0
ans = -1
for val, i in end:
    while temp < len(start) and val + start[temp][0] > F:
        temp = temp + 1
    if temp < len(start) and val + start[temp][0] <= F:
        ans = max(i - start[temp][1] + 1, ans)
if ans == 1:
    ans = -1
print(ans)