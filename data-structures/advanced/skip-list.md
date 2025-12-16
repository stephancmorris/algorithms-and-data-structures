# Skip List

## Description
A probabilistic data structure that allows fast search, insertion, and deletion operations in a sorted sequence. It consists of multiple levels of linked lists, where higher levels skip over many elements, providing O(log n) average performance similar to balanced trees.

## Time Complexity
- Search: O(log n) average, O(n) worst case
- Insert: O(log n) average, O(n) worst case
- Delete: O(log n) average, O(n) worst case
- All operations: O(log n) expected, O(n) worst case

## Space Complexity
O(n) on average, O(n log n) worst case

## Implementation

```python
import random

class SkipNode:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)  # Array of forward pointers

class SkipList:
    def __init__(self, max_level=16, p=0.5):
        self.max_level = max_level  # Maximum level of skip list
        self.p = p  # Probability for level generation
        self.level = 0  # Current level of skip list
        self.header = SkipNode(float('-inf'), max_level)  # Header node
    
    def _random_level(self):
        """Generate random level for new node"""
        level = 0
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level
    
    def search(self, target):
        """Search for a value in the skip list"""
        current = self.header
        
        # Start from highest level and move down
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < target:
                current = current.forward[i]
        
        # Move to next node at level 0
        current = current.forward[0]
        
        # Check if we found the target
        if current and current.value == target:
            return True
        return False
    
    def insert(self, value):
        """Insert a value into the skip list"""
        update = [None] * (self.max_level + 1)
        current = self.header
        
        # Find position to insert
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        
        # Move to next node at level 0
        current = current.forward[0]
        
        # If value already exists, don't insert duplicate
        if current and current.value == value:
            return False
        
        # Generate random level for new node
        new_level = self._random_level()
        
        # Update skip list level if necessary
        if new_level > self.level:
            for i in range(self.level + 1, new_level + 1):
                update[i] = self.header
            self.level = new_level
        
        # Create new node
        new_node = SkipNode(value, new_level)
        
        # Update forward pointers
        for i in range(new_level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node
        
        return True
    
    def delete(self, value):
        """Delete a value from the skip list"""
        update = [None] * (self.max_level + 1)
        current = self.header
        
        # Find the node to delete
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        
        # Move to next node at level 0
        current = current.forward[0]
        
        # If value not found
        if not current or current.value != value:
            return False
        
        # Update forward pointers to skip deleted node
        for i in range(self.level + 1):
            if update[i].forward[i] != current:
                break
            update[i].forward[i] = current.forward[i]
        
        # Update skip list level if necessary
        while self.level > 0 and self.header.forward[self.level] is None:
            self.level -= 1
        
        return True
    
    def display(self):
        """Display all levels of the skip list"""
        print("\n===== Skip List =====")
        for i in range(self.level, -1, -1):
            print(f"Level {i}: ", end="")
            node = self.header.forward[i]
            while node:
                print(f"{node.value} -> ", end="")
                node = node.forward[i]
            print("None")
        print("====================\n")
    
    def to_list(self):
        """Convert skip list to regular list"""
        result = []
        current = self.header.forward[0]
        while current:
            result.append(current.value)
            current = current.forward[0]
        return result

# Example usage
if __name__ == "__main__":
    skip_list = SkipList()
    
    # Insert elements
    elements = [3, 6, 7, 9, 12, 17, 19, 21, 25, 26]
    for elem in elements:
        skip_list.insert(elem)
    
    print("After inserting:", elements)
    skip_list.display()
    
    # Search for elements
    print("Search 19:", skip_list.search(19))  # True
    print("Search 15:", skip_list.search(15))  # False
    
    # Delete element
    skip_list.delete(19)
    print("\nAfter deleting 19:")
    skip_list.display()
    
    # List representation
    print("As list:", skip_list.to_list())
```

## Key Points
- Multiple levels of linked lists with express lanes
- Level 0 contains all elements
- Higher levels skip elements for faster traversal
- Probabilistic balancing (no rotations needed)
- Simple implementation compared to balanced trees
- Average case performance similar to balanced BST

## Common Use Cases
- Implementing sorted sets and maps
- In-memory databases (Redis uses skip lists)
- Real-time systems where consistency matters
- Alternative to balanced trees when simplicity preferred
- Concurrent data structures (easier to lock)

## How It Works

### Structure
- Level 0: All elements in sorted order
- Level 1: Roughly half the elements
- Level 2: Roughly quarter of the elements
- And so on...

### Level Selection
- Coin flip (probability p, usually 0.5)
- Keep flipping, increase level while heads
- Probabilistically creates balanced structure

### Search Process
1. Start at highest level
2. Move forward while next value < target
3. Drop down a level
4. Repeat until level 0
5. Check if found

## Advantages over Balanced Trees
- Simpler implementation (no rotations)
- Easier to understand and maintain
- Good cache performance (forward pointers)
- Naturally concurrent-friendly
- Probabilistic balance (no worst-case rebalancing)

## Disadvantages
- Uses more space (extra pointers)
- Probabilistic guarantees (not deterministic)
- Worst case can be O(n) (unlikely)
- More memory accesses than arrays

## Skip List vs Other Structures

### vs. Balanced BST (AVL, Red-Black)
- Simpler to implement
- Better for concurrent access
- Similar average performance
- More space overhead

### vs. Hash Table
- Maintains sorted order
- Range queries efficient
- No hash function needed
- Slower for exact lookups

### vs. B-Tree
- Better for in-memory (B-trees for disk)
- Simpler structure
- Good for smaller datasets

## Real-World Usage
- **Redis**: Sorted sets implementation
- **LevelDB**: MemTable implementation
- **Apache HBase**: In-memory storage
- **Lucene**: Index data structure

## Example Problems
While skip lists are less common in LeetCode, understanding them helps with:
1. Design Skiplist (LeetCode #1206)
2. Problems requiring sorted data with fast operations
3. Understanding probabilistic data structures
4. Database and cache implementations

## Notes
- Invented by William Pugh in 1990
- Probabilistic alternative to balanced trees
- Expected height is O(log n)
- Typically use p = 0.5 or p = 0.25
- Popular in systems programming (Redis, LevelDB)
- Good when you need simplicity over guaranteed performance
- Concurrent skip lists are easier than concurrent trees
- Practice understanding the probability analysis