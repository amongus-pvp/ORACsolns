# https://orac2.info/problem/296/
def main():
    import sys
    input = sys.stdin.read().split() # average crust
    
    idx = 0
    n = int(input[idx])
    idx += 1
    a = int(input[idx])
    idx += 1
    b = int(input[idx])
    idx += 1
    
    left = []
    right = []
    ans = 0
    
    for _ in range(n):
        x = int(input[idx])
        idx += 1
        y = int(input[idx])
        idx += 1
        if x > y and x > 0:
            left.append(x - max(y, 0))
            ans += x
        elif y >= x and y > 0:
            right.append(y - max(x, 0))
            ans += y
    
    if len(left) > a:
        left.sort()
        for i in range(len(left) - a):
            ans -= left[i]
    
    if len(right) > b:
        right.sort()
        for i in range(len(right) - b):
            ans -= right[i]
    
    print(ans)

if __name__ == "__main__":
    main()
