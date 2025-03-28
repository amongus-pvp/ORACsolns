# https://orac2.info/problem/1376/
import sys
import heapq
 
def main():
    # Read input
    n = int(input())
    islands = []
    islands2 = []
    for i in range(n):
        x, y = map(int, input().split())
        islands.append(((x, y), i))
        islands2.append(((y, x), i))
    
    # Sort islands by x and y coordinates
    islands.sort()
    islands2.sort()
    
    # Represent as a graph
    graph = [[] for _ in range(n)]
    
    # Add edges for patches with the same x-coordinate
    for i in range(n - 1):
        if islands[i][0][0] == islands[i + 1][0][0]:
            dist = abs(islands[i][0][1] - islands[i + 1][0][1])
            graph[islands[i][1]].append((islands[i + 1][1], dist))
            graph[islands[i + 1][1]].append((islands[i][1], dist))
    
    # Add edges for patches with the same y-coordinate
    for i in range(n - 1):
        if islands2[i][0][0] == islands2[i + 1][0][0]:
            dist = abs(islands2[i][0][1] - islands2[i + 1][0][1])
            graph[islands2[i][1]].append((islands2[i + 1][1], dist))
            graph[islands2[i + 1][1]].append((islands2[i][1], dist))
    
    # Dijkstra's algorithm
    distances = [float('inf')] * n
    distances[0] = 0
    pq = [(0, 0)]
    visited = [False] * n
    
    while pq:
        current_dist, v = heapq.heappop(pq)
        if visited[v]:
            continue
        visited[v] = True
        for neighbor, weight in graph[v]:
            if distances[v] + weight < distances[neighbor]:
                distances[neighbor] = distances[v] + weight
                heapq.heappush(pq, (distances[neighbor], neighbor))
    
    # Output the result
    if distances[n - 1] == float('inf'):
        print(-1)
    else:
        print(distances[n - 1])
 
if __name__ == "__main__":
    main()
