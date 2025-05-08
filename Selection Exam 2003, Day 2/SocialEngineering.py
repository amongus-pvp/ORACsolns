# https://orac2.info/problem/145/
from collections import deque
from itertools import combinations
import copy
import sys

sys.stdin = open("socialin.txt", "r")
sys.stdout = open("socialout.txt", "w")
 
def normalize(state):
    # Each group is a sorted tuple, and the list of groups is sorted
    return tuple(sorted(tuple(sorted(group)) for group in state))
 
def r_line(line):
    numbers = list(map(int, line.split()))
    groups = []
    group = []
    for num in numbers:
        if num == 0:
            groups.append(tuple(sorted(group)))
            group = []
        else:
            group.append(num)
    return tuple(sorted(groups))
 
def divide_groups(groups):
    results = []
    for i, group in enumerate(groups):
        if len(group) >= 2:
            mid = (len(group) + 1) // 2
            g1 = group[:mid]
            g2 = group[mid:]
            new_groups = list(groups[:i] + groups[i+1:])
            new_groups.extend([g1, g2])
            results.append(normalize(new_groups))
    return results
 
def merge_groups(groups):
    results = []
    for i in range(len(groups)):
        for j in range(i+1, len(groups)):
            g1 = groups[i]
            g2 = groups[j]
            new_group = tuple(sorted(g1 + g2))
            new_groups = list(groups[:i] + groups[i+1:j] + groups[j+1:])
            new_groups.append(new_group)
            results.append(normalize(new_groups))
    return results
 
def swap_groups(groups):
    results = []
    for i in range(len(groups)):
        for j in range(len(groups)):
            if i == j:
                continue
            g1 = groups[i]
            g2 = groups[j]
            if not g1 or not g2:
                continue
            g1_oldest = g1[-1]
            g2_youngest = g2[0]
            new_g1 = tuple(sorted(g1[:-1] + (g2_youngest,)))
            new_g2 = tuple(sorted(g2[1:] + (g1_oldest,)))
            new_groups = list(groups)
            new_groups[i] = new_g1
            new_groups[j] = new_g2
            results.append(normalize(new_groups))
    return results
 
def bfs(start, goal):
    visited = set()
    queue = deque()
    start = normalize(start)
    goal = normalize(goal)
    queue.append((start, 0))
    visited.add(start)
 
    while queue:
        state, dist = queue.popleft()
        if state == goal:
            return dist
        for next_state in divide_groups(state) + merge_groups(state) + swap_groups(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, dist + 1))

n = int(input())
start = r_line(input())
goal = r_line(input()) # doing this for ease of reading i swear my eyes hurt so much when i wrote this
print(bfs(start, goal))
