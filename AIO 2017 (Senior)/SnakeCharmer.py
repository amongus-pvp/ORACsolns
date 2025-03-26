# https://orac2.info/problem/122/
facingdir = "up"
currentposition = [0, 0]
goalposition = list(map(int, input().split()))
moveslist = []

def nextbestmove(currentpos, goalpos, facing):
    if facing == "up":
        if goalpos[0] - currentpos[0] < 0:
            facing = "left"
            return ["L", "L"]
        elif goalpos[0] - currentpos[0] > 0:
            facing = "right"
            return ["R", "R"]
        elif goalpos[0] - currentpos[0] == 0:
            facing = "right"
            return ["R", "R"]
    elif facing == "down":
        if goalpos[0] - currentpos[0] < 0:
            facing = "left"
            return ["R", "L"]
        elif goalpos[0] - currentpos[0] > 0:
            facing = "right"
            return ["L", "R"]
        elif goalpos[0] - currentpos[0] == 0:
            facing = "left"
            return ["R", "L"]
    elif facing == "right":
        if goalpos[1] - currentpos[1] < 0:
            facing = "down"
            return ["R", "D"]
        elif goalpos[1] - currentpos[1] > 0:
            facing = "up"
            return ["L", "U"]
        elif goalpos[1] - currentpos[1] == 0:
            facing = "up"
            return ["L", "U"]
    elif facing == "left":
        if goalpos[1] - currentpos[1] < 0:
            facing = "down"
            return ["L", "D"]
        elif goalpos[1] - currentpos[1] > 0:
            facing = "up"
            return ["R", "U"]
        elif goalpos[1] - currentpos[1] == 0:
            facing = "up"
            return ["R", "U"]

while currentposition[0] != goalposition[0] or currentposition[1] != goalposition[1]:
    newmove = nextbestmove(currentposition, goalposition, facingdir)
    moveslist.append(newmove[0])
    if newmove[1] == "U":
        facingdir = "up"
        currentposition[1] += 1
    elif newmove[1] == "D":
        facingdir = "down"
        currentposition[1] -= 1
    elif newmove[1] == "L":
        facingdir = "left"
        currentposition[0] -= 1
    elif newmove[1] == "R":
        facingdir = "right"
        currentposition[0] += 1

print("".join(moveslist))
