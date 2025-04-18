# https://orac2.info/problem/1082/
import sys
sys.stdin = open("holesin.txt", "r")
sys.stdout = open("holesout.txt", "w")

l, w = map(int, input().split())
a, b = map(int, input().split())

print((l//a)*(w//b))
