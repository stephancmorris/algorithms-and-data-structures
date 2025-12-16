# A* (A-Star) Search Algorithm

## Description
An informed search algorithm that finds the shortest path between nodes using heuristics. Combines the benefits of Dijkstra (guaranteed shortest path) and Greedy Best-First Search (fast exploration). Uses f(n) = g(n) + h(n) where g(n) is cost from start and h(n) is estimated cost to goal.

## Time Complexity
O(E) in the best case with perfect heuristic
O(b^d) in worst case where b = branching factor, d = depth

## Space Complexity
O(V) for storing nodes in open and closed sets

## Implementation

```python
import heapq
from collections import defaultdict

def a_star(graph, start, goal, heuristic):
    """
    A* pathfinding algorithm
    graph: adjacency list {vertex: [(neighbor, cost), ...]}
    start: start vertex
    goal: goal vertex  
    heuristic: function(node, goal) -> estimated cost
    Returns: (path, total_cost)
    """
    # Priority queue: (f_score, g_score, vertex, path)
    open_set = [(heuristic(start, goal), 0, start, [start])]
    closed_set = set()
    g_scores = {start: 0}
    
    while open_set:
        f_score, g_score, current, path = heapq.heappop(open_set)
        
        if current == goal:
            return path, g_score
        
        if current in closed_set:
            continue
        
        closed_set.add(current)
        
        for neighbor, cost in graph.get(current, []):
            if neighbor in closed_set:
                continue
            
            tentative_g = g_score + cost
            
            if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                new_path = path + [neighbor]
                heapq.heappush(open_set, (f_score, tentative_g, neighbor, new_path))
    
    return None, float('inf')  # No path found

# Grid-based A* with Manhattan distance
def a_star_grid(grid, start, goal):
    """
    A* on grid (common for games/maps)
    grid: 2D array where 0 = passable, 1 = obstacle
    start: (row, col)
    goal: (row, col)
    """
    def manhattan_distance(pos1, pos2):
        """Heuristic: Manhattan distance"""
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    def euclidean_distance(pos1, pos2):
        """Alternative: Euclidean distance"""
        return ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**0.5
    
    rows, cols = len(grid), len(grid[0])
    
    # Priority queue: (f_score, g_score, position, path)
    open_set = [(manhattan_distance(start, goal), 0, start, [start])]
    closed_set = set()
    g_scores = {start: 0}
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 4-directional
    # For 8-directional: add [(1,1), (1,-1), (-1,1), (-1,-1)]
    
    while open_set:
        f_score, g_score, current, path = heapq.heappop(open_set)
        
        if current == goal:
            return path, g_score
        
        if current in closed_set:
            continue
        
        closed_set.add(current)
        row, col = current
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            neighbor = (new_row, new_col)
            
            # Check bounds and obstacles
            if (0 <= new_row < rows and 0 <= new_col < cols and
                grid[new_row][new_col] == 0 and neighbor not in closed_set):
                
                tentative_g = g_score + 1  # Cost = 1 per move
                
                if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                    g_scores[neighbor] = tentative_g
                    h_score = manhattan_distance(neighbor, goal)
                    f_score = tentative_g + h_score
                    new_path = path + [neighbor]
                    heapq.heappush(open_set, (f_score, tentative_g, neighbor, new_path))
    
    return None, float('inf')

# Weighted A* (greedy variant)
def weighted_a_star(graph, start, goal, heuristic, weight=1.0):
    """
    Weighted A* for faster but potentially suboptimal paths
    weight > 1: more greedy (faster, less optimal)
    weight = 1: standard A*
    weight < 1: more thorough (slower, more optimal)
    """
    open_set = [(heuristic(start, goal) * weight, 0, start, [start])]
    closed_set = set()
    g_scores = {start: 0}
    
    while open_set:
        _, g_score, current, path = heapq.heappop(open_set)
        
        if current == goal:
            return path, g_score
        
        if current in closed_set:
            continue
        
        closed_set.add(current)
        
        for neighbor, cost in graph.get(current, []):
            if neighbor in closed_set:
                continue
            
            tentative_g = g_score + cost
            
            if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal) * weight
                new_path = path + [neighbor]
                heapq.heappush(open_set, (f_score, tentative_g, neighbor, new_path))
    
    return None, float('inf')

# Example usage
if __name__ == "__main__":
    # Simple graph example
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    
    # Simple heuristic (could be based on coordinates, etc.)
    def simple_heuristic(node, goal):
        # Example: predefined heuristic values
        h_values = {'A': 7, 'B': 6, 'C': 2, 'D': 0}
        return h_values.get(node, 0)
    
    path, cost = a_star(graph, 'A', 'D', simple_heuristic)
    print(f"Path: {path}, Cost: {cost}")
    
    # Grid example
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    
    path, cost = a_star_grid(grid, (0, 0), (4, 4))
    print(f"Grid path: {path}")
    print(f"Path length: {cost}")
```

## Key Points
- Informed search using heuristic function h(n)
- f(n) = g(n) + h(n) where g = actual cost, h = estimated cost
- Guarantees shortest path if heuristic is admissible
- More efficient than Dijkstra when good heuristic available
- Widely used in games and robotics

## Heuristic Requirements

### Admissible Heuristic
- Never overestimates actual cost
- Guarantees optimal solution
- Example: straight-line distance

### Consistent Heuristic
- h(n) ≤ cost(n, n') + h(n') for every edge
- Implies admissibility
- More efficient search

## Common Heuristics

### Manhattan Distance (Grid, 4-directional)
```python
h = abs(x1 - x2) + abs(y1 - y2)
```

### Euclidean Distance (Any direction)
```python
h = sqrt((x1 - x2)² + (y1 - y2)²)
```

### Chebyshev Distance (Grid, 8-directional)
```python
h = max(abs(x1 - x2), abs(y1 - y2))
```

## A* vs Other Algorithms

| Algorithm | Heuristic | Optimal | Time |
|-----------|-----------|---------|------|
| Dijkstra | No | Yes | O(E log V) |
| A* | Yes | Yes* | O(E) best |
| Greedy BFS | Yes | No | Fast |
| BFS | No | Yes** | O(V + E) |

*If heuristic is admissible
**For unweighted graphs

## Common Use Cases
- Video game pathfinding
- GPS navigation
- Robot motion planning
- Puzzle solving (8-puzzle, Rubik's cube)
- Network routing
- Maze solving

## Optimizations

### Jump Point Search
Optimization for uniform-cost grids with symmetry.

### Hierarchical A*
Preprocess map into hierarchy for faster pathfinding.

### Bidirectional A*
Search from both start and goal simultaneously.

## Example Problems
1. Word Ladder (LeetCode #127) - can use A*
2. Sliding Puzzle (LeetCode #773)
3. Minimum Cost to Make at Least One Valid Path (LeetCode #1368)
4. Shortest Path in a Grid with Obstacles Elimination (LeetCode #1293)

## Notes
- Choice of heuristic is crucial for performance
- Admissible heuristic guarantees optimal path
- Zero heuristic → A* becomes Dijkstra
- Perfect heuristic → straight to goal
- Common in game development (Unity, Unreal Engine)
- For grids: Manhattan for 4-dir, Chebyshev for 8-dir
- Can weight heuristic for faster but suboptimal paths
- Track both g(n) and f(n) in priority queue