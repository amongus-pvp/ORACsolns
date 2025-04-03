# https://orac2.info/problem/148/
import sys
from collections import defaultdict
 
def main():
    n = int(sys.stdin.readline())
    stars = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        stars.append((x, y))
    
    # Sort stars by y-coordinate in descending order
    stars.sort(key=lambda point: (-point[1], point[0]))
    
    # Group stars by their y-coordinate
    height_map = defaultdict(list)
    for x, y in stars:
        height_map[y].append(x)
    
    max_size = 0
    for i in range(n):
        tip_x, tip_y = stars[i]
        # Iterate over all possible side star heights above the tip
        for side_y in height_map:
            if side_y <= tip_y:
                continue  # Side stars must be above the tip
            x_coords = height_map[side_y]
            if len(x_coords) < 2:
                continue  # Need at least two stars at the same height
            # Check all pairs of stars at this height
            for j in range(len(x_coords)):
                for k in range(j + 1, len(x_coords)):
                    left_x = min(x_coords[j], x_coords[k])
                    right_x = max(x_coords[j], x_coords[k])
                    if left_x < tip_x < right_x:
                        width = right_x - left_x
                        height = side_y - tip_y
                        if width <= height:
                            size = width + height
                            if size > max_size:
                                max_size = size
    print(max_size)
 
if __name__ == "__main__":
    main()
