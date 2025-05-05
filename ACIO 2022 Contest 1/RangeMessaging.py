# https://orac2.info/problem/1136/
from collections import defaultdict
import heapq

def find_set(v, parent):
    if v == parent[v]:
        return v
    parent[v] = find_set(parent[v], parent)
    return parent[v]

def union_sets(a, b, parent):
    a = find_set(a, parent)
    b = find_set(b, parent)
    if a != b:
        parent[b] = a

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    union_sets(u, v, parent)

components = defaultdict(list)
for i in range(1, N + 1):
    root = find_set(i, parent)
    components[root].append(i)

component_students = list(components.values())

pq = []
current_max = -float('inf')
pointers = [0] * len(component_students)

for i in range(len(component_students)):
    heapq.heappush(pq, (component_students[i][0], i))
    current_max = max(current_max, component_students[i][0])

min_range = float('inf')
min_left = 0
min_right = 0

while True:
    current_val, list_index = heapq.heappop(pq)
    current_range = current_max - current_val + 1
    if current_range < min_range:
        min_range = current_range
        min_left = current_val
        min_right = current_max

    pointers[list_index] += 1
    if pointers[list_index] >= len(component_students[list_index]):
        break

    next_val = component_students[list_index][pointers[list_index]]
    heapq.heappush(pq, (next_val, list_index))
    current_max = max(current_max, next_val)

print(min_range)
