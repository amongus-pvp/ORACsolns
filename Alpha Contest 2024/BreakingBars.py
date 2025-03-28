# https://orac2.info/problem/1373/
def main():
    n = int(input())
    bar = list(map(int, input().split()))
 
    ld = [0] * n
    seen = set()
    for i in range(n):
        seen.add(bar[i])
        ld[i] = len(seen)
 
    rd = [0] * n
    seen.clear()
    for i in range(n-1, -1, -1):
        seen.add(bar[i])
        rd[i] = len(seen)
    
    answer = 0
    for c in range(1, n):
        answer = max(answer, ld[c - 1] + rd[c])
    
    print(answer)
 
if __name__ == "__main__":
    main()
