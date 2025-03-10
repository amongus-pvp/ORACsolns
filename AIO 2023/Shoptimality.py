# https://orac2.info/problem/1301/
import bisect
 
n, m = map(int, input().split())
house_locations = list(map(int, input().split()))
shop_locations = list(map(int, input().split()))
shop_prices = list(map(int, input().split()))

# Precompute the minimum cost to reach each supermarket from the left and right
p = [[0, 0] for _ in range(m)]  # p[i][0] = left cost, p[i][1] = right cost

# Left-to-right pass
p[0][0] = shop_prices[0]
for i in range(1, m):
    p[i][0] = min(p[i - 1][0] + abs(shop_locations[i] - shop_locations[i - 1]), shop_prices[i])

# Right-to-left pass
p[m - 1][1] = shop_prices[m - 1]
for i in range(m - 2, -1, -1):
    p[i][1] = min(p[i + 1][1] + abs(shop_locations[i] - shop_locations[i + 1]), shop_prices[i])

# For each house, find the best supermarket
result = []
for house in house_locations:
    # Find the closest supermarkets to the left and right
    left_shop = bisect.bisect_left(shop_locations, house) - 1
    right_shop = bisect.bisect_right(shop_locations, house)

    # Calculate badness for the closest supermarkets
    if left_shop < 0:
        # No supermarket to the left, only consider the right one
        badness = p[right_shop][1] + abs(house - shop_locations[right_shop])
    elif right_shop >= m:
        # No supermarket to the right, only consider the left one
        badness = p[left_shop][0] + abs(house - shop_locations[left_shop])
    else:
        # Consider both left and right supermarkets
        badness_left = p[left_shop][0] + abs(house - shop_locations[left_shop])
        badness_right = p[right_shop][1] + abs(house - shop_locations[right_shop])
        badness = min(badness_left, badness_right)

    result.append(badness)

print(" ".join(map(str, result)))