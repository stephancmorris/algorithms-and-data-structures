# Graph

## Description
A non-linear data structure consisting of vertices (nodes) connected by edges. Graphs can represent networks, relationships, and connections. Unlike trees, graphs can have cycles and nodes can have multiple connections.

## Time Complexity
- Add vertex: O(1)
- Add edge: O(1)
- Remove vertex: O(V + E)
- Remove edge: O(E)
- Search (DFS/BFS): O(V + E)

Where V = vertices, E = edges

## Space Complexity
- Adjacency Matrix: O(V²)
- Adjacency List: O(V + E)

## Implementation

```python
# Adjacency List Implementation (most common)
class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph"""
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, u, v, weight=1):
        """Add an edge between vertices u and v"""
        # Add vertices if they don't exist
        self.add_vertex(u)
        self.add_vertex(v)
        
        # Add edge
        self.graph[u].append((v, weight))
        
        # If undirected, add edge in both directions
        if not self.directed:
            self.graph[v].append((u, weight))
    
    def remove_edge(self, u, v):
        """Remove edge between u and v"""
        if u in self.graph:
            self.graph[u] = [(vertex, weight) for vertex, weight in self.graph[u] if vertex != v]
        
        if not self.directed and v in self.graph:
            self.graph[v] = [(vertex, weight) for vertex, weight in self.graph[v] if vertex != u]
    
    def remove_vertex(self, vertex):
        """Remove a vertex and all its edges"""
        if vertex in self.graph:
            # Remove the vertex
            del self.graph[vertex]
            
            # Remove all edges pointing to this vertex
            for v in self.graph:
                self.graph[v] = [(neighbor, weight) for neighbor, weight in self.graph[v] if neighbor != vertex]
    
    def get_neighbors(self, vertex):
        """Get all neighbors of a vertex"""
        return self.graph.get(vertex, [])
    
    def has_edge(self, u, v):
        """Check if edge exists between u and v"""
        if u in self.graph:
            return any(vertex == v for vertex, _ in self.graph[u])
        return False
    
    def dfs(self, start, visited=None):
        """Depth-First Search traversal"""
        if visited is None:
            visited = set()
        
        visited.add(start)
        result = [start]
        
        for neighbor, _ in self.graph.get(start, []):
            if neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))
        
        return result
    
    def bfs(self, start):
        """Breadth-First Search traversal"""
        visited = set([start])
        queue = [start]
        result = []
        
        while queue:
            vertex = queue.pop(0)
            result.append(vertex)
            
            for neighbor, _ in self.graph.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def __str__(self):
        result = []
        for vertex in self.graph:
            neighbors = [f"{v}(w:{w})" for v, w in self.graph[vertex]]
            result.append(f"{vertex} -> {', '.join(neighbors)}")
        return '\n'.join(result)

# Adjacency Matrix Implementation
class GraphMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.vertex_labels = {}
    
    def add_edge(self, u, v, weight=1):
        """Add edge with weight"""
        self.matrix[u][v] = weight
        # For undirected graph:
        # self.matrix[v][u] = weight
    
    def remove_edge(self, u, v):
        """Remove edge"""
        self.matrix[u][v] = 0
    
    def has_edge(self, u, v):
        """Check if edge exists"""
        return self.matrix[u][v] != 0
    
    def print_matrix(self):
        """Print adjacency matrix"""
        for row in self.matrix:
            print(row)

# Example usage
if __name__ == "__main__":
    # Create an undirected graph
    g = Graph(directed=False)
    
    # Add edges
    g.add_edge('A', 'B', 5)
    g.add_edge('A', 'C', 3)
    g.add_edge('B', 'D', 2)
    g.add_edge('C', 'D', 1)
    g.add_edge('D', 'E', 4)
    
    print("Graph:")
    print(g)
    print()
    
    print("DFS from A:", g.dfs('A'))
    print("BFS from A:", g.bfs('A'))
    print("Neighbors of B:", g.get_neighbors('B'))
    print("Has edge A-B:", g.has_edge('A', 'B'))
```

## Key Points
- Vertices (nodes) connected by edges
- Can be directed or undirected
- Can be weighted or unweighted
- May contain cycles (unlike trees)
- Adjacency list is more space-efficient for sparse graphs
- Adjacency matrix is faster for dense graphs

## Common Use Cases
- Social networks (friends, followers)
- Road networks and GPS navigation
- Web page linking (PageRank)
- Network routing protocols
- Dependency resolution
- Recommendation systems
- State machines

## Graph Types
- **Directed (Digraph)**: Edges have direction (one-way)
- **Undirected**: Edges are bidirectional
- **Weighted**: Edges have weights/costs
- **Unweighted**: All edges equal
- **Cyclic**: Contains at least one cycle
- **Acyclic**: No cycles (DAG - Directed Acyclic Graph)
- **Connected**: Path exists between any two vertices
- **Disconnected**: Some vertices unreachable from others

## Graph Representations
- **Adjacency List**: Array/HashMap of lists (space-efficient)
- **Adjacency Matrix**: 2D array (fast edge lookup)
- **Edge List**: List of all edges (simple but inefficient)

## Graph Algorithms
- **Traversal**: DFS, BFS
- **Shortest Path**: Dijkstra, Bellman-Ford, Floyd-Warshall, A*
- **Minimum Spanning Tree**: Kruskal's, Prim's
- **Cycle Detection**: DFS with colors
- **Topological Sort**: For DAGs
- **Strongly Connected Components**: Kosaraju's, Tarjan's

## Example Problems
1. Number of Islands (LeetCode #200)
2. Clone Graph (LeetCode #133)
3. Course Schedule (LeetCode #207) - Topological sort
4. Network Delay Time (LeetCode #743) - Dijkstra
5. Cheapest Flights Within K Stops (LeetCode #787)
6. Word Ladder (LeetCode #127)
7. Graph Valid Tree (LeetCode #261)
8. Minimum Height Trees (LeetCode #310)
9. Critical Connections in Network (LeetCode #1192)

## Notes
- Choose adjacency list for sparse graphs (E << V²)
- Choose adjacency matrix for dense graphs or when edge lookups are frequent
- Always clarify if graph is directed/undirected, weighted/unweighted
- Practice both DFS and BFS implementations
- Many graph problems can be solved with DFS/BFS modifications
- Understanding graph representations is crucial for optimization