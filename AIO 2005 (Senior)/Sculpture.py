# https://orac2.info/problem/294/
# this was a REALLY fun problem to solve so ill be commenting my solution
import sys
from collections import defaultdict

# first time i have ever used << operator :skull:
sys.setrecursionlimit(1 << 25)

# Read the number of apples (nodes)
n = int(input())

# Special case: if there's only 1 apple, no sticks to adjust
if n == 1:
    print(0)
    exit()

# Initialize data structures:
# tree: stores each node's children and stick lengths
# done: tracks if a node's distance has been computed
# val: stores the computed distance for each node
# top: marks if a node is a leaf (top apple)
# root: maps each node to its parent's stick length and parent node
tree = [[] for _ in range(n)]
done = [False] * n
val = [0] * n
top = [False] * n
root = defaultdict(lambda: (0, 0))  # Default value is (0, 0)

# Build the tree from input
for i in range(n):
    # Read the two children and their stick lengths for node i
    a, x, b, y = map(int, input().split())
    
    # If both sticks are 0, this is a leaf node (top apple)
    if x == 0 and y == 0:
        top[i] = True
        done[i] = True  # Leaf nodes are already "done"
    
    # Store children with 0-based indexing and their stick lengths
    tree[i] = [a-1, x, b-1, y]
    
    # Record the parent information for each child
    # root[child] = (stick_length, parent_node)
    root[a-1] = (x, i)
    root[b-1] = (y, i)

def solve(node):
    ans = 0  # Tracks total adjustments needed for this subtree
    left_child, left_stick, right_child, right_stick = tree[node]
    
    # If children are leaves, their values are just their lengths
    if top[left_child]:
        val[left_child] = left_stick
        done[left_child] = True
    if top[right_child]:
        val[right_child] = right_stick
        done[right_child] = True

    # Case 1: Both children's distances are already computed
    if done[left_child] and done[right_child]:
        # Add the difference between children's distances to balance them
        ans += abs(val[left_child] - val[right_child])
        # This node's distance is max child distance plus its own stick length
        val[node] = max(val[left_child], val[right_child]) + root[node][0]
        done[node] = True
        return ans
    
    # Case 2: Only left child's distance is computed
    if done[left_child]:
        # First compute the right child's distance
        ans += solve(right_child)
        # Then balance the two children
        ans += abs(val[left_child] - val[right_child])
        val[node] = max(val[left_child], val[right_child]) + root[node][0]
        done[node] = True
        return ans
    
    # Case 3: Only right child's distance is computed
    if done[right_child]:
        # First compute the left child's distance
        ans += solve(left_child)
        # Then balance the two children
        ans += abs(val[left_child] - val[right_child])
        val[node] = max(val[left_child], val[right_child]) + root[node][0]
        done[node] = True
        return ans
    
    # Case 4: Neither child's distance is computed
    # Compute both children first
    ans += solve(left_child)
    ans += solve(right_child)
    # Then balance them
    ans += abs(val[left_child] - val[right_child])
    val[node] = max(val[left_child], val[right_child]) + root[node][0]
    done[node] = True
    return ans

print(solve(0)) # start from the root node
