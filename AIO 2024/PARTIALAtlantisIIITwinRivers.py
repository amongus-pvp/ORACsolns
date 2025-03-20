# https://orac2.info/problem/1462/
# PARTIAL SOLUTION
# THIS ONLY SCORES 50 POINTS
import bisect
 
def main():
    # Read N and L
    N, L = map(int, input().split())
    
    # Read bridges (only River 1)
    bridges = []
    for _ in range(N):
        B, R = map(int, input().split())
        if R == 1:  # Only consider bridges on River 1
            bridges.append(B)
    
    # Read T
    T = int(input())
    
    # Read trips (only ending on Strip 2)
    trips = []
    for _ in range(T):
        X, S = map(int, input().split())
        if S == 2:  # Only consider trips ending on Strip 2
            trips.append(X)
    
    # Sort bridges
    bridges.sort()
    
    # Precompute closest bridge for each trip
    closest_bridge = []
    for X in trips:
        pos = bisect.bisect_left(bridges, X)
        if pos == 0:
            closest_bridge.append(bridges[0])
        elif pos == len(bridges):
            closest_bridge.append(bridges[-1])
        else:
            before = bridges[pos - 1]
            after = bridges[pos]
            if abs(X - before) <= abs(X - after):
                closest_bridge.append(before)
            else:
                closest_bridge.append(after)
    
    # Calculate initial total distance
    total_distance = 0
    for i in range(len(trips)):
        X = trips[i]
        b = closest_bridge[i]
        distance = 2 * abs(X - b) + 1
        total_distance += distance
    
    # Initialize updates array
    updates = {}
    
    # Calculate updates
    for i in range(len(trips)):
        X = trips[i]
        b = closest_bridge[i]
        d = abs(X - b)
        updates[X - d] = updates.get(X - d, 0) - 2
        updates[X] = updates.get(X, 0) + 4
        updates[X + d] = updates.get(X + d, 0) - 2
    
    # Sweep through all possible new bridge locations
    min_distance = total_distance
    rate_of_change = 0
    sorted_positions = sorted(updates.keys())
    current_pos = -L
    for pos in sorted_positions:
        if current_pos < pos:
            steps = pos - current_pos
            total_distance += rate_of_change * steps
            current_pos = pos
        rate_of_change += updates[pos]
        if 0 <= current_pos <= L:
            if total_distance < min_distance:
                min_distance = total_distance
    
    print(int(min_distance))
 
if __name__ == "__main__":
    main()
