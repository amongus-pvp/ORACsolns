# https://orac2.info/problem/304/
def calculate_overlap(j_intervals, g_intervals):
    total_time = 0
    i, j = 0, 0  # Pointers for Jean-David and Sir Geoffrey's intervals
    
    while i < len(j_intervals) and j < len(g_intervals):
        a, b = j_intervals[i]  # Jean-David's current interval
        c, d = g_intervals[j]  # Sir Geoffrey's current interval
        
        # Calculate overlap
        overlap_start = max(a, c)
        overlap_end = min(b, d)
        
        if overlap_start < overlap_end:  # Valid overlap
            total_time += overlap_end - overlap_start
        
        # Move the pointer for the interval that ends earlier
        if b < d:
            i += 1  # Move to Jean-David's next interval
        else:
            j += 1  # Move to Sir Geoffrey's next interval
    
    return total_time
 
n = int(input())
j_intervals = []
for i in range(n):
    a, b = map(int, input().split())
    j_intervals.append((a, b))
n = int(input())
g_intervals = []
for i in range(n):
    a, b = map(int, input().split())
    g_intervals.append((a, b))
print(calculate_overlap(j_intervals, g_intervals))
