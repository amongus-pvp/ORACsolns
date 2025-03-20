# https://orac2.info/problem/103/
import sys
import math
import heapq
 
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
 
def dijkstra(start, end, nodes):
    n = len(nodes)
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        current_dist, u = heapq.heappop(heap)
        if u == end:
            break
        if current_dist > dist[u]:
            continue
        for v in range(n):
            if v == u:
                continue
            d = euclidean_distance(nodes[u], nodes[v])
            if d <= 50:
                if dist[v] > dist[u] + d:
                    dist[v] = dist[u] + d
                    heapq.heappush(heap, (dist[v], v))
    return dist[end]
 
def main():
    input_file = open("nightin.txt", "r")
    output_file = open("nightout.txt", "w")
    
    # Read input
    cs = tuple(map(float, input_file.readline().split()))
    burgmann = tuple(map(float, input_file.readline().split()))
    n = int(input_file.readline())
    posts = [tuple(map(float, input_file.readline().split())) for _ in range(n)]
    
    # Combine all nodes
    nodes = [cs] + posts + [burgmann]
    start = 0
    end = len(nodes) - 1
    
    # Run Dijkstra's algorithm
    shortest_distance = dijkstra(start, end, nodes)
    
    # Output the result
    output_file.write(f"{shortest_distance:.3f}\n")
    
    input_file.close()
    output_file.close()
 
if __name__ == "__main__":
    main()