# https://orac2.info/problem/171/
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    w = int(data[idx])
    idx += 1
    h = int(data[idx])
    idx += 1
    k = int(data[idx])
    idx += 1
    
    v = []
    for _ in range(k):
        p = int(data[idx])
        idx += 1
        maxx = -1
        minx = w + 5
        for _ in range(p):
            x = int(data[idx])
            idx += 1
            y = int(data[idx])  # y is read but not used
            idx += 1
            minx = min(minx, x)
            maxx = max(maxx, x)
        if minx != maxx:
            v.append((minx, maxx - 1))
    
    # Sort intervals based on the start
    v.sort()
    
    # Merge overlapping or adjacent intervals
    newv = []
    for interval in v:
        if not newv:
            newv.append(interval)
        else:
            last_start, last_end = newv[-1]
            current_start, current_end = interval
            if current_start <= last_end + 1:
                # Merge them
                new_end = max(last_end, current_end)
                newv[-1] = (last_start, new_end)
            else:
                newv.append(interval)
    
    # Calculate the remaining width
    ans = w
    for (start, end) in newv:
        ans -= (end - start + 1)
    
    print(ans)

if __name__ == "__main__":
    main()
