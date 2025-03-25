# https://orac2.info/problem/90/
# thanks to SebZanardo for this soln sorry i couldnt be bothered to refactor code
corners = []
for i in range(8):
    corners.append(tuple(map(int, input().split())))
 
# Step One: Find minimum and maximum
min_x = corners[0][0]
max_x = min_x
min_y = corners[0][1]
max_y = min_y
for i in range(1, 8):
    x, y = corners[i]
    if x < min_x:
        min_x = x
    if x > max_x:
        max_x = x
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y
 
# Step Two: Find corners that make up the missing piece
inner = []
for c in corners:
    x, y = c
    if x == min_x and y == min_y:
        continue
    if x == min_x and y == max_y:
        continue
    if x == max_x and y == min_y:
        continue
    if x == max_x and y == max_y:
        continue
    inner.append(c)
 
# Step Three: Find direction
for c in inner:
    x, y = c
    if x == min_x:
        direction = "W"
        break
    elif x == max_x:
        direction = "E"
        break
    elif y == max_y:
        direction = "N"
        break
    elif y == min_y:
        direction = "S"
        break
 
print(direction)
