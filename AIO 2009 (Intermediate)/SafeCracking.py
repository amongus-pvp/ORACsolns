# https://orac2.info/problem/70/
def solve():
    a, b = map(int, input().split())
    
    code_sheet = [int(input()) for _ in range(a)]
    known_code = [int(input()) for _ in range(b)]
    
    for start in range(a - b + 1):
        if code_sheet[start] < known_code[0]:
            continue  # Skip if k would be negative
        
        k = code_sheet[start] - known_code[0]
        
        match = True
        for i in range(1, b):
            if code_sheet[start + i] - known_code[i] != k:
                match = False
                break
        
        if match:
            actual_code = [num - k for num in code_sheet]
            for num in actual_code:
                print(num)
            return
 
solve()
