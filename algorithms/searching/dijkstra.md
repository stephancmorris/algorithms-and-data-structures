# Dijkstra's Algorithm

## Description
A shortest path algorithm for weighted graphs with non-negative edge weights. Uses a priority queue (min-heap) to greedily select the unvisited vertex with the smallest distance, then updates distances to its neighbors.

## Time Complexity
- With binary heap: O((V + E) log V)
- With Fibonacci heap: O(E + V log V)
- Where V = vertices, E = edges

## Space Complexity
O(V) for distances array and priority queue

## Implementation

```python
import heapq
from collections import defaultdict

def dijkstra(graph, start):
    """
    Find shortest paths from start to all vertices
    graph: adjacency list {vertex: [(neighbor, weight), ...]}
    start: starting vertex
    Returns: distances dict {vertex: shortest_distance}
    """
    # Initialize distances
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    # Priority queue: (distance, vertex)
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, current_vertex = heapq.heappop(pq)
        
        # Skip if already visited
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        # Update distances to neighbors
        for neighbor, weight in graph[current_vertex]:
            distance = current_dist + weight
            
            # Only consider if shorter path found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Dijkstra with path reconstruction
def dijkstra_with_path(graph, start, end):
    """
    Find shortest path and return both distance and path
    Returns: (distance, path)
    """
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    previous = {vertex: None for vertex in graph}
    
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, current_vertex = heapq.heappop(pq)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        # Early termination if we reached the end
        if current_vertex == end:
            break
        
        for neighbor, weight in graph[current_vertex]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))
    
    # Reconstruct path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    
    return distances[end], path if path[0] == start else []

# Grid-based Dijkstra
def dijkstra_grid(grid, start, end):
    """
    Dijkstra on a grid where cell values are weights
    start: (row, col)
    end: (row, col)
    """
    rows, cols = len(grid), len(grid[0])
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = grid[start[0]][start[1]]
    
    # Priority queue: (distance, row, col)
    pq = [(grid[start[0]][start[1]], start[0], start[1])]
    visited = set()
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while pq:
        current_dist, row, col = heapq.heappop(pq)
        
        if (row, col) in visited:
            continue
        
        visited.add((row, col))
        
        if (row, col) == end:
            return current_dist
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and
                (new_row, new_col) not in visited):
                
                distance = current_dist + grid[new_row][new_col]
                
                if distance < distances[new_row][new_col]:
                    distances[new_row][new_col] = distance
                    heapq.heappush(pq, (distance, new_row, new_col))
    
    return -1  # No path found

# Example usage
if __name__ == "__main__":
    # Build graph
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
        'D': [('B', 5), ('C', 8), ('E', 2)],
        'E': [('C', 10), ('D', 2)]
    }
    
    distances = dijkstra(graph, 'A')
    print("Shortest distances from A:", distances)
    
    distance, path = dijkstra_with_path(graph, 'A', 'E')
    print(f"Path A to E: {path}, Distance: {distance}")
```

## Key Points
- Only works with non-negative edge weights
- Greedy algorithm - always picks closest unvisited vertex
- Uses priority queue for efficiency
- Guarantees shortest path
- Can terminate early when destination is reached
- Similar to BFS but for weighted graphs

## Common Use Cases
- GPS navigation and route planning
- Network routing protocols
- Social networks (shortest connection path)
- Game pathfinding (with uniform costs)
- Flight route optimization
- Maze solving with weighted cells

## Dijkstra vs Other Algorithms
| Algorithm | Edge Weights | Time | Use Case |
|-----------|--------------|------|----------|
| Dijkstra | Non-negative | O(E log V) | Single source, non-negative |
| Bellman-Ford | Any | O(VE) | Negative weights, detect cycles |
| A* | Non-negative | O(E log V) | Single pair, with heuristic |
| Floyd-Warshall | Any | O(V³) | All pairs |

## Example Problems
1. Network Delay Time (LeetCode #743)
2. Path with Maximum Probability (LeetCode #1514)
3. Cheapest Flights Within K Stops (LeetCode #787)
4. Path With Minimum Effort (LeetCode #1631)
5. Swim in Rising Water (LeetCode #778)
6. Minimum Cost to Make at Least One Valid Path (LeetCode #1368)

## Notes
- Use heapq in Python (min-heap by default)
- Track visited set to avoid reprocessing
- Can optimize with Fibonacci heap for O(E + V log V)
- For unweighted graphs, use BFS instead
- Cannot handle negative edge weights (use Bellman-Ford)
- Priority queue may contain duplicates - check visited before processing