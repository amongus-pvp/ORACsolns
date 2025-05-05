# https://orac2.info/problem/312/
N, L = map(int, input().split())
intervals = [tuple(map(int, input().split())) for _ in range(N)]

max_len = 0
left = 0
inter_left = 0
inter_right = L

for right in range(N):
    inter_left = max(inter_left, intervals[right][0])
    inter_right = min(inter_right, intervals[right][1])

    # Shrink window if intersection is invalid
    while inter_right - inter_left < 1 and left <= right:
        # Remove left interval
        if intervals[left][0] == inter_left:
            inter_left = intervals[left + 1][0] if left + 1 <= right else 0
            for i in range(left + 2, right + 1):
                inter_left = max(inter_left, intervals[i][0])
        if intervals[left][1] == inter_right:
            inter_right = intervals[left + 1][1] if left + 1 <= right else L
            for i in range(left + 2, right + 1):
                inter_right = min(inter_right, intervals[i][1])
        left += 1

    if inter_right - inter_left >= 1:
        max_len = max(max_len, right - left + 1)

print(max_len)
