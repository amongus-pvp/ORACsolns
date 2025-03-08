n = int(input().strip())
cmds = list(input().strip())
maxleft = 0
maxright = 0
pos = 0
for i in range(n):
    if cmds[i] == 'R':
        if maxright == pos:
            maxright += 1
        pos += 1
    elif cmds[i] == 'L':
        if maxleft == pos:
            maxleft -= 1
        pos -= 1
    elif cmds[i] == 'T':
        pos = 0
 
print(maxright + abs(maxleft) + 1)