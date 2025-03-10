# https://orac2.info/problem/1298/
N, M = map(int, input().split())
V = list(map(int, input().split()))
P = list(map(int, input().split()))
 
voter_order = sorted(range(M), key=lambda x: -P[x])
cand_voters = [[] for _ in range(N)]
order = [0] * M
 
for i, v in enumerate(voter_order):
    order[v] = M - i - 1
 
used = [0] * M
forced = 0
forced_cnt = 0
other = 0
v1 = 0
ans = 9e9
 
for i in voter_order:
    if V[i] == 1:
        v1 += 1
        used[i] = 1
    else:
        other += P[i]
        cand_voters[V[i] - 1].append(i)
 
other_cnt = M - v1
cand_voters.sort(key=len, reverse=True)
voter_order.reverse()
 
for x in range(M, max(0, v1 - 1), -1):
    c_idx = 0
    while c_idx < N - 1 and len(cand_voters[c_idx]) >= x:
        voter = cand_voters[c_idx].pop()
        forced += P[voter]
        forced_cnt += 1
        used[voter] = True
        c_idx += 1
        if order[voter] < len(voter_order):
            other_cnt -= 1
            other -= P[voter]
    while other_cnt > 0 and forced_cnt + v1 + other_cnt > x:
        voter = voter_order.pop()
        if not used[voter]:
            other_cnt -= 1
            other -= P[voter]
    ans = min(ans, forced + other)
 
print(ans)