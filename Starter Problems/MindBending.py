def calculate_overlap_area(r1_x1, r1_y1, r1_x2, r1_y2, r2_x1, r2_y1, r2_x2, r2_y2):
    # Calculate the overlap boundaries
    x_overlap_left = max(r1_x1, r2_x1)
    x_overlap_right = min(r1_x2, r2_x2)
    y_overlap_bottom = max(r1_y1, r2_y1)
    y_overlap_top = min(r1_y2, r2_y2)
    
    # Check if there is an overlap
    # ts is hella yap
    if x_overlap_left < x_overlap_right and y_overlap_bottom < y_overlap_top:
        overlap_width = x_overlap_right - x_overlap_left
        overlap_height = y_overlap_top - y_overlap_bottom
        overlap_area = overlap_width * overlap_height
    else:
        overlap_area = 0
    
    return overlap_area
r1_x1, r1_y1, r1_x2, r1_y2 = map(int, input().split())

r2_x1, r2_y1, r2_x2, r2_y2 = map(int, input().split())

overlap = 0
 
r1w = abs(r1_x1-r1_x2)
r1h = abs(r1_y1-r1_y2)
 
r2w = abs(r2_x1-r2_x2)
r2h = abs(r2_y1-r2_y2)
 
answer = (r1w*r1h) + (r2w*r2h) # prelim
 
overlap = calculate_overlap_area(r1_x1, r1_y1, r1_x2, r1_y2, r2_x1, r2_y1, r2_x2, r2_y2)
answer -= overlap

print(answer)
