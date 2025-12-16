# Queue

## Description
A First-In-First-Out (FIFO) data structure where elements are added at the rear (enqueue) and removed from the front (dequeue). Like a line of people waiting, the first person in line is the first to be served.

## Time Complexity
- Enqueue (insert at rear): O(1)
- Dequeue (remove from front): O(1)
- Peek (view front): O(1)
- Search: O(n)
- Access by index: O(n)

## Space Complexity
O(n) where n is the number of elements

## Implementation

```python
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add item to rear of queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return front item"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)  # O(n) - see note below
    
    def peek(self):
        """View front item without removing"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def is_empty(self):
        """Check if queue is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items"""
        return len(self.items)
    
    def __str__(self):
        return f"Queue({self.items})"

# More efficient implementation using collections.deque
from collections import deque

class QueueDeque:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        """Add item to rear of queue - O(1)"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return front item - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.popleft()
    
    def peek(self):
        """View front item without removing"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def is_empty(self):
        """Check if queue is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items"""
        return len(self.items)

# Linked list implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
    
    def enqueue(self, item):
        """Add item to rear of queue"""
        new_node = Node(item)
        
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self._size += 1
    
    def dequeue(self):
        """Remove and return front item"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        data = self.front.data
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
        
        self._size -= 1
        return data
    
    def peek(self):
        """View front item without removing"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data
    
    def is_empty(self):
        """Check if queue is empty"""
        return self.front is None
    
    def size(self):
        """Return number of items"""
        return self._size
    
    def display(self):
        """Display all elements"""
        elements = []
        current = self.front
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)

# Example usage
if __name__ == "__main__":
    # Using deque (recommended)
    queue = QueueDeque()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    print(queue.peek())  # Output: 1
    print(queue.dequeue())  # Output: 1
    print(queue.dequeue())  # Output: 2
    
    # Linked list queue
    ll_queue = QueueLinkedList()
    ll_queue.enqueue(10)
    ll_queue.enqueue(20)
    ll_queue.enqueue(30)
    
    print(ll_queue.display())  # Output: 10 -> 20 -> 30
    print(ll_queue.dequeue())  # Output: 10
```

## Key Points
- FIFO principle: First In, First Out
- Two ends: front (for removal) and rear (for insertion)
- Use `collections.deque` in Python for O(1) operations
- Linked list implementation avoids array shifting
- Circular queues optimize space usage

## Common Use Cases
- Breadth-First Search (BFS)
- Task scheduling and job queues
- Print queue management
- Buffering (I/O buffers, streaming)
- Message queues in systems
- Level-order tree traversal
- Request handling in servers

## Queue Variations
- **Circular Queue**: Last position connects back to first (efficient use of space)
- **Priority Queue**: Elements dequeued based on priority, not insertion order
- **Deque (Double-ended Queue)**: Insert/remove from both ends
- **Blocking Queue**: Thread-safe queue with blocking operations

## Example Problems
1. Number of Recent Calls (LeetCode #933)
2. Moving Average from Data Stream (LeetCode #346)
3. Design Circular Queue (LeetCode #622)
4. Implement Stack using Queues (LeetCode #225)
5. Design Hit Counter (LeetCode #362)
6. Shortest Path in Binary Matrix (LeetCode #1091) - BFS
7. Walls and Gates (LeetCode #286) - BFS
8. Perfect Squares (LeetCode #279) - BFS

## Notes
- Python's `list.pop(0)` is O(n), use `deque.popleft()` for O(1)
- Queues are essential for BFS algorithms
- Circular buffers prevent wasting space in fixed-size queues
- Consider using `queue.Queue` for thread-safe operations
- Always check if queue is empty before dequeue/peek operations