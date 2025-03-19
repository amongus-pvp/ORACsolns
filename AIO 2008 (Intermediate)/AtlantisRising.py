# https://orac2.info/problem/149/
N = int(input())
 
shape = []
 
for i in range(N):
    shape.append(int(input()))
isBigger = [None] * (N-1)
isBigger.append(False) # final value has nothing to the right to be bigger than it
isBigger1 = [None]*(N)
isBigger[0] = False # this time for left
runningmax = shape[-1]
 
for i in range(N - 2, -1, -1): # right to left traversal
    if shape[i] < runningmax:
        isBigger[i] = True
    else:
        isBigger[i] = False
        runningmax = shape[i]
 
runningmax = shape[0]
for i in range(1, N): # left to right traversal
    if shape[i] < runningmax:
        isBigger1[i] = True
    else:
        isBigger1[i] = False
        runningmax = shape[i]
 
 
answer = 0
for i in range(1, N-1):
    left = isBigger1[i]
    cur = shape[i]
    right = isBigger[i] # ts is a bool
 
    # trying to avoid recalculations, doesnt matter that much but good practise
    if left and right:
        answer += 1
 
print(answer)
