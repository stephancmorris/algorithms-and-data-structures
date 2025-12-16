# Disjoint Set (Union-Find)

## Description
A data structure that keeps track of elements partitioned into disjoint (non-overlapping) sets. It efficiently performs two operations: finding which set an element belongs to, and merging two sets together.

## Time Complexity
- Find: O(α(n)) ≈ O(1) amortized with path compression
- Union: O(α(n)) ≈ O(1) amortized with union by rank
- MakeSet: O(1)

Where α(n) is the inverse Ackermann function, which grows extremely slowly.

## Space Complexity
O(n) where n is the number of elements

## Implementation

```python
class DisjointSet:
    def __init__(self, n):
        """Initialize n disjoint sets"""
        self.parent = list(range(n))  # Each element is its own parent
        self.rank = [0] * n  # Rank for union by rank
        self.size = [1] * n  # Size of each set
        self.num_sets = n  # Number of disjoint sets
    
    def find(self, x):
        """
        Find the representative (root) of the set containing x
        Uses path compression for optimization
        """
        if self.parent[x] != x:
            # Path compression: make parent point directly to root
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """
        Merge the sets containing x and y
        Uses union by rank for optimization
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        # Already in same set
        if root_x == root_y:
            return False
        
        # Union by rank: attach smaller tree to larger tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.rank[root_x] += 1
        
        self.num_sets -= 1
        return True
    
    def connected(self, x, y):
        """Check if x and y are in the same set"""
        return self.find(x) == self.find(y)
    
    def get_set_size(self, x):
        """Get size of the set containing x"""
        return self.size[self.find(x)]
    
    def count_sets(self):
        """Return number of disjoint sets"""
        return self.num_sets

# Alternative implementation with dictionary (for non-integer elements)
class DisjointSetDict:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def make_set(self, x):
        """Create a new set with element x"""
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
    
    def find(self, x):
        """Find with path compression"""
        if x not in self.parent:
            self.make_set(x)
        
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """Union by rank"""
        self.make_set(x)
        self.make_set(y)
        
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True
    
    def connected(self, x, y):
        """Check if x and y are connected"""
        return self.find(x) == self.find(y)

# Example usage
if __name__ == "__main__":
    # Create disjoint set with 10 elements (0-9)
    ds = DisjointSet(10)
    
    # Initially, each element is in its own set
    print("Number of sets:", ds.count_sets())  # 10
    
    # Union operations
    ds.union(0, 1)  # {0,1}, {2}, {3}, ...
    ds.union(2, 3)  # {0,1}, {2,3}, {4}, ...
    ds.union(0, 2)  # {0,1,2,3}, {4}, {5}, ...
    
    print("Number of sets:", ds.count_sets())  # 7
    
    # Check if connected
    print("0 and 3 connected:", ds.connected(0, 3))  # True
    print("0 and 4 connected:", ds.connected(0, 4))  # False
    
    # Get set size
    print("Size of set containing 0:", ds.get_set_size(0))  # 4
    
    # Dictionary-based example
    ds_dict = DisjointSetDict()
    ds_dict.union("Alice", "Bob")
    ds_dict.union("Charlie", "David")
    ds_dict.union("Alice", "Charlie")
    
    print("Alice and David connected:", ds_dict.connected("Alice", "David"))  # True
    print("Alice and Eve connected:", ds_dict.connected("Alice", "Eve"))  # False
```

## Key Points
- Two main optimizations: path compression and union by rank
- Path compression flattens tree during find
- Union by rank keeps trees balanced
- Together, operations are nearly O(1)
- Very efficient for connectivity problems

## Common Use Cases
- Network connectivity
- Kruskal's minimum spanning tree algorithm
- Image processing (connected components)
- Social network friend groups
- Least common ancestor problems
- Cycle detection in undirected graphs
- Percolation theory

## Optimizations

### Path Compression
When finding the root, make all nodes on the path point directly to the root. This flattens the tree structure.

### Union by Rank
When merging sets, attach the tree with smaller rank to the tree with larger rank. This keeps trees balanced.

### Union by Size
Alternative to union by rank: attach smaller tree (by number of nodes) to larger tree.

## Applications in Algorithms

### Kruskal's MST
Used to detect cycles when adding edges to the minimum spanning tree.

### Cycle Detection
In an undirected graph, if two vertices of an edge are in the same set, adding the edge creates a cycle.

### Dynamic Connectivity
Efficiently answer queries about whether two nodes are connected in a dynamically changing graph.

## Example Problems
1. Number of Connected Components (LeetCode #323)
2. Redundant Connection (LeetCode #684)
3. Accounts Merge (LeetCode #721)
4. Most Stones Removed (LeetCode #947)
5. Regions Cut by Slashes (LeetCode #959)
6. Satisfiability of Equality Equations (LeetCode #990)
7. Smallest String With Swaps (LeetCode #1202)
8. Number of Provinces (LeetCode #547)
9. Longest Consecutive Sequence (LeetCode #128) - can use Union-Find

## Notes
- Also known as Union-Find or Merge-Find Set
- Without optimizations, operations can be O(n)
- With both optimizations, nearly constant time
- Essential for graph connectivity problems
- Practice implementing both optimizations
- Common in competitive programming
- When you see "groups" or "connected components", think Union-Find