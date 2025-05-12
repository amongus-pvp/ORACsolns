# https://orac2.info/problem/144/
# this is too memory inneficient on 3 testcases, check the C++ file in the same directory as this file
import sys
from collections import defaultdict

sys.stdin = open('divain.txt', 'r')
sys.stdout = open('divaout.txt', 'w')

idx = 0
N, T = map(int, input().split())
idx += 1
K = int(input())
idx += 1

events_by_day = defaultdict(list)  # day -> list of (musician, effect)

for _ in range(K):
    d, m, r = map(int, input().split())
    events_by_day[d].append((m, r))
    idx += 1

current_effect = [0] * (N + 1)  # current slope for each musician
slope = 0
current_quality = 0
last_day = 0

# Store all unique days to process (events + T + 1 to close the interval)
important_days = set(events_by_day.keys())
important_days.add(T + 1)  # to finalize till end
important_days = sorted(important_days)

best_day = 0
best_quality = 0

for day in important_days:
    delta_days = day - last_day
    current_quality += slope * delta_days

    # If equal quality, prefer the LATEST such day
    if current_quality >= best_quality:
        best_quality = current_quality
        best_day = day - 1

    # Apply all effect changes at current day
    for musician, new_r in events_by_day.get(day, []):
        slope -= current_effect[musician]
        current_effect[musician] = new_r
        slope += current_effect[musician]

    last_day = day

print(f"{best_day} {best_quality}\n")
