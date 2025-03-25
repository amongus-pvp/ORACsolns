# https://orac2.info/problem/300/
N, S, K = map(int, input().split())
# we will update S with every instruction
for i in range(K):
    a, b = map(int, input().split())
    if a == S: # the cup being moved is the cup that contains the ball
        S = b
    elif b == S: # the cup being moved is moving to the cup that contains the ball
        if a > S:
            S += 1
        else:
            S -= 1
    elif a > S: # the starting cup is on the right of our winning cup
        if b > S:
            continue
        else: # finishing cup is less than starting cup, we go B <---S---- A
            S += 1
    elif a < S: # starting cup is on the left
        if b > S: # we go over our winning cup
            S -= 1
        else:
            continue
print(S)
