# https://orac2.info/problem/9/
import sys

class Query:
    def __init__(self, l, r, k):
        self.l = l
        self.r = r
        self.k = k
    
    def __lt__(self, other):
        return self.k > other.k

def build_tree(tree_node, tree_lazy, i, l, r):
    if l > r:
        return
    if l == r:
        tree_node[i] = 0
        tree_lazy[i] = 0
        return
    
    m = (l + r) // 2
    build_tree(tree_node, tree_lazy, i << 1, l, m)
    build_tree(tree_node, tree_lazy, (i << 1) | 1, m + 1, r)
    
    tree_node[i] = max(tree_node[i << 1], tree_node[(i << 1) | 1])
    tree_lazy[i] = max(tree_lazy[i << 1], tree_lazy[(i << 1) | 1])

def push_lazy(tree_node, tree_lazy, i, l, r):
    if tree_lazy[i] != 0:
        tree_node[i] = tree_lazy[i]
        if l != r:
            tree_lazy[i << 1] = tree_lazy[i]
            tree_lazy[(i << 1) | 1] = tree_lazy[i]
        tree_lazy[i] = 0

def update_range(tree_node, tree_lazy, i, l, r, a, b, val):
    push_lazy(tree_node, tree_lazy, i, l, r)
    if l > r or a > r or b < l:
        return
    if a <= l and r <= b:
        tree_node[i] = val
        if l != r:
            tree_lazy[i << 1] = val
            tree_lazy[(i << 1) | 1] = val
        return
    
    m = (l + r) // 2
    update_range(tree_node, tree_lazy, i << 1, l, m, a, b, val)
    update_range(tree_node, tree_lazy, (i << 1) | 1, m + 1, r, a, b, val)
    
    tree_node[i] = max(tree_node[i << 1], tree_node[(i << 1) | 1])

def query_max(tree_node, tree_lazy, i, l, r, a, b):
    if l > r or a > r or b < l:
        return -0x3f3f3f3f
    push_lazy(tree_node, tree_lazy, i, l, r)
    if a <= l and r <= b:
        return tree_node[i]
    
    m = (l + r) // 2
    return max(query_max(tree_node, tree_lazy, i << 1, l, m, a, b),
               query_max(tree_node, tree_lazy, (i << 1) | 1, m + 1, r, a, b))

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, q = map(int, input[ptr:ptr+2])
        ptr += 2
        
        # Initialize segment tree
        tree_node = [0] * (4 * (n + 2))
        tree_lazy = [0] * (4 * (n + 2))
        build_tree(tree_node, tree_lazy, 1, 1, n)
        
        queries = []
        for __ in range(q):
            l, r, k = map(int, input[ptr:ptr+3])
            ptr += 3
            queries.append(Query(l, r, k))
        
        # Process queries in descending order of k
        queries.sort()
        for query in queries:
            update_range(tree_node, tree_lazy, 1, 1, n, query.l, query.r, query.k)
        
        # Verify all queries
        valid = True
        for query in queries:
            res = query_max(tree_node, tree_lazy, 1, 1, n, query.l, query.r)
            if res != query.k:
                valid = False
                break
        
        print(1 if valid else 0)

if __name__ == "__main__":
    main()
