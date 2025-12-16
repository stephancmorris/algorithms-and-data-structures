# Tree

## Description
A hierarchical data structure consisting of nodes connected by edges. Each tree has a root node, and every node has zero or more child nodes. Trees are non-linear and used to represent hierarchical relationships.

## Time Complexity
- Search: O(n) general tree, O(log n) balanced BST
- Insert: O(n) general tree, O(log n) balanced BST
- Delete: O(n) general tree, O(log n) balanced BST
- Traversal: O(n)

## Space Complexity
O(n) where n is the number of nodes

## Implementation

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []  # For general trees
        # For binary trees:
        # self.left = None
        # self.right = None
    
    def add_child(self, child_node):
        """Add a child to this node"""
        self.children.append(child_node)
    
    def __repr__(self):
        return f"TreeNode({self.data})"

# Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"Node({self.data})"

class BinaryTree:
    def __init__(self, root_data=None):
        self.root = BinaryTreeNode(root_data) if root_data else None
    
    def inorder_traversal(self, node):
        """Left -> Root -> Right"""
        if node is None:
            return []
        
        result = []
        result.extend(self.inorder_traversal(node.left))
        result.append(node.data)
        result.extend(self.inorder_traversal(node.right))
        return result
    
    def preorder_traversal(self, node):
        """Root -> Left -> Right"""
        if node is None:
            return []
        
        result = [node.data]
        result.extend(self.preorder_traversal(node.left))
        result.extend(self.preorder_traversal(node.right))
        return result
    
    def postorder_traversal(self, node):
        """Left -> Right -> Root"""
        if node is None:
            return []
        
        result = []
        result.extend(self.postorder_traversal(node.left))
        result.extend(self.postorder_traversal(node.right))
        result.append(node.data)
        return result
    
    def level_order_traversal(self):
        """Breadth-first traversal"""
        if not self.root:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    def height(self, node):
        """Calculate height of tree"""
        if node is None:
            return -1
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        return max(left_height, right_height) + 1
    
    def count_nodes(self, node):
        """Count total nodes"""
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)
    
    def search(self, node, value):
        """Search for a value in the tree"""
        if node is None:
            return False
        
        if node.data == value:
            return True
        
        return self.search(node.left, value) or self.search(node.right, value)

# Example usage
if __name__ == "__main__":
    # Create a binary tree
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    
    tree = BinaryTree(1)
    tree.root.left = BinaryTreeNode(2)
    tree.root.right = BinaryTreeNode(3)
    tree.root.left.left = BinaryTreeNode(4)
    tree.root.left.right = BinaryTreeNode(5)
    
    print("Inorder:", tree.inorder_traversal(tree.root))  # [4, 2, 5, 1, 3]
    print("Preorder:", tree.preorder_traversal(tree.root))  # [1, 2, 4, 5, 3]
    print("Postorder:", tree.postorder_traversal(tree.root))  # [4, 5, 2, 3, 1]
    print("Level-order:", tree.level_order_traversal())  # [1, 2, 3, 4, 5]
    print("Height:", tree.height(tree.root))  # 2
    print("Node count:", tree.count_nodes(tree.root))  # 5
```

## Key Points
- Root: topmost node with no parent
- Leaf: node with no children
- Height: longest path from root to leaf
- Depth: distance from root to a specific node
- Binary tree: each node has at most 2 children
- Recursive structure makes trees naturally suited for recursive algorithms

## Common Use Cases
- File systems (directory structure)
- DOM (Document Object Model) in web browsers
- Organization hierarchies
- Expression parsing (syntax trees)
- Decision trees in machine learning
- Database indexing (B-trees)
- Routing tables

## Tree Terminology
- **Root**: Top node
- **Parent**: Node with children
- **Child**: Node descended from another
- **Leaf**: Node with no children
- **Subtree**: Tree formed by a node and its descendants
- **Level**: Distance from root (root is level 0)
- **Height**: Longest path from node to leaf
- **Depth**: Distance from root to node

## Tree Traversal Types
- **Inorder** (Left-Root-Right): Gives sorted order in BST
- **Preorder** (Root-Left-Right): Used to create a copy of tree
- **Postorder** (Left-Right-Root): Used to delete tree
- **Level-order** (Breadth-first): Process nodes level by level

## Binary Tree Types
- **Full Binary Tree**: Every node has 0 or 2 children
- **Complete Binary Tree**: All levels filled except possibly last, filled left to right
- **Perfect Binary Tree**: All internal nodes have 2 children, all leaves at same level
- **Balanced Binary Tree**: Height difference of left and right subtrees ≤ 1

## Example Problems
1. Maximum Depth of Binary Tree (LeetCode #104)
2. Same Tree (LeetCode #100)
3. Invert Binary Tree (LeetCode #226)
4. Symmetric Tree (LeetCode #101)
5. Binary Tree Level Order Traversal (LeetCode #102)
6. Path Sum (LeetCode #112)
7. Lowest Common Ancestor (LeetCode #236)
8. Diameter of Binary Tree (LeetCode #543)
9. Serialize and Deserialize Binary Tree (LeetCode #297)

## Notes
- Many tree operations are naturally recursive
- Consider iterative approaches using stacks/queues for interviews
- Morris traversal allows O(1) space traversal
- Practice drawing trees while solving problems
- Understanding tree traversals is crucial for interview success