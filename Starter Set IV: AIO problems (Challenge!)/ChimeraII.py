N = int(input())
top = list(input())
bottom = list(input())
target = list(input())
 
switches = 0
status = True
# js put the fries in the bag lil bro
# translating ts from C++ was a pain in the ass :pray:
state = 3
 
for i in range(N):
    if state == 1:
        if top[i] == target[i]:
            state = 1
        elif bottom[i] == target[i]:
            switches += 1
            state = 2
        else:
            status = False
            break
    elif state == 2:
        if bottom[i] == target[i]:
            state = 2
        elif top[i] == target[i]:
            switches += 1
            state = 1
        else:
            status = False
            break
    elif state == 3:
        if top[i] == target[i] and bottom[i] == target[i]:
            state = 3
        elif bottom[i] == target[i]:
            state = 2
        elif top[i] == target[i]:
            state = 1
        else:
            status = False
            break
 
if status == True:
    print('SUCCESS')
    print(switches)
else:
    print('PLAN FOILED')