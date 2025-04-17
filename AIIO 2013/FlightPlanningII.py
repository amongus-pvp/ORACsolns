# https://orac2.info/problem/277/
import sys
from collections import defaultdict
 
def main():
    input = sys.stdin.read().split()
    ptr = 0
    N, M = map(int, input[ptr:ptr+2])
    ptr +=2
 
    country = []
    country_to_cities = defaultdict(list)
    for i in range(N):
        c = int(input[ptr])
        ptr +=1
        country.append(c)
        country_to_cities[c].append(i+1)  # cities are 1-based
 
    edges = []
    intra_edges = defaultdict(list)
    inter_edges = []
 
    for _ in range(M):
        a, b, cost = map(int, input[ptr:ptr+3])
        ptr +=3
        if country[a-1] == country[b-1]:
            intra_edges[country[a-1]].append((cost, a, b))
        else:
            inter_edges.append((cost, a, b))
    
    total_cost_saved = 0
 
    # Process intra-country edges: build MST for each country
    for c in country_to_cities:
        cities = country_to_cities[c]
        k = len(cities)
        if k <1:
            continue
        # Kruskal's algorithm
        parent = {city: city for city in cities}
        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u
        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            if root_u != root_v:
                parent[root_v] = root_u
        # Get all edges for this country
        edges_c = intra_edges[c]
        edges_c.sort()  # sorted by cost
        mst_edges = 0
        total_edges = len(edges_c)
        max_possible_edges = k -1
        for cost, a, b in edges_c:
            if mst_edges >= max_possible_edges:
                total_cost_saved += cost
                continue
            if find(a) != find(b):
                union(a, b)
                mst_edges +=1
            else:
                total_cost_saved += cost
    
    # Process inter-country edges: build MST across countries
    # We need to represent each country as a component. The initial components are the MSTs of each country.
    # So first, collect all inter edges, then build a global MST where nodes are the country components.
    # But how to model the components? Using DSU again.
 
    # Rebuild parent for all cities based on intra-MSTs
    parent = [i for i in range(N+1)]  # 1-based
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            parent[root_v] = root_u
    
    # Process intra-country unions first (from the MSTs built earlier)
    # Re-process the intra-country edges in the same way as before
    parent_intra = [i for i in range(N+1)]
    def find_intra(u):
        while parent_intra[u] != u:
            parent_intra[u] = parent_intra[parent_intra[u]]
            u = parent_intra[u]
        return u
    def union_intra(u, v):
        root_u = find_intra(u)
        root_v = find_intra(v)
        if root_u != root_v:
            parent_intra[root_v] = root_u
    
    for c in country_to_cities:
        edges_c = intra_edges.get(c, [])
        edges_c.sort()
        k = len(country_to_cities[c])
        mst_edges =0
        for cost, a, b in edges_c:
            if mst_edges >= k -1:
                break
            if find_intra(a) != find_intra(b):
                union_intra(a, b)
                mst_edges +=1
    
    # Now, the parent_intra represents the intra-country MSTs.
    # For inter-country edges, we need to connect different components (which are now country MST roots)
    inter_edges.sort()
    global_parent = parent_intra  # the intra-MSTs are the initial components
    # Now, the find for global is find_intra
    mst_inter_edges =0
    total_inter = len(inter_edges)
    # The required edges is (number of country components - 1)
    # The country components are the unique find_intra roots across all cities.
    unique_roots = set()
    for city in range(1, N+1):
        unique_roots.add(find_intra(city))
    required_inter = len(unique_roots) -1
 
    for cost, a, b in inter_edges:
        if mst_inter_edges >= required_inter:
            total_cost_saved += cost
            continue
        root_a = find_intra(a)
        root_b = find_intra(b)
        if root_a != root_b:
            union_intra(a, b)
            mst_inter_edges +=1
        else:
            total_cost_saved += cost
    
    print(total_cost_saved)
 
if __name__ == '__main__':
    main()
