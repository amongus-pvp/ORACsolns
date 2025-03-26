# https://orac2.info/problem/378/
def solve():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    H = int(input[idx+1])
    F = int(input[idx+2])
    idx += 3
    hippos = []
    for _ in range(H):
        hippos.append(int(input[idx]))
        idx += 1
    
    if H == 1:
        if F >= 2:
            print(N - 1)
            return
        else:
            x = hippos[0]
            print(max(x - 1, N - x))
            return
    
    gaps = []
    for i in range(1, H):
        gaps.append(hippos[i] - hippos[i-1] - 1)
    
    edge1 = hippos[0] - 1
    edge2 = N - hippos[-1]
    
    gaps.sort(reverse=True)
    
    if F == 1:
        print(max(edge1, edge2))
        return
    
    bothedge = edge1 + edge2
    for i in range((F - 2) // 2):
        if i >= len(gaps):
            break
        bothedge += gaps[i]
    
    edge = max(edge1, edge2)
    for i in range((F - 1) // 2):
        if i >= len(gaps):
            break
        edge += gaps[i]
    
    noedge = 0
    for i in range(F // 2):
        if i >= len(gaps):
            break
        noedge += gaps[i]
    
    print(max(edge, max(noedge, bothedge)))

solve()
