# https://orac2.info/problem/200/
import sys
sys.stdin = open("spiesin.txt", "r")
sys.stdout = open("spiesout.txt", "w")
 
n = int(input())
exes = []
eyes = []
for i in range(n):
    x, y = map(int, input().split())
    exes.append(x)
    eyes.append(y)
 
exes.sort()
eyes.sort()
 
print(str(exes[n//2]) + " " + str(eyes[n//2]))
