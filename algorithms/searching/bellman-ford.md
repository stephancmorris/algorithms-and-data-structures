# Bellman-Ford Algorithm

## Description
A shortest path algorithm that works with negative edge weights and can detect negative cycles. Relaxes all edges V-1 times to find shortest paths from a single source to all other vertices.

## Time Complexity
O(V × E) where V = vertices, E = edges

## Space Complexity
O(V) for distances array

## Implementation

```python
def bellman_ford(graph, vertices, start):
    """
    Find shortest paths with negative weights
    graph: list of edges [(from, to, weight), ...]
    vertices: list of all vertices
    start: starting vertex
    Returns: (distances, has_negative_cycle)
    """
    # Initialize distances
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0
    
    # Relax edges V-1 times
    for _ in range(len(vertices) - 1):
        for u, v, weight in graph:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    
    # Check for negative cycles
    for u, v, weight in graph:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            return distances, True  # Negative cycle detected
    
    return distances, False

# With path reconstruction
def bellman_ford_with_path(graph, vertices, start, end):
    """Returns (distance, path, has_negative_cycle)"""
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0
    predecessor = {v: None for v in vertices}
    
    # Relax edges
    for _ in range(len(vertices) - 1):
        for u, v, weight in graph:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                predecessor[v] = u
    
    # Check negative cycle
    has_cycle = False
    for u, v, weight in graph:
        if distances[u] + weight < distances[v]:
            has_cycle = True
            break
    
    # Reconstruct path
    if not has_cycle:
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = predecessor[current]
        path.reverse()
        return distances[end], path, False
    
    return float('-inf'), [], True

# Example
if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [
        ('A', 'B', -1),
        ('A', 'C', 4),
        ('B', 'C', 3),
        ('B', 'D', 2),
        ('B', 'E', 2),
        ('D', 'B', 1),
        ('D', 'C', 5),
        ('E', 'D', -3)
    ]
    
    distances, has_cycle = bellman_ford(edges, vertices, 'A')
    print("Distances:", distances)
    print("Has negative cycle:", has_cycle)
```

## Key Points
- Handles negative edge weights
- Can detect negative cycles
- Slower than Dijkstra: O(VE) vs O(E log V)
- Relaxes all edges V-1 times
- Used in distance vector routing protocols

## When to Use
- Graph has negative edge weights
- Need to detect negative cycles
- Distributed systems (simpler to implement)

## Example Problems
1. Network Delay Time (LeetCode #743)
2. Cheapest Flights Within K Stops (LeetCode #787)
3. Find the City With Smallest Number of Neighbors (LeetCode #1334)

## Notes
- If distance still decreases after V-1 iterations, negative cycle exists
- Cannot use with negative cycles (distances become -∞)
- For non-negative weights, use Dijkstra instead