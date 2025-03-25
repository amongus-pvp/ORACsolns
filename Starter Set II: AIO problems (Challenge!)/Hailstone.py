# https://orac2.info/problem/795/
def collatz(n, memo):
    if n in memo: 
        return memo[n]
    if n == 1:
        return 1
    if n % 2 == 0:
        memo[n] = 1 + collatz(n // 2, memo)
    else:
        memo[n] = 1 + collatz(3 * n + 1, memo)
    return memo[n]
 
m = {}
for i in range(0, 30):
    m[2**i] = i + 1
 

while True:
    c = int(input())
    if c == 0:
        break
    else:
        print(collatz(c, m)-1)