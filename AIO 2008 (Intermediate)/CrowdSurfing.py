# https://orac2.info/problem/288/
R, C = map(int, input().split())
crowd = []
sinkholes = []
for i in range(R):
    line = list(input())
    crowd.append(line)
    for j in range(C):
        if line[j] == '*':
            sinkholes.append((i, j)) # keep track of where all the sinkholes are
 
def backtrack(s : tuple[int, int]) -> None: # we backtrack from a sinkhole and count how many ways we can get to one
    global answer # keeping answer as a global variable
    x = s[0]
    y = s[1]
    canLeft = y > 0 # is there a valid square to the left of us?
    canUp = x > 0 # is there a valid square above us?
    if canLeft:
        if crowd[x][y - 1] == ">": # is the one to our left pointing to us? if so then thats another way to get to a sinkhole
            answer += 1
            backtrack((x, y-1))
    if canUp:
        if crowd[x-1][y] == "v":
            answer += 1
            backtrack((x-1, y))
 
total = 0
for i in sinkholes:
    answer = 0
    backtrack(i)
    total += answer
 
print(total + len(sinkholes)) # we have to add every single sinkhole as a bad square as well
