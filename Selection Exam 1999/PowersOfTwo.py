# https://orac2.info/problem/179/
import sys
def main():
    n = input()

    cur = 1
    ans = 0

    while ans < 10000:
    if n in str(cur):
        print(ans)
        return 0
    cur *= 2
    ans += 1

    print("No solution found")
    return 0
# mathematically proven
 
if __name__ == '__main__':
    main()