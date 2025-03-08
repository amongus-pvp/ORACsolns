# https://orac2.info/problem/1098/
x = input() # js skipping the first line since we dont need it
x = input()
 
v = 0
h = 0
for i in x:
    if i == 'N':
        v+=1
    elif i == 'S':
        v-=1
    elif i == 'E':
        h+=1
    elif i == 'W':
        h-=1


print(abs(v)+abs(h))