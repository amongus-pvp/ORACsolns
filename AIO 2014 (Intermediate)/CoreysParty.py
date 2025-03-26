# https://orac2.info/problem/199/
import sys
from collections import defaultdict
 
def solve():
    input_lines = sys.stdin.read().splitlines()
    first_line = input_lines[0].split()
    N = int(first_line[0])
    M = int(first_line[1])
    A = int(first_line[2])
    B = int(first_line[3])
    
    adj = defaultdict(set)
    for line in input_lines[1:M+1]:
        x, y = map(int, line.split())
        adj[x].add(y)
        adj[y].add(x)
    
    # Initialize all friends as candidates
    candidates = set(range(1, N+1))
    changed = True
    
    while changed:
        changed = False
        to_remove = set()
        for x in candidates:
            # Count how many friends in candidates x knows
            known = 0
            for y in adj[x]:
                if y in candidates:
                    known += 1
            total_in_candidates = len(candidates) - 1
            unknown = total_in_candidates - known
            if known < A or unknown < B:
                to_remove.add(x)
        if to_remove:
            candidates -= to_remove
            changed = True
    
    print(len(candidates) if candidates else 0)
 
solve()
