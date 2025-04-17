# https://orac2.info/problem/125/
import sys
import bisect

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    q = int(input[ptr])
    ptr += 1

    # Initialize binary lifting table
    LOG = 20
    next_node = [[-1] * (q + 2) for _ in range(LOG)]
    queries = [(-1, -1)] * (q + 1)  # 1-based indexing
    event_times = [[] for _ in range(n + 1)]  # Track when each element was set

    for i in range(1, q + 1):
        c = input[ptr]
        ptr += 1
        if c == 'E':
            x = int(input[ptr])
            ptr += 1
            y = int(input[ptr])
            ptr += 1
            event_times[x].append(i)
            queries[i] = (x, y)
        else:
            x = int(input[ptr])
            ptr += 1
            queries[i] = (x, -1)

    # Build the initial next pointers (binary lifting table base case)
    for i in range(1, q + 1):
        x, y = queries[i]
        if y == -1:
            continue  # Only process 'E' events for the next pointers
        # Find the first event for y that happens after i
        times = event_times[y]
        pos = bisect.bisect_left(times, i)
        if pos < len(times):
            next_node[0][i] = times[pos]
        else:
            next_node[0][i] = -1

    # Build the binary lifting table
    for k in range(1, LOG):
        for i in range(1, q + 1):
            if next_node[k-1][i] != -1:
                next_node[k][i] = next_node[k-1][next_node[k-1][i]]
            else:
                next_node[k][i] = -1

    # Process queries
    for i in range(1, q + 1):
        x, y = queries[i]
        if y != -1:
            continue  # Only process 'Q' events
        # Handle query for x at time i
        times = event_times[x]
        if not times or times[0] > i:
            print(x)
            continue

        # Start from the first event for x
        current = times[0]
        # Binary lift to find the latest event before or at i
        for k in range(LOG-1, -1, -1):
            if next_node[k][current] != -1 and next_node[k][current] <= i:
                current = next_node[k][current]
        print(queries[current][1])

if __name__ == "__main__":
    main()
