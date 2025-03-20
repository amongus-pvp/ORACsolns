# https://orac2.info/problem/250/
# solution by Muyao_Zhang, i am too lazy to translate C++
N, K = map(int, input().split())
map_c = map(int, input().split())
map_m = map(int, input().split())
 
prime, out = None, None
ll = deque()
num_c = K
num_m = K + 1
pos_c = None
pos_m = None
while num_c or num_m or pos_c or pos_m:
    if (pos_c is None) and num_c:
        pos_c = next(map_c)
        num_c -= 1
    if (pos_m is None) and num_m:
        pos_m = next(map_m)
        num_m -= 1
    if pos_c and pos_m:
        if pos_m <= pos_c:
            ll.append(K + 1 - num_m)
            pos_m = None
        else:
            ll.append(-1 if num_c == K - 1 else 0)
            pos_c = None
        if len(ll) > 1:
            if ll[-1] in (-1, 0) and ll[-2] > 0:
                ch = ll.pop()
                mi = ll.pop()
                if ch == -1:
                    prime = mi
    elif pos_c:
        ll.append(-1 if num_c == K - 1 else 0)
        pos_c = None
 
        if len(ll) > 1:
            if ll[-1] in (-1, 0) and ll[-2] > 0:
                ch = ll.pop()
                mi = ll.pop()
                if ch == -1:
                    prime = mi
    elif pos_m:
        ll.append(K + 1 - num_m)
        pos_m = None
len_ll = len(ll)
out = ll[len_ll // 2]
if prime is None:
    prime_index = len_ll - ll.index(-1) - 1
    prime = ll[prime_index]

print(prime)
print(out)
