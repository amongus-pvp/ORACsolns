# https://orac2.info/problem/158/
N = int(input())
fences = []
for i in range(N):
    fences.append(int(input()))
min_pre = [0] * N
min_pre[0] = 1000000
for i in range(1, N):
    min_pre[i] = min(fences[i - 1], min_pre[i - 1])
min_post = [0] * N
min_post[N - 1] = 1000000
for i in range(N - 2, -1, -1):
    min_post[i] = min(fences[i + 1], min_post[i + 1])
ans = max((fences[i] - min_pre[i]) + (fences[i] - min_post[i]) for i in range(1, N - 1) if min_pre[i] < fences[i] > min_post[i])
print(ans)
