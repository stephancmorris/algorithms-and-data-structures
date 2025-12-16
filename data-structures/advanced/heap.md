# Heap (Priority Queue)

## Description
A complete binary tree that satisfies the heap property: in a max heap, parent nodes are greater than or equal to children; in a min heap, parent nodes are less than or equal to children. Often implemented as an array for efficiency.

## Time Complexity
- Insert: O(log n)
- Delete/Extract min or max: O(log n)
- Peek min or max: O(1)
- Heapify (build heap): O(n)
- Search: O(n)

## Space Complexity
O(n) where n is the number of elements

## Implementation

```python
class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        """Get parent index"""
        return (i - 1) // 2
    
    def left_child(self, i):
        """Get left child index"""
        return 2 * i + 1
    
    def right_child(self, i):
        """Get right child index"""
        return 2 * i + 2
    
    def swap(self, i, j):
        """Swap two elements"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, value):
        """Insert a new value"""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, i):
        """Restore heap property upward"""
        parent = self.parent(i)
        
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            self._heapify_up(parent)
    
    def extract_min(self):
        """Remove and return minimum element"""
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        
        return min_val
    
    def _heapify_down(self, i):
        """Restore heap property downward"""
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right
        
        if min_index != i:
            self.swap(i, min_index)
            self._heapify_down(min_index)
    
    def peek(self):
        """View minimum element without removing"""
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]
    
    def size(self):
        """Return number of elements"""
        return len(self.heap)
    
    def is_empty(self):
        """Check if heap is empty"""
        return len(self.heap) == 0
    
    def build_heap(self, arr):
        """Build heap from array in O(n) time"""
        self.heap = arr.copy()
        # Start from last non-leaf node and heapify down
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

class MaxHeap:
    """Max Heap - parent >= children"""
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] > self.heap[parent]:
            self.swap(i, parent)
            self._heapify_up(parent)
    
    def extract_max(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_val
    
    def _heapify_down(self, i):
        max_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
            max_index = left
        
        if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
            max_index = right
        
        if max_index != i:
            self.swap(i, max_index)
            self._heapify_down(max_index)
    
    def peek(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]

# Example usage
if __name__ == "__main__":
    # Min Heap
    min_heap = MinHeap()
    min_heap.insert(5)
    min_heap.insert(3)
    min_heap.insert(7)
    min_heap.insert(1)
    
    print("Min Heap:", min_heap.heap)  # [1, 3, 7, 5]
    print("Extract min:", min_heap.extract_min())  # 1
    print("Peek:", min_heap.peek())  # 3
    
    # Build heap from array
    arr = [9, 5, 6, 2, 3]
    min_heap.build_heap(arr)
    print("Built heap:", min_heap.heap)  # [2, 3, 6, 5, 9]
    
    # Using Python's heapq (min heap by default)
    import heapq
    heap = []
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 5)
    print("Python heapq:", heap)  # [1, 3, 5]
    print("Pop:", heapq.heappop(heap))  # 1
```

## Key Points
- Complete binary tree stored as array
- Parent at index i, children at 2i+1 and 2i+2
- Root is always min (min heap) or max (max heap)
- Insert: add to end, bubble up
- Extract: remove root, move last to root, bubble down
- Building heap from array is O(n), not O(n log n)

## Common Use Cases
- Priority queues (task scheduling)
- Dijkstra's shortest path algorithm
- Huffman coding (compression)
- Finding k largest/smallest elements
- Median maintenance
- Event-driven simulation
- Heap sort

## Heap vs Priority Queue
A priority queue is an abstract data type, while a heap is a concrete data structure commonly used to implement priority queues.

## Array Representation
For index i (0-based):
- Parent: (i - 1) // 2
- Left child: 2 * i + 1
- Right child: 2 * i + 2

## Example Problems
1. Kth Largest Element in Array (LeetCode #215)
2. Top K Frequent Elements (LeetCode #347)
3. Merge k Sorted Lists (LeetCode #23)
4. Find Median from Data Stream (LeetCode #295)
5. Last Stone Weight (LeetCode #1046)
6. K Closest Points to Origin (LeetCode #973)
7. Task Scheduler (LeetCode #621)
8. Reorganize String (LeetCode #767)
9. Meeting Rooms II (LeetCode #253)

## Notes
- Python's heapq only provides min heap (negate values for max heap)
- Java has PriorityQueue, C++ has priority_queue
- Heap sort uses a heap but sorts in-place
- Not suitable for searching arbitrary elements
- Perfect for "top k" or "kth largest/smallest" problems
- Always consider heap when you need to repeatedly access min/max