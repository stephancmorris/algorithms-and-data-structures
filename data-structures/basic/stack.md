# Stack

## Description
A Last-In-First-Out (LIFO) data structure where elements are added and removed from the same end (the top). Like a stack of plates, you can only add or remove from the top.

## Time Complexity
- Push (insert): O(1)
- Pop (remove): O(1)
- Peek (view top): O(1)
- Search: O(n)
- Access by index: O(n)

## Space Complexity
O(n) where n is the number of elements

## Implementation

```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top of stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """View top item without removing"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items"""
        return len(self.items)
    
    def __str__(self):
        return f"Stack({self.items})"

# Using a linked list for implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self._size = 0
    
    def push(self, item):
        """Add item to top of stack"""
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
    
    def pop(self):
        """Remove and return top item"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return data
    
    def peek(self):
        """View top item without removing"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.data
    
    def is_empty(self):
        """Check if stack is empty"""
        return self.top is None
    
    def size(self):
        """Return number of items"""
        return self._size
    
    def display(self):
        """Display all elements"""
        elements = []
        current = self.top
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)

# Example usage
if __name__ == "__main__":
    # Array-based stack
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    print(stack)  # Output: Stack([1, 2, 3])
    print(stack.peek())  # Output: 3
    print(stack.pop())  # Output: 3
    print(stack)  # Output: Stack([1, 2])
    
    # Linked list stack
    ll_stack = StackLinkedList()
    ll_stack.push(10)
    ll_stack.push(20)
    ll_stack.push(30)
    
    print(ll_stack.display())  # Output: 30 -> 20 -> 10
    print(ll_stack.pop())  # Output: 30
```

## Key Points
- LIFO principle: Last In, First Out
- All operations happen at one end (top)
- Can be implemented using arrays or linked lists
- Very efficient - all main operations are O(1)
- Natural recursion call stack behavior

## Common Use Cases
- Function call stack (recursion)
- Undo/Redo functionality in editors
- Expression evaluation (infix to postfix conversion)
- Backtracking algorithms (DFS, maze solving)
- Browser history (back button)
- Syntax parsing and matching brackets
- Reversing a sequence

## Stack Applications in Algorithms
- Depth-First Search (DFS)
- Backtracking problems
- Balanced parentheses checking
- Evaluating postfix expressions
- Tower of Hanoi
- Implementing recursion iteratively

## Example Problems
1. Valid Parentheses (LeetCode #20)
2. Min Stack (LeetCode #155)
3. Evaluate Reverse Polish Notation (LeetCode #150)
4. Daily Temperatures (LeetCode #739)
5. Next Greater Element I (LeetCode #496)
6. Decode String (LeetCode #394)
7. Basic Calculator (LeetCode #224)
8. Largest Rectangle in Histogram (LeetCode #84)

## Notes
- Python lists work well as stacks (append/pop from end)
- Use collections.deque for thread-safe operations
- Stack overflow occurs when stack size limit is exceeded
- Consider stack size limits in recursive algorithms
- Monotonic stacks are useful for "next greater/smaller element" problems