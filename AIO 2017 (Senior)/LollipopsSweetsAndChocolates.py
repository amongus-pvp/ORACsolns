# https://orac2.info/problem/168/
def solve():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    L = int(input[ptr + 1])
    ptr += 2
    shops = [0] * (N + 1)  # 1-based indexing
    for i in range(1, N + 1):
        shops[i] = int(input[ptr])
        ptr += 1
    pamph = [0] * (N + 1)  # 1-based indexing
    for i in range(1, N + 1):
        pamph[i] = int(input[ptr])
        ptr += 1

    if N == 1:
        print(1)
        return

    # Determine initial range [a, b]
    if shops[pamph[1]] > shops[pamph[2]]:
        a = (shops[pamph[1]] + shops[pamph[2]]) // 2
        b = L
    else:
        a = 1
        b = (shops[pamph[1]] + shops[pamph[2]]) // 2

    prev_shop_pos = shops[pamph[2]]
    for i in range(3, N + 1):
        current_shop_pos = shops[pamph[i]]
        if current_shop_pos < prev_shop_pos:
            a = max((current_shop_pos + prev_shop_pos) // 2, a)
        else:
            b = min((current_shop_pos + prev_shop_pos) // 2, b)

        if a > b:
            print(-1)
            return

        prev_shop_pos = current_shop_pos

    print(a)

solve()
