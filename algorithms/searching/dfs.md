# Depth-First Search (DFS)

## Description
A graph/tree traversal algorithm that explores as far as possible along each branch before backtracking. Uses a stack (LIFO) - either explicitly or through recursion. Goes deep before going wide.

## Time Complexity
- Graph: O(V + E) where V = vertices, E = edges
- Tree: O(n) where n = number of nodes
- Grid: O(rows × cols)

## Space Complexity
- Recursive: O(h) where h = height (call stack)
- Iterative: O(V) for the stack and visited set

## Implementation

```python
# Recursive DFS - Graph
def dfs_recursive(graph, vertex, visited=None):
    """
    Recursive DFS traversal of graph
    graph: adjacency list
    vertex: current vertex
    visited: set of visited vertices
    """
    if visited is None:
        visited = set()
    
    visited.add(vertex)
    result = [vertex]
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    
    return result

# Iterative DFS - Graph
def dfs_iterative(graph, start):
    """Iterative DFS using explicit stack"""
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            # Add neighbors in reverse order to match recursive DFS order
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result

# Tree DFS - Inorder, Preorder, Postorder
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_dfs(root):
    """Left -> Root -> Right"""
    if not root:
        return []
    return inorder_dfs(root.left) + [root.val] + inorder_dfs(root.right)

def preorder_dfs(root):
    """Root -> Left -> Right"""
    if not root:
        return []
    return [root.val] + preorder_dfs(root.left) + preorder_dfs(root.right)

def postorder_dfs(root):
    """Left -> Right -> Root"""
    if not root:
        return []
    return postorder_dfs(root.left) + postorder_dfs(root.right) + [root.val]

# Iterative Tree DFS
def inorder_iterative(root):
    """Iterative inorder traversal"""
    result = []
    stack = []
    current = root
    
    while current or stack:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Process node
        current = stack.pop()
        result.append(current.val)
        
        # Move to right subtree
        current = current.right
    
    return result

def preorder_iterative(root):
    """Iterative preorder traversal"""
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # Push right first so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result

# Grid DFS
def dfs_grid(grid, row, col, visited):
    """
    DFS on grid (for island counting, flood fill, etc.)
    grid: 2D array
    row, col: current position
    visited: set of visited positions
    """
    rows, cols = len(grid), len(grid[0])
    
    # Base cases
    if (row < 0 or row >= rows or 
        col < 0 or col >= cols or
        (row, col) in visited or
        grid[row][col] == 0):  # 0 = water, 1 = land
        return
    
    visited.add((row, col))
    
    # Explore all 4 directions
    dfs_grid(grid, row + 1, col, visited)  # down
    dfs_grid(grid, row - 1, col, visited)  # up
    dfs_grid(grid, row, col + 1, visited)  # right
    dfs_grid(grid, row, col - 1, visited)  # left

# Path finding with DFS
def find_path_dfs(graph, start, end, path=None):
    """Find a path from start to end using DFS"""
    if path is None:
        path = []
    
    path = path + [start]
    
    if start == end:
        return path
    
    for neighbor in graph[start]:
        if neighbor not in path:  # Avoid cycles
            new_path = find_path_dfs(graph, neighbor, end, path)
            if new_path:
                return new_path
    
    return None

# Find all paths
def find_all_paths_dfs(graph, start, end, path=None):
    """Find all paths from start to end"""
    if path is None:
        path = []
    
    path = path + [start]
    
    if start == end:
        return [path]
    
    paths = []
    for neighbor in graph[start]:
        if neighbor not in path:
            new_paths = find_all_paths_dfs(graph, neighbor, end, path)
            paths.extend(new_paths)
    
    return paths

# Cycle detection in directed graph
def has_cycle_directed(graph):
    """Detect cycle in directed graph using DFS"""
    visited = set()
    rec_stack = set()  # Recursion stack
    
    def dfs(vertex):
        visited.add(vertex)
        rec_stack.add(vertex)
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True  # Back edge found - cycle exists
        
        rec_stack.remove(vertex)
        return False
    
    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex):
                return True
    
    return False

# Cycle detection in undirected graph
def has_cycle_undirected(graph):
    """Detect cycle in undirected graph"""
    visited = set()
    
    def dfs(vertex, parent):
        visited.add(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                if dfs(neighbor, vertex):
                    return True
            elif neighbor != parent:
                return True  # Found back edge to non-parent
        
        return False
    
    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, None):
                return True
    
    return False

# Connected components
def count_connected_components(graph):
    """Count number of connected components in undirected graph"""
    visited = set()
    count = 0
    
    def dfs(vertex):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor)
    
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)
            count += 1
    
    return count

# Example usage
if __name__ == "__main__":
    # Graph example
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1, 5],
        5: [2, 4]
    }
    
    print("DFS recursive:", dfs_recursive(graph, 0))
    print("DFS iterative:", dfs_iterative(graph, 0))
    
    # Tree example
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("Inorder:", inorder_dfs(root))    # [4, 2, 5, 1, 3]
    print("Preorder:", preorder_dfs(root))  # [1, 2, 4, 5, 3]
    print("Postorder:", postorder_dfs(root)) # [4, 5, 2, 3, 1]
    
    # Path finding
    print("Path 0->5:", find_path_dfs(graph, 0, 5))
    print("All paths 0->5:", find_all_paths_dfs(graph, 0, 5))
    
    # Cycle detection
    graph_with_cycle = {
        0: [1],
        1: [2],
        2: [0]
    }
    print("Has cycle:", has_cycle_directed(graph_with_cycle))  # True
```

## Key Points
- Uses stack (LIFO) - recursive call stack or explicit stack
- Goes as deep as possible before backtracking
- May not find shortest path
- Better space complexity than BFS for deep graphs
- Natural for tree traversals and backtracking

## Common Use Cases
- Tree traversals (inorder, preorder, postorder)
- Cycle detection
- Topological sorting
- Finding connected components
- Maze solving
- Sudoku solver
- Path existence checking
- Backtracking problems

## DFS Traversal Orders (Trees)

### Inorder (Left-Root-Right)
- Used for: BST to get sorted order
- Pattern: Process left, then node, then right

### Preorder (Root-Left-Right)
- Used for: Creating copy of tree
- Pattern: Process node first, then children

### Postorder (Left-Right-Root)
- Used for: Deleting tree, calculating tree properties
- Pattern: Process children first, then node

## Common Patterns

### Pattern 1: Backtracking
Explore path, backtrack if it doesn't work, try another.

### Pattern 2: Cycle Detection
Track recursion stack or parent to detect cycles.

### Pattern 3: Connected Components
Run DFS from each unvisited node, increment counter.

### Pattern 4: Path Finding
Build path while exploring, return when target found.

## Example Problems
1. Number of Islands (LeetCode #200)
2. Clone Graph (LeetCode #133)
3. Path Sum (LeetCode #112)
4. Course Schedule (LeetCode #207) - cycle detection
5. Binary Tree Inorder Traversal (LeetCode #94)
6. Validate Binary Search Tree (LeetCode #98)
7. Same Tree (LeetCode #100)
8. Surrounded Regions (LeetCode #130)
9. Max Area of Island (LeetCode #695)
10. All Paths From Source to Target (LeetCode #797)
11. Word Search (LeetCode #79)
12. Flood Fill (LeetCode #733)

## Notes
- Recursive DFS is cleaner but can cause stack overflow for deep graphs
- Iterative DFS uses explicit stack to avoid stack overflow
- For trees, consider which traversal order fits the problem
- Always track visited nodes to avoid infinite loops in graphs
- For grids, mark cells as visited or modify in-place
- DFS is the basis for many backtracking algorithms
- Space: O(h) for recursion vs O(V) for iterative
- Can use DFS for topological sort (postorder in DAG)