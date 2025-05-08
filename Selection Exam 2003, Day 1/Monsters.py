# https://orac2.info/problem/86/

import sys
sys.stdin = open("monsterin.txt", "r")
sys.stdout = open("monsterout.txt", "w")

n = int(sys.stdin.readline())
target = int(sys.stdin.readline())
monsters = [int(sys.stdin.readline()) for _ in range(n)]

# DP and path tables
dp = [[set() for _ in range(n)] for _ in range(n)]
path = [[dict() for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i].add(monsters[i])
    path[i][i][monsters[i]] = None

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        for k in range(i, j):
            for a in dp[i][k]:
                for b in dp[k + 1][j]:
                    res = abs(a - b)
                    if res not in dp[i][j]:
                        dp[i][j].add(res)
                        path[i][j][res] = (k, a, b)

if target not in dp[0][n - 1]:
    print(0)
    exit()

# Build merge tree
class Node:
    def __init__(self, i, j, val):
        self.i = i
        self.j = j
        self.val = val
        self.left = None
        self.right = None

def build(i, j, val):
    if i == j:
        return Node(i, j, val)
    k, a, b = path[i][j][val]
    node = Node(i, j, val)
    node.left = build(i, k, a)
    node.right = build(k + 1, j, b)
    return node

root = build(0, n - 1, target)

# Simulate merges
merges = []

def simulate(node, array, positions):
    if node.i == node.j:
        return array, positions

    # Process left and right subtrees
    array, positions = simulate(node.left, array, positions)
    array, positions = simulate(node.right, array, positions)

    # Merge left and right subtree roots
    li = positions[node.left.i]
    ri = positions[node.right.i]

    if li > ri:
        li, ri = ri, li  # ensure li < ri

    merged = abs(array[li] - array[ri])
    array = array[:li] + [merged] + array[li+1:ri] + array[ri+1:]

    # Update positions: merged monster takes li's place
    # Remove ri's position, and update all affected indices
    del positions[node.right.i]
    for key in positions:
        if positions[key] > ri:
            positions[key] -= 1
    positions[node.i] = li  # merged node now at li

    merges.append(li + 1)  # 1-based index
    return array, positions

initial_positions = {i: i for i in range(n)}
simulate(root, monsters[:], initial_positions)

for m in merges:
    print(m)