# https://orac2.info/problem/130/
# another solution from JustinWang, i wrote this in C++ but when refactored to python it was too slow on like 5 testcases, so heres an actually optimised solution from someone way better at this than me :skull:
import sys
sys.setrecursionlimit(1000000000)
 
# Parse the number of nodes (n) and edges (m).
n, m = map(int, input().split())
 
# Initialize adjacency lists and cookies storage.
adj = [[] for _ in range(n + 1)]
cookie = [[] for _ in range(n + 1)]
 
# Process the edges.
for i in range(m):
    a, b, c = map(int, input().split())
    if c == 3:
        cookie[a].append(b)
    else:
        adj[a].append([b, c - 1])
        adj[b].append([a, c - 1])
 
# Initialize variables to track children, restrictions, and potential mistakes.
children = [-1] * (n + 1)
cant = [0] * (n + 1)
must = set(range(1, n + 1))
mistake = False
 
# Process each node to determine groups and validate the graph.
for i in range(1, n + 1):
    if children[i] != -1:
        continue
 
    groups = [set(), set()]
    children[i] = 0
    stack = [i]
 
    while stack:
        v = stack.pop()
        for x in cookie[v]:
            groups[children[v]].add(x)
        for a, b in adj[v]:
            if children[a] != -1:
                if children[v] ^ b != children[a]:
                    mistake = True
            else:
                children[a] = children[v] ^ b
                stack.append(a)
 
    L0, L1 = len(groups[0]), len(groups[1])
    if L0 == 0:
        if L1 > 1:
            for x in groups[1]:
                cant[x] = 1
    elif L1 == 0:
        if L0 > 1:
            for x in groups[0]:
                cant[x] = 1
    elif L0 == 1 and L1 == 1:
        must = must.intersection({min(groups[0]), min(groups[1])})
    elif L0 == 1:
        must = must.intersection({min(groups[0])})
    elif L1 == 1:
        must = must.intersection({min(groups[1])})
    else:
        mistake = True
 
    if groups[0].intersection(groups[1]):
        mistake = True
 
# Output the results.
if mistake:
    print("MISTAKE")
else:
    empty = True
    for i in range(1, n + 1):
        if i in must and cant[i] != 1:
            print(i)
            empty = False
    if empty:
        print("MISTAKE")
