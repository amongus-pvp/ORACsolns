# https://orac2.info/problem/1147/
N = int(input())
d = list(map(int, input().split()))
 
l = 0
r = 0
 
# we're going on the range l -> r inclusive
 
m = 1 # best length of consectuvie days
# should be O(N) since we constantly increasing right pointer and dragging left along with it. Only time right stops is when sequence is no longer increasing
 
while r < N - 1:
    if l == r:
        if d[r+1] == d[l] + 1:
            r += 1 # sequence is increasing yay!
            m = max(m, r - l + 1)
        else:
            r += 1
            l += 1 # sequence aint increasing lil bro
    elif l != r:
        if d[r+1] == d[r] + 1:
            r += 1 # you already know what im about to say
            m = max(m, r - l + 1)
        else:
            r += 1
            l = r # womp womp sequence wasnt good enough
print(m)
