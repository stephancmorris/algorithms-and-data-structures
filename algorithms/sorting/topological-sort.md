# Topological Sort

## Description
Linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every edge u→v, u comes before v. Used for task scheduling with dependencies. Only possible for DAGs.

## Time Complexity
O(V + E) where V = vertices, E = edges

## Space Complexity
O(V) for recursion stack and visited set

## Implementation

```python
from collections import deque, defaultdict

# DFS-based (Kahn's is alternative)
def topological_sort_dfs(graph):
    """
    Topological sort using DFS
    graph: adjacency list {vertex: [neighbors]}
    Returns: topologically sorted list or None if cycle exists
    """
    visited = set()
    rec_stack = set()
    result = []
    
    def dfs(vertex):
        if vertex in rec_stack:
            return False  # Cycle detected
        if vertex in visited:
            return True
        
        visited.add(vertex)
        rec_stack.add(vertex)
        
        for neighbor in graph.get(vertex, []):
            if not dfs(neighbor):
                return False
        
        rec_stack.remove(vertex)
        result.append(vertex)
        return True
    
    for vertex in graph:
        if vertex not in visited:
            if not dfs(vertex):
                return None  # Graph has cycle
    
    return result[::-1]  # Reverse for correct order

# BFS-based (Kahn's Algorithm)
def topological_sort_bfs(graph):
    """
    Kahn's algorithm using BFS
    Returns topologically sorted list or None if cycle
    """
    # Calculate in-degrees
    in_degree = {v: 0 for v in graph}
    for vertex in graph:
        for neighbor in graph[vertex]:
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1
    
    # Queue of vertices with no incoming edges
    queue = deque([v for v in graph if in_degree[v] == 0])
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if all vertices processed (no cycle)
    if len(result) != len(graph):
        return None  # Cycle exists
    
    return result

# Course schedule problem pattern
def can_finish_courses(num_courses, prerequisites):
    """
    Detect if courses can be completed
    LeetCode #207 pattern
    """
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    return topological_sort_bfs(graph) is not None

def find_order(num_courses, prerequisites):
    """
    Find valid course order
    LeetCode #210 pattern
    """
    graph = {i: [] for i in range(num_courses)}
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    return topological_sort_bfs(graph) or []

# Example
if __name__ == "__main__":
    graph = {
        'A': ['C'],
        'B': ['C', 'D'],
        'C': ['E'],
        'D': ['F'],
        'E': ['F'],
        'F': []
    }
    
    print("DFS:", topological_sort_dfs(graph))
    print("BFS:", topological_sort_bfs(graph))
```

## Key Points
- Only works on DAGs (Directed Acyclic Graphs)
- Multiple valid orderings may exist
- DFS gives one valid order
- Kahn's algorithm useful for dependency resolution
- Can detect cycles during sorting

## Common Use Cases
- Course prerequisites
- Build systems (compile dependencies)
- Task scheduling
- Package dependency resolution
- Spreadsheet formula evaluation

## Example Problems
1. Course Schedule (LeetCode #207)
2. Course Schedule II (LeetCode #210)
3. Alien Dictionary (LeetCode #269)
4. Sequence Reconstruction (LeetCode #444)

## Notes
- DFS: easier to implement, gives reverse postorder
- BFS (Kahn's): better for incremental updates
- Both detect cycles
- Result not unique if multiple valid orders exist

