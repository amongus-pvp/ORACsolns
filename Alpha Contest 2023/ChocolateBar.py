# https://orac2.info/problem/1222/
N = int(input())
l = list(map(int, input().split()))
prefix_sum = [l[0]] # prefix sum [-1] returns the sum of the whole list
# first loop is to get the prefix sum
diff = 2**32
for i in range(1, N):
    prefix_sum.append(prefix_sum[i-1] + l[i])
total = prefix_sum[-1]
for i in range(N - 1):
    x = total - prefix_sum[i]
    diff = min(diff, abs(x-prefix_sum[i]))
print(diff)
