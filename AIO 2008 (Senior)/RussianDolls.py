# https://orac2.info/problem/319/
import bisect
n = int(input())
v = []
for i in range(n):
    v.append(int(input()))
 
s = []
for i in range(n):
    pos = bisect.bisect_right(s, v[i])
    if pos == len(s):
        s.append(v[i])
    else:
        s[pos] = v[i]
print(len(s))

# short solution but kinda hard
# i might comment this later so my soln makes some sense but eh we shall see
