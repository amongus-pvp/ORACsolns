# https://orac2.info/problem/229/
S, U = map(int, input().split())

# Initialize 3D difference array (N+2 x N+2 x N+2)
N = 100
diff = [[[0] * (N + 2) for _ in range(N + 2)] for __ in range(N + 2)]
is_spammer = [[[False] * N for _ in range(N)] for __ in range(N)]

def add_cube(a1, h1, w1, a2, h2, w2):
    diff[a1][h1][w1] += 1
    diff[a2 + 1][h1][w1] -= 1
    diff[a1][h2 + 1][w1] -= 1
    diff[a1][h1][w2 + 1] -= 1
    diff[a2 + 1][h2 + 1][w1] += 1
    diff[a2 + 1][h1][w2 + 1] += 1
    diff[a1][h2 + 1][w2 + 1] += 1
    diff[a2 + 1][h2 + 1][w2 + 1] -= 1

for _ in range(S):
    amin, amax, hmin, hmax, wmin, wmax = map(int, input().split())
    add_cube(amin, hmin, wmin, amax, hmax, wmax)

# Compute 3D prefix sum to get is_spammer
for a in range(N):
    for h in range(N):
        for w in range(N):
            if a > 0:
                diff[a][h][w] += diff[a - 1][h][w]
            if h > 0:
                diff[a][h][w] += diff[a][h - 1][w]
            if w > 0:
                diff[a][h][w] += diff[a][h][w - 1]
            if a > 0 and h > 0:
                diff[a][h][w] -= diff[a - 1][h - 1][w]
            if a > 0 and w > 0:
                diff[a][h][w] -= diff[a - 1][h][w - 1]
            if h > 0 and w > 0:
                diff[a][h][w] -= diff[a][h - 1][w - 1]
            if a > 0 and h > 0 and w > 0:
                diff[a][h][w] += diff[a - 1][h - 1][w - 1]
            
            is_spammer[a][h][w] = diff[a][h][w] > 0

# Sum visits of non-spammers
total_visits = 0
for _ in range(U):
    a, h, w, v = map(int, input().split())
    if not is_spammer[a][h][w]:
        total_visits += v

print(total_visits)
