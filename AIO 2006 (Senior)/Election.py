# https://orac2.info/problem/278/
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    w = int(data[idx])
    idx += 1
    h = int(data[idx])
    idx += 1
    n = int(data[idx])
    idx += 1
    
    windows = []
    for _ in range(n):
        xi = int(data[idx])
        idx += 1
        yi = int(data[idx])
        idx += 1
        wi = int(data[idx])
        idx += 1
        hi = int(data[idx])
        idx += 1
        first_corner = (xi, yi)
        second_corner = (xi + wi, yi + hi)
        windows.append((first_corner, second_corner))
    
    rectangles = set()
    rectangles.add(((0, 0), (w, h)))
    
    for window in windows:
        win_first = window[0]
        win_second = window[1]
        new_rectangles = set()
        for rect in rectangles:
            rect_first = rect[0]
            rect_second = rect[1]
            # Check if the rectangle and window do not intersect
            if (rect_first[0] >= win_second[0] or 
                rect_second[0] <= win_first[0] or 
                rect_first[1] >= win_second[1] or 
                rect_second[1] <= win_first[1]):
                new_rectangles.add(rect)
                continue
            # Split the rectangle into smaller rectangles
            # Left part
            if rect_first[0] < win_first[0]:
                new_rect = (rect_first, (win_first[0], rect_second[1]))
                new_rectangles.add(new_rect)
            # Bottom part
            if rect_first[1] < win_first[1]:
                new_rect = (rect_first, (rect_second[0], win_first[1]))
                new_rectangles.add(new_rect)
            # Right part
            if rect_second[0] > win_second[0]:
                new_rect = ((win_second[0], rect_first[1]), rect_second)
                new_rectangles.add(new_rect)
            # Top part
            if rect_second[1] > win_second[1]:
                new_rect = ((rect_first[0], win_second[1]), rect_second)
                new_rectangles.add(new_rect)
        rectangles = new_rectangles
    
    max_area = 0
    for rect in rectangles:
        first = rect[0]
        second = rect[1]
        area = (second[0] - first[0]) * (second[1] - first[1])
        if area > max_area:
            max_area = area
    
    print(max_area)

if __name__ == "__main__":
    main()
