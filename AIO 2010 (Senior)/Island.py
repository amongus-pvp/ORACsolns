# https://orac2.info/problem/230/
import bisect
 
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    l = int(data[idx + 1])
    idx += 2
    
    if n == 0 or l == 0:
        print(0)
        return
    
    v = []
    p = []
    total = 0
    half = 0
    score = 0
    
    for _ in range(n):
        pos = int(data[idx]) - 1  # Convert to 0-based index
        pop = int(data[idx + 1])
        v.append(pos)
        p.append(pop)
        idx += 2
        if pos > v[0] and pos <= (v[0] + 2 * l):
            half += pop
        total += pop
        # Calculate the minimal distance (clockwise or counter-clockwise)
        dist = min(pos - v[0], 4 * l + v[0] - pos)
        score += dist * pop
    
    if n == 1:
        ans = l * p[0] * 2
        print(ans)
        return
    
    ans = score
    i1 = v[0]
    i2 = (v[0] + 2 * l) % (4 * l)
    p1 = 0
    # Find the first house beyond i2
    p2 = bisect.bisect_right(v, i2) - 1
    if p2 < 0:
        p2 += n
    
    for _ in range(200005):  # Sufficiently large number to cover all possible moves
        # Calculate distances to next houses
        next_p1 = (p1 + 1) % n
        dist1 = (v[next_p1] - i1) % (4 * l)
        next_p2 = (p2 + 1) % n
        dist2 = (v[next_p2] - i2) % (4 * l)
        move = min(dist1, dist2)
        
        # Update the score
        score -= move * half
        score += move * (total - half)
        ans = max(ans, score)
        
        # Move the pointers based on the minimal distance
        if dist1 <= dist2:
            p1 = next_p1
            half -= p[p1]
        if dist2 <= dist1:
            p2 = next_p2
            half += p[p2]
        
        # Update the current positions
        i1 = (i1 + move) % (4 * l)
        i2 = (i2 + move) % (4 * l)
    
    print(ans)
 
if __name__ == "__main__":
    main()
