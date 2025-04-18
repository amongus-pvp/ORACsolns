# https://orac2.info/problem/1381/


# had to copy a bunch of code for this one i struggled with this question :skull:
class SegmentTree:
    def __init__(self, data, combine_function, default_value):
        self.size = len(data)
        self.combine_function = combine_function
        self.default_value = default_value
        self.tree = [default_value] * (4 * self.size)
        self._build_tree(data, 1, 0, self.size - 1)

    def _build_tree(self, data, node_index, left, right):
        if left == right:
            self.tree[node_index] = data[left]
        else:
            mid = (left + right) // 2
            self._build_tree(data, 2 * node_index, left, mid)
            self._build_tree(data, 2 * node_index + 1, mid + 1, right)
            self.tree[node_index] = self.combine_function(self.tree[2 * node_index], self.tree[2 * node_index + 1])

    def update(self, index, value):
        self._update_tree(1, 0, self.size - 1, index, value)

    def _update_tree(self, node_index, left, right, index, value):
        if left == right:
            self.tree[node_index] = value
        else:
            mid = (left + right) // 2
            if index <= mid:
                self._update_tree(2 * node_index, left, mid, index, value)
            else:
                self._update_tree(2 * node_index + 1, mid + 1, right, index, value)
            self.tree[node_index] = self.combine_function(self.tree[2 * node_index], self.tree[2 * node_index + 1])

    def query(self, left, right):
        return self._query(1, 0, self.size - 1, left, right)

    def _query(self, node_index, left, right, query_left, query_right):
        if query_right < left or right < query_left:
            return self.default_value
        if query_left <= left and right <= query_right:
            return self.tree[node_index]
        mid = (left + right) // 2
        left_result = self._query(2 * node_index, left, mid, query_left, query_right)
        right_result = self._query(2 * node_index + 1, mid + 1, right, query_left, query_right)
        return self.combine_function(left_result, right_result)

N = int(input())  # Number of pebbles
p = list(map(int, input().split()))  # Pebble sizes

max_segment_tree = SegmentTree(p, max, 0)
min_segment_tree = SegmentTree(p, min, int(1e9))

Q = int(input())  # Number of queries
for _ in range(Q):
    query_parts = input().split()
    t = int(query_parts[0])  # Type of query

    if t == 1:
        s = int(query_parts[1]) - 1  # Pebble index (0-based)
        if s == 0:
            print(N)
            continue
        if s == N - 1:
            print(1)
            continue
        max_left = max_segment_tree.query(0, s - 1)
        min_left = min_segment_tree.query(0, s - 1)
        max_right = max_segment_tree.query(s + 1, N - 1)
        min_right = min_segment_tree.query(s + 1, N - 1)

        left_abs_diff = max(abs(p[s] - max_left), abs(p[s] - min_left))
        right_abs_diff = max(abs(p[s] - max_right), abs(p[s] - min_right))

        if left_abs_diff == right_abs_diff:
            print(-1)
        elif left_abs_diff > right_abs_diff:
            print(1)
        else:
            print(N)
    
    else:  # Query type 2 (update)
        s = int(query_parts[1]) - 1  # Pebble index (0-based)
        x = int(query_parts[2])  # New size
        p[s] = x
        max_segment_tree.update(s, x)
        min_segment_tree.update(s, x)
