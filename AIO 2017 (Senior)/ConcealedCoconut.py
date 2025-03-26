# https://orac2.info/problem/4/
import math
 
# Read input values
Ix, Iy, Id = map(int, input().split())
Cx, Cy, Cd = map(int, input().split())
 
# Compute Euclidean distance between Ishraq and Clement
d = math.sqrt((Cx - Ix) ** 2 + (Cy - Iy) ** 2)
 
# Check intersection conditions
if abs(Id - Cd) <= d <= Id + Cd:
    print("yes")
else:
    print("no")
