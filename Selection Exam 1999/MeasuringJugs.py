# https://orac2.info/problem/196/
import sys
from collections import deque
 
class Tracing:
    def __init__(self, from_=0, to=0, nfrom=0, nto=0):
        self.from_ = from_
        self.to = to
        self.nfrom = nfrom
        self.nto = nto
 
def bfs(a, b, c, need):
    N = 1005
    d = [[float('inf')] * N for _ in range(N)]
    trace = [[Tracing() for _ in range(N)] for __ in range(N)]
    sum_ = a
    d[a][0] = 0
    q = deque()
    q.append((a, 0))
    
    while q:
        ca, cb = q.popleft()
        cc = sum_ - ca - cb
        
        if ca == need or cb == need or cc == need:
            ans = []
            cura, curb = ca, cb
            while not (cura == a and curb == 0):
                t = trace[cura][curb]
                ans.append((t.from_, t.to))
                cura += t.nfrom
                curb -= t.nto
            
            ans.reverse()
            for step in ans:
                print(f"{step[0]} {step[1]}")
            
            if ca == need:
                print("0 1")
            elif cb == need:
                print("0 2")
            else:
                print("0 3")
            return
        
        # Pour 1 to 2
        trans = min(ca, b - cb)
        if d[ca - trans][cb + trans] > d[ca][cb] + 1:
            d[ca - trans][cb + trans] = d[ca][cb] + 1
            trace[ca - trans][cb + trans] = Tracing(1, 2, trans, trans)
            q.append((ca - trans, cb + trans))
        
        # Pour 1 to 3
        trans = min(ca, c - cc)
        if d[ca - trans][cb] > d[ca][cb] + 1:
            d[ca - trans][cb] = d[ca][cb] + 1
            trace[ca - trans][cb] = Tracing(1, 3, trans, 0)
            q.append((ca - trans, cb))
        
        # Pour 2 to 1
        trans = min(cb, a - ca)
        if d[ca + trans][cb - trans] > d[ca][cb] + 1:
            d[ca + trans][cb - trans] = d[ca][cb] + 1
            trace[ca + trans][cb - trans] = Tracing(2, 1, -trans, -trans)
            q.append((ca + trans, cb - trans))
        
        # Pour 2 to 3
        trans = min(cb, c - cc)
        if d[ca][cb - trans] > d[ca][cb] + 1:
            d[ca][cb - trans] = d[ca][cb] + 1
            trace[ca][cb - trans] = Tracing(2, 3, 0, -trans)
            q.append((ca, cb - trans))
        
        # Pour 3 to 1
        trans = min(cc, a - ca)
        if d[ca + trans][cb] > d[ca][cb] + 1:
            d[ca + trans][cb] = d[ca][cb] + 1
            trace[ca + trans][cb] = Tracing(3, 1, -trans, 0)
            q.append((ca + trans, cb))
        
        # Pour 3 to 2
        trans = min(cc, b - cb)
        if d[ca][cb + trans] > d[ca][cb] + 1:
            d[ca][cb + trans] = d[ca][cb] + 1
            trace[ca][cb + trans] = Tracing(3, 2, 0, trans)
            q.append((ca, cb + trans))
    
    print("0 0")
 
sys.stdin = open("jugsin.txt", 'r')
sys.stdout = open("jugsout.txt", 'w')
    
a, b, c = map(int, sys.stdin.readline().split())
need = int(input())
bfs(a, b, c, need)
