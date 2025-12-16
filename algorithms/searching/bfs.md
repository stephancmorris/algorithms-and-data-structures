# Breadth-First Search (BFS)

## Description
A graph/tree traversal algorithm that explores all vertices at the current depth before moving to vertices at the next depth level. Uses a queue (FIFO) to track which vertex to visit next. Guarantees shortest path in unweighted graphs.

## Time Complexity
- Graph: O(V + E) where V = vertices, E = edges
- Tree: O(n) where n = number of nodes
- Grid: O(rows × cols)

## Space Complexity
O(V) for the queue and visited set

## Implementation

```python
from collections import deque

# Graph BFS
def bfs_graph(graph, start):
    """
    BFS traversal of a graph
    graph: adjacency list (dict or list of lists)
    start: starting vertex
    """
    visited = set([start])
    queue = deque([start])
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        # Visit all neighbors
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

# Tree BFS (Level Order Traversal)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs_tree(root):
    """Level order traversal of binary tree"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

# BFS by levels (returns list of lists)
def bfs_by_levels(root):
    """Group nodes by level"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

# Grid BFS (shortest path)
def bfs_grid(grid, start, end):
    """
    Find shortest path in grid
    grid: 2D array where 0=walkable, 1=obstacle
    start: (row, col) tuple
    end: (row, col) tuple
    """
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start[0], start[1], 0)])  # (row, col, distance)
    visited = {start}
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    
    while queue:
        row, col, dist = queue.popleft()
        
        # Found destination
        if (row, col) == end:
            return dist
        
        # Explore neighbors
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # Check bounds and obstacles
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                grid[new_row][new_col] == 0 and
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, dist + 1))
    
    return -1  # No path found

# BFS with path reconstruction
def bfs_with_path(graph, start, end):
    """Find shortest path and return the actual path"""
    if start == end:
        return [start]
    
    visited = {start}
    queue = deque([start])
    parent = {start: None}
    
    while queue:
        vertex = queue.popleft()
        
        if vertex == end:
            # Reconstruct path
            path = []
            current = end
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = vertex
                queue.append(neighbor)
    
    return []  # No path found

# Multi-source BFS
def multi_source_bfs(grid):
    """
    BFS from multiple sources simultaneously
    Example: spread of fire, flood fill from multiple points
    """
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    visited = set()
    
    # Add all sources to queue
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:  # Source cell
                queue.append((r, c, 0))
                visited.add((r, c))
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    max_distance = 0
    
    while queue:
        row, col, dist = queue.popleft()
        max_distance = max(max_distance, dist)
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                (new_row, new_col) not in visited and
                grid[new_row][new_col] == 0):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, dist + 1))
    
    return max_distance

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
    print("BFS traversal:", bfs_graph(graph, 0))  # [0, 1, 2, 3, 4, 5]
    
    # Tree example
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("Tree BFS:", bfs_tree(root))  # [1, 2, 3, 4, 5]
    print("By levels:", bfs_by_levels(root))  # [[1], [2, 3], [4, 5]]
    
    # Grid example
    grid = [
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 0, 0, 0]
    ]
    print("Shortest path length:", bfs_grid(grid, (0, 0), (3, 3)))  # 6
```

## Key Points
- Uses queue (FIFO) for level-by-level exploration
- Guarantees shortest path in unweighted graphs
- Explores all nodes at distance k before distance k+1
- Better for finding shortest path than DFS
- Requires more memory than DFS (stores all frontier nodes)

## Common Use Cases
- Shortest path in unweighted graphs
- Level order tree traversal
- Finding connected components
- Social network connections (friends within N degrees)
- Web crawlers
- GPS navigation (unweighted)
- Puzzle solving (minimum moves)

## BFS vs DFS
| Aspect | BFS | DFS |
|--------|-----|-----|
| Data Structure | Queue | Stack/Recursion |
| Path Found | Shortest | Any path |
| Memory | O(width) | O(height) |
| Complete | Yes | Yes (finite graphs) |
| Use Case | Shortest path | Path existence, topological sort |

## Common Patterns

### Pattern 1: Level-by-Level Processing
Process nodes in levels, tracking level information.

### Pattern 2: Multi-source BFS
Start BFS from multiple sources simultaneously.

### Pattern 3: Bi-directional BFS
Start from both source and destination, meet in middle.

### Pattern 4: 0-1 BFS
BFS on graph with edge weights 0 or 1 (use deque).

## Example Problems
1. Binary Tree Level Order Traversal (LeetCode #102)
2. Binary Tree Zigzag Level Order (LeetCode #103)
3. Minimum Depth of Binary Tree (LeetCode #111)
4. Shortest Path in Binary Matrix (LeetCode #1091)
5. Word Ladder (LeetCode #127)
6. Rotting Oranges (LeetCode #994)
7. Number of Islands (LeetCode #200) - can use BFS or DFS
8. Pacific Atlantic Water Flow (LeetCode #417)
9. Walls and Gates (LeetCode #286)
10. Clone Graph (LeetCode #133)

## Notes
- Always use `collections.deque` for O(1) popleft operation
- Track visited nodes to avoid infinite loops
- For grids, common directions: [(0,1), (1,0), (0,-1), (-1,0)]
- Can add diagonal: [(1,1), (1,-1), (-1,1), (-1,-1)]
- Level-by-level processing: track `level_size = len(queue)` before inner loop
- For shortest path, store distance with each node in queue
- Multi-source BFS: add all sources to queue initially
- Space complexity dominated by queue size (proportional to width)