# https://orac2.info/problem/1215/
# one person has solved this in python "sandworm"
# i have solved in C++ but i can just not figure out how to optimise it for python so I'm using their solution here
# my soln use a BFS so pretty similar to this one
from collections import deque
 
R, C, N = map(int, input().split())
moves = input()
 
C += 3
 
x = 0
y = 0
square = { 0: 0 }
for i in range(N):
  c = moves[i]
  if c == 'N': y -= 1
  elif c == 'S' : y += 1
  elif c == 'E' : x += 1
  else: x -= 1
  square[y*C+x] = i+1
 
#print(square)
 
dirfrom = [None for i in range(N+1)]
q = deque([(y, x, 0)])
dirfrom[square[y*C+x]] = 'X'
starty = y
startx = x
 
dy = [-1,0,1,0]
dx = [0,1,0,-1]
dc = 'NESW'
 
while q:
  y, x, curdist = q.popleft()
  #print(y, x, curdist)
  if y == 0 and x == 0:
    print(curdist)
    path = ''
    while y != starty or x != startx:
      d = dirfrom[square[y*C+x]]
      path += dc[d]
      y += dy[d^2]
      x += dx[d^2]
    print(path[::-1])
    break
  for d in range(4):
    ny = y + dy[d]
    nx = x + dx[d]
    v = ny*C+nx
    if v in square:
      i = square[v]
      if dirfrom[i] is None:
        dirfrom[i] = d
        q.append((ny, nx, curdist+1))
