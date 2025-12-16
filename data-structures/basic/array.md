# Array

## Description
A contiguous block of memory that stores elements of the same type in sequential order. Arrays provide constant-time access to elements by index and are the foundation for many other data structures.

## Time Complexity
- Access by index: O(1)
- Search (unsorted): O(n)
- Search (sorted): O(log n) with binary search
- Insert at end: O(1) amortized (dynamic arrays)
- Insert at position: O(n)
- Delete at end: O(1)
- Delete at position: O(n)

## Space Complexity
O(n) where n is the number of elements

## Implementation

```python
class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.array = [None] * self.capacity
    
    def get(self, index):
        """Get element at index"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[index]
    
    def set(self, index, value):
        """Set element at index"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.array[index] = value
    
    def append(self, value):
        """Add element to end of array"""
        if self.size == self.capacity:
            self._resize()
        self.array[self.size] = value
        self.size += 1
    
    def insert(self, index, value):
        """Insert element at specific index"""
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        
        if self.size == self.capacity:
            self._resize()
        
        # Shift elements to the right
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        
        self.array[index] = value
        self.size += 1
    
    def delete(self, index):
        """Delete element at index"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        # Shift elements to the left
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        
        self.array[self.size - 1] = None
        self.size -= 1
    
    def _resize(self):
        """Double the capacity when full"""
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        return str([self.array[i] for i in range(self.size)])

# Example usage
if __name__ == "__main__":
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    arr.append(3)
    arr.insert(1, 10)
    
    print(arr)  # Output: [1, 10, 2, 3]
    print(arr.get(2))  # Output: 2
    arr.delete(1)
    print(arr)  # Output: [1, 2, 3]
```

## Key Points
- Direct access to any element using index
- Cache-friendly due to contiguous memory layout
- Fixed size in static arrays, dynamic in resizable arrays
- Insertion/deletion in middle requires shifting elements
- Resizing is expensive (O(n)) but amortized O(1) for appends

## Common Use Cases
- Storing collections of homogeneous data
- Implementing other data structures (stacks, queues, heaps)
- Lookup tables and hash table backing storage
- Mathematical matrices and vectors
- Buffer management

## Variations
- **Static Array**: Fixed size, allocated at creation
- **Dynamic Array**: Automatically resizes (ArrayList in Java, vector in C++, list in Python)
- **Circular Array**: Used in circular buffers and queues
- **Multi-dimensional Array**: Arrays of arrays (matrices)

## Example Problems
1. Two Sum (LeetCode #1)
2. Best Time to Buy and Sell Stock (LeetCode #121)
3. Contains Duplicate (LeetCode #217)
4. Product of Array Except Self (LeetCode #238)
5. Maximum Subarray (LeetCode #53)
6. Rotate Array (LeetCode #189)
7. Move Zeroes (LeetCode #283)

## Notes
- Python lists are dynamic arrays implemented in C
- Consider using arrays when you need fast index-based access
- For frequent insertions/deletions in the middle, linked lists may be better
- Always check bounds before accessing to avoid errors
- Resizing cost is amortized across many operations