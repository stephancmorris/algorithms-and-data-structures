# Linked List

## Description
A linear data structure where elements are stored in nodes, and each node points to the next node in the sequence. Unlike arrays, linked lists don't store elements in contiguous memory locations.

## Time Complexity
- Insert at head: O(1)
- Insert at tail: O(1) with tail pointer, O(n) without
- Insert at position: O(n)
- Delete at head: O(1)
- Delete at tail: O(n)
- Search: O(n)
- Access by index: O(n)

## Space Complexity
O(n) where n is the number of elements

## Implementation

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert_at_head(self, data):
        """Insert a new node at the beginning of the list"""
        new_node = Node(data)
        new_node.next = self.head  
        self.head = new_node
        self.size += 1
    
    def insert_at_tail(self, data):
        """Insert a new node at the end of the list"""
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            self.size += 1
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.size += 1
    
    def delete(self, data):
        """Delete the first occurrence of a node with given data"""
        if not self.head:
            return False
        
        # If head needs to be deleted
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def search(self, data):
        """Search for a node with given data"""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def display(self):
        """Display all elements in the list"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_tail(1)
    ll.insert_at_tail(2)
    ll.insert_at_tail(3)
    ll.insert_at_head(0)
    
    print(ll.display())  # Output: 0 -> 1 -> 2 -> 3
    print(ll.search(2))  # Output: True
    ll.delete(2)
    print(ll.display())  # Output: 0 -> 1 -> 3
```

## Key Points
- No random access - must traverse from head to reach any element
- Dynamic size - can grow or shrink easily
- Efficient insertion/deletion at the beginning
- Requires extra memory for storing pointers
- Good for implementing stacks and queues

## Common Use Cases
- Implementing stacks and queues
- Undo functionality in applications
- Browser history (back/forward buttons)
- Image viewer (next/previous image)
- Music playlists

## Variations
- **Doubly Linked List**: Each node has pointers to both next and previous nodes
- **Circular Linked List**: Last node points back to the first node
- **Skip List**: Multi-level linked list for faster searching

## Example Problems
1. Reverse a Linked List (LeetCode #206)
2. Detect Cycle in a Linked List (LeetCode #141)
3. Merge Two Sorted Lists (LeetCode #21)
4. Remove Nth Node From End (LeetCode #19)
5. Find Middle of Linked List (LeetCode #876)

## Notes
- Always check for null/None pointers to avoid crashes
- Consider using a dummy head node to simplify edge cases
- Two-pointer technique is very useful for linked list problems
- Practice with pen and paper to visualize pointer movements