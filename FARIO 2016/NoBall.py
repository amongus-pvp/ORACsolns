# https://orac2.info/problem/207/
import sys
import bisect
from collections import defaultdict

def main():
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read().split()
    ptr = 0

    n, q = map(int, input[ptr:ptr+2])
    ptr += 2

    vrow = []
    vcol = []
    row = [0] * (n + 1)
    col = [0] * (n + 1)
    rows = defaultdict(list)

    for i in range(1, n + 1):
        row[i], col[i] = map(int, input[ptr:ptr+2])
        ptr += 2
        vrow.append(row[i])
        vcol.append(col[i])

    queries = []
    for _ in range(q):
        r1, c1, r2, c2 = map(int, input[ptr:ptr+4])
        ptr += 4
        queries.append((r1, c1, r2, c2))
        vrow.extend([r1, r2])
        vcol.extend([c1, c2])

    # Coordinate compression
    vrow = sorted(set(vrow))
    vcol = sorted(set(vcol))

    row_map = {v: i for i, v in enumerate(vrow)}
    col_map = {v: i for i, v in enumerate(vcol)}

    for i in range(1, n + 1):
        row[i] = row_map[row[i]]
        col[i] = col_map[col[i]]
        rows[row[i]].append(col[i])

    # Process queries with compressed coordinates
    compressed_queries = []
    for r1, c1, r2, c2 in queries:
        r1 = bisect.bisect_left(vrow, r1)
        r2 = bisect.bisect_left(vrow, r2)
        c1 = bisect.bisect_left(vcol, c1)
        c2 = bisect.bisect_left(vcol, c2)
        compressed_queries.append((r1, r2, c1, c2))

    # Segment Tree implementation
    class SegmentTree:
        class Node:
            def __init__(self):
                self.f = []
                self.g = []

            def solve(self, c1, c2):
                pos1 = bisect.bisect_left(self.f, c1)
                pos2 = bisect.bisect_right(self.f, c2) - 1
                if pos1 >= len(self.f) or pos2 < 0:
                    return 0
                return self.g[pos2] - (self.g[pos1 - 1] if pos1 > 0 else 0)

            def apply(self, r1, r2):
                cols = []
                for r in range(r1, r2 + 1):
                    cols.extend(rows.get(r, []))
                self.f = sorted(set(cols))
                freq = defaultdict(int)
                for r in range(r1, r2 + 1):
                    for c in rows.get(r, []):
                        freq[c] += 1
                self.g = []
                total = 0
                for c in sorted(freq.keys()):
                    total += freq[c]
                    self.g.append(total)

        def __init__(self, size):
            self.size = size
            self.nodes = [self.Node() for _ in range(4 * size)]

        def init(self, i, l, r):
            if l == r:
                self.nodes[i].apply(l, l)
                return
            mid = (l + r) // 2
            self.init(2 * i, l, mid)
            self.init(2 * i + 1, mid + 1, r)
            self.nodes[i].apply(l, r)

        def query(self, i, l, r, a, b, c1, c2):
            if l > r or a > r or b < l:
                return 0
            if a <= l and r <= b:
                return self.nodes[i].solve(c1, c2)
            mid = (l + r) // 2
            return self.query(2 * i, l, mid, a, b, c1, c2) + \
                   self.query(2 * i + 1, mid + 1, r, a, b, c1, c2)

    max_row = len(vrow)
    st = SegmentTree(max_row)
    st.init(1, 0, max_row - 1)

    for r1, r2, c1, c2 in compressed_queries:
        total = st.query(1, 0, max_row - 1, r1, r2, c1, c2)

        # Binary search for median row
        low, high = r1, r2
        while low <= high:
            mid = (low + high) // 2
            cnt = st.query(1, 0, max_row - 1, r1, mid, c1, c2)
            if cnt * 2 >= total:
                high = mid - 1
            else:
                low = mid + 1
        median_row = vrow[low] if low < len(vrow) else vrow[-1]

        # Binary search for median column
        low, high = c1, c2
        while low <= high:
            mid = (low + high) // 2
            cnt = st.query(1, 0, max_row - 1, r1, r2, c1, mid)
            if cnt * 2 >= total:
                high = mid - 1
            else:
                low = mid + 1
        median_col = vcol[low] if low < len(vcol) else vcol[-1]

        print(median_row, median_col)

if __name__ == "__main__":
    main()
