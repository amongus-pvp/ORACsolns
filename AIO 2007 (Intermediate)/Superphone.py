# https://orac2.info/problem/6/
n = int(input())
x = [] # array of arrays
for i in range(n - 1):
    x.append(list(map(int, input().split())))
x.append([-999, int(input()), -999]) # quirky!
d = [2**32 for i in range(2*n)]
d[0] = 0
d[1] = x[0][1] # from here we work our way up
for i in range(0, n - 1): # going through the edges again
    #ok so this solution is kind of quirky what i ended up doing was simplifying it down to having to check a window of 4 nodes at a time
    d[2*(i+1)] = min(d[2*i] + x[i][0] + x[i+1][1], d[2*i+1] + x[i][2])
    d[2*(i+1) + 1] = min(d[2*i] + x[i][0], d[2*i+1] + x[i][2] + x[i+1][1])
print(d[-1])
