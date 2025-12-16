# LRU Cache (Least Recently Used Cache)

## Description
A cache that evicts the least recently used item when capacity is reached. Combines a hash map for O(1) access and a doubly linked list for O(1) insertion/deletion to maintain usage order.

## Time Complexity
- Get: O(1)
- Put: O(1)
- All operations: O(1)

## Space Complexity
O(capacity) where capacity is the maximum number of items

## Implementation

```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        
        # Dummy head and tail for easier operations
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_to_front(self, node):
        """Add node right after head (most recently used)"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        """Remove node from linked list"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _move_to_front(self, node):
        """Move node to front (mark as most recently used)"""
        self._remove_node(node)
        self._add_to_front(node)
    
    def _remove_lru(self):
        """Remove least recently used node (before tail)"""
        lru_node = self.tail.prev
        self._remove_node(lru_node)
        return lru_node
    
    def get(self, key):
        """Get value for key, return -1 if not found"""
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._move_to_front(node)
        return node.value
    
    def put(self, key, value):
        """Insert or update key-value pair"""
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            # Add new key
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)
            
            # Check capacity
            if len(self.cache) > self.capacity:
                lru_node = self._remove_lru()
                del self.cache[lru_node.key]
    
    def display(self):
        """Display cache contents from most to least recently used"""
        result = []
        current = self.head.next
        while current != self.tail:
            result.append(f"{current.key}:{current.value}")
            current = current.next
        return " -> ".join(result)

# Simpler implementation using OrderedDict
from collections import OrderedDict

class LRUCacheSimple:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        if key not in self.cache:
            return -1
        
        # Move to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            # Update and move to end
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        
        # Remove least recently used (first item)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Example usage
if __name__ == "__main__":
    cache = LRUCache(3)
    
    cache.put(1, "A")
    cache.put(2, "B")
    cache.put(3, "C")
    print("Cache:", cache.display())  # 3:C -> 2:B -> 1:A
    
    cache.get(1)  # Access 1
    print("After get(1):", cache.display())  # 1:A -> 3:C -> 2:B
    
    cache.put(4, "D")  # Evicts 2 (least recently used)
    print("After put(4,D):", cache.display())  # 4:D -> 1:A -> 3:C
    
    print("get(2):", cache.get(2))  # -1 (not found)
    print("get(3):", cache.get(3))  # C
    
    # Using OrderedDict version
    simple_cache = LRUCacheSimple(2)
    simple_cache.put(1, 1)
    simple_cache.put(2, 2)
    print(simple_cache.get(1))  # 1
    simple_cache.put(3, 3)  # evicts key 2
    print(simple_cache.get(2))  # -1
```

## Key Points
- Combines HashMap (O(1) access) and Doubly Linked List (O(1) reordering)
- Most recently used items at front, least recently used at back
- On access, move item to front
- On capacity reached, remove from back
- Dummy head/tail simplify edge cases

## Common Use Cases
- Browser cache
- Database query result caching
- Memory management in OS
- CDN content caching
- API response caching
- Memoization with limited memory

## Why Doubly Linked List?
- Need to move nodes to front: O(1) with pointers
- Need to remove nodes from middle: O(1) with pointers
- Need to remove from back: O(1) with tail pointer
- Singly linked list would require O(n) to find previous node

## Design Decisions
- **HashMap**: Maps key to node for O(1) lookup
- **Doubly Linked List**: Maintains usage order
- **Dummy Nodes**: Simplify edge cases (empty list, single element)
- **Move on Access**: Both get() and put() update recency

## Variations
- **LFU Cache**: Evicts least frequently used
- **MRU Cache**: Evicts most recently used
- **TTL Cache**: Items expire after time period
- **Write-through vs Write-back**: When to persist to storage

## Example Problems
1. LRU Cache (LeetCode #146) - The classic problem
2. LFU Cache (LeetCode #460)
3. Design In-Memory File System (LeetCode #588)
4. All O(1) Data Structure (LeetCode #432)

## Notes
- Python's OrderedDict provides simpler implementation
- In interviews, implement from scratch to show understanding
- Practice drawing the data structure state after each operation
- Remember to update both HashMap and LinkedList together
- Consider thread-safety for production systems
- This is a very common system design interview question