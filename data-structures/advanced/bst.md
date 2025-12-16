# Binary Search Tree (BST)

## Description
A binary tree where for each node, all values in the left subtree are less than the node's value, and all values in the right subtree are greater. This property enables efficient searching, insertion, and deletion operations.

## Time Complexity
- Search: O(log n) average, O(n) worst case (unbalanced)
- Insert: O(log n) average, O(n) worst case
- Delete: O(log n) average, O(n) worst case
- Find min/max: O(log n) average, O(n) worst case
- Inorder traversal: O(n) - gives sorted order

## Space Complexity
O(n) where n is the number of nodes

## Implementation

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Insert a value into the BST"""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """Helper method for recursive insertion"""
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        """Search for a value in the BST"""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        """Helper method for recursive search"""
        if node is None:
            return False
        
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def find_min(self, node=None):
        """Find minimum value (leftmost node)"""
        if node is None:
            node = self.root
        
        if node is None:
            return None
        
        while node.left is not None:
            node = node.left
        return node.value
    
    def find_max(self, node=None):
        """Find maximum value (rightmost node)"""
        if node is None:
            node = self.root
        
        if node is None:
            return None
        
        while node.right is not None:
            node = node.right
        return node.value
    
    def delete(self, value):
        """Delete a value from the BST"""
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        """Helper method for recursive deletion"""
        if node is None:
            return None
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node to delete found
            
            # Case 1: Node has no children (leaf)
            if node.left is None and node.right is None:
                return None
            
            # Case 2: Node has one child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            
            # Case 3: Node has two children
            # Find inorder successor (min value in right subtree)
            min_value = self.find_min(node.right)
            node.value = min_value
            node.right = self._delete_recursive(node.right, min_value)
        
        return node
    
    def inorder_traversal(self, node=None):
        """Inorder traversal (sorted order)"""
        if node is None:
            node = self.root
        
        result = []
        if node:
            result.extend(self.inorder_traversal(node.left))
            result.append(node.value)
            result.extend(self.inorder_traversal(node.right))
        return result
    
    def is_valid_bst(self, node=None, min_val=float('-inf'), max_val=float('inf')):
        """Check if tree is a valid BST"""
        if node is None:
            node = self.root
        
        if node is None:
            return True
        
        if node.value <= min_val or node.value >= max_val:
            return False
        
        return (self.is_valid_bst(node.left, min_val, node.value) and
                self.is_valid_bst(node.right, node.value, max_val))
    
    def height(self, node=None):
        """Calculate height of tree"""
        if node is None:
            node = self.root
        
        if node is None:
            return -1
        
        return 1 + max(self.height(node.left), self.height(node.right))

# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    
    # Insert values
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.insert(val)
    
    # Tree structure:
    #       50
    #      /  \
    #    30    70
    #   / \   / \
    # 20  40 60  80
    
    print("Inorder traversal:", bst.inorder_traversal())  # [20, 30, 40, 50, 60, 70, 80]
    print("Search 40:", bst.search(40))  # True
    print("Search 25:", bst.search(25))  # False
    print("Min value:", bst.find_min())  # 20
    print("Max value:", bst.find_max())  # 80
    print("Is valid BST:", bst.is_valid_bst())  # True
    print("Height:", bst.height())  # 2
    
    # Delete node with two children
    bst.delete(30)
    print("After deleting 30:", bst.inorder_traversal())  # [20, 40, 50, 60, 70, 80]
```

## Key Points
- Left subtree < node < right subtree (BST property)
- Inorder traversal gives sorted sequence
- Performance depends on tree balance
- Worst case is a skewed tree (linked list)
- Deletion with two children requires finding successor/predecessor

## Common Use Cases
- Implementing sorted sets and maps
- Database indexing
- Expression parsing
- Auto-complete features
- File system directories
- Priority queues (with modifications)

## BST Operations Detail
- **Search**: Compare with root, go left or right
- **Insert**: Find correct leaf position
- **Delete**: Three cases:
  1. Leaf node: Simply remove
  2. One child: Replace with child
  3. Two children: Replace with inorder successor/predecessor

## Balanced BST Variants
- **AVL Tree**: Height-balanced, strict balancing
- **Red-Black Tree**: Colored nodes, looser balancing
- **Splay Tree**: Recently accessed nodes near root
- **B-Tree**: Multi-way tree for databases

## BST Properties
- Inorder traversal produces sorted sequence
- No duplicate values (typically)
- Search path from root to node is unique
- Can be used as a priority queue
- Min always on leftmost, max on rightmost

## Example Problems
1. Validate Binary Search Tree (LeetCode #98)
2. Kth Smallest Element in BST (LeetCode #230)
3. Lowest Common Ancestor of BST (LeetCode #235)
4. Convert Sorted Array to BST (LeetCode #108)
5. Delete Node in BST (LeetCode #450)
6. Inorder Successor in BST (LeetCode #285)
7. Range Sum of BST (LeetCode #938)
8. Balance a BST (LeetCode #1382)
9. Trim a BST (LeetCode #669)

## Notes
- Unbalanced BST degrades to O(n) operations
- Use balanced BST (AVL, Red-Black) for guaranteed O(log n)
- Recursive implementations are cleaner but use stack space
- Practice both recursive and iterative versions
- Remember the BST property: left < node < right
- Deletion is the most complex operation - practice it!