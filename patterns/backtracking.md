# Backtracking

## Description
A general algorithmic technique that incrementally builds candidates to solutions and abandons ("backtracks") a candidate as soon as it determines the candidate cannot lead to a valid solution. Essentially a depth-first search with pruning.

## Time Complexity
Typically O(b^d) where b = branching factor, d = depth
Varies greatly based on problem and pruning

## Space Complexity
O(d) for recursion stack where d = maximum depth

## Implementation

```python
# Template for backtracking
def backtrack(candidates, target, path, result):
    """
    General backtracking template
    candidates: available choices
    target: goal condition
    path: current solution being built
    result: collection of all solutions
    """
    # Base case: found valid solution
    if is_solution(path, target):
        result.append(path.copy())  # Must copy!
        return
    
    # Try each candidate
    for candidate in candidates:
        # Check if candidate is valid
        if is_valid(candidate, path):
            # Make choice
            path.append(candidate)
            
            # Recurse
            backtrack(candidates, target, path, result)
            
            # Undo choice (backtrack)
            path.pop()

# Permutations
def permute(nums):
    """Generate all permutations"""
    result = []
    
    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path.copy())
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            
            # Make choice
            path.append(nums[i])
            used[i] = True
            
            # Recurse
            backtrack(path, used)
            
            # Undo
            path.pop()
            used[i] = False
    
    backtrack([], [False] * len(nums))
    return result

# Combinations
def combine(n, k):
    """Generate combinations of k numbers from 1 to n"""
    result = []
    
    def backtrack(start, path):
        if len(path) == k:
            result.append(path.copy())
            return
        
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)  # Use next number
            path.pop()
    
    backtrack(1, [])
    return result

# Subsets
def subsets(nums):
    """Generate all subsets (power set)"""
    result = []
    
    def backtrack(start, path):
        result.append(path.copy())
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result

# N-Queens
def solve_n_queens(n):
    """Place n queens on n×n board"""
    result = []
    board = [['.'] * n for _ in range(n)]
    
    def is_safe(row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # Check anti-diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True
    
    def backtrack(row):
        if row == n:
            result.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'
    
    backtrack(0)
    return result

# Sudoku Solver
def solve_sudoku(board):
    """Solve sudoku puzzle"""
    def is_valid(row, col, num):
        # Check row
        if num in board[row]:
            return False
        
        # Check column
        if num in [board[i][col] for i in range(9)]:
            return False
        
        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return False
        
        return True
    
    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in '123456789':
                        if is_valid(i, j, num):
                            board[i][j] = num
                            if backtrack():
                                return True
                            board[i][j] = '.'
                    return False
        return True
    
    backtrack()
    return board

# Word Search
def exist(board, word):
    """Find if word exists in board"""
    rows, cols = len(board), len(board[0])
    
    def backtrack(row, col, index):
        if index == len(word):
            return True
        
        if (row < 0 or row >= rows or col < 0 or col >= cols or
            board[row][col] != word[index]):
            return False
        
        # Mark as visited
        temp = board[row][col]
        board[row][col] = '#'
        
        # Explore all directions
        found = (backtrack(row + 1, col, index + 1) or
                backtrack(row - 1, col, index + 1) or
                backtrack(row, col + 1, index + 1) or
                backtrack(row, col - 1, index + 1))
        
        # Restore
        board[row][col] = temp
        
        return found
    
    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0):
                return True
    return False

# Example
if __name__ == "__main__":
    print("Permutations of [1,2,3]:", permute([1, 2, 3]))
    print("Combinations C(4,2):", combine(4, 2))
    print("Subsets of [1,2]:", subsets([1, 2]))
```

## Key Points
- Build solution incrementally
- Backtrack when constraint violated
- Prune invalid branches early
- DFS with constraint checking
- Always undo choices (restore state)

## When to Use
- All possible solutions needed
- Constraint satisfaction problems
- Combinatorial optimization
- NP-complete problems

## Common Patterns
1. **Choice/Explore/Unchoose**: Make choice, recurse, undo
2. **Path building**: Incrementally build solution path
3. **Pruning**: Skip invalid branches early
4. **State restoration**: Undo changes after recursion

## Example Problems
1. Permutations (LeetCode #46)
2. Combinations (LeetCode #77)
3. Subsets (LeetCode #78)
4. N-Queens (LeetCode #51)
5. Sudoku Solver (LeetCode #37)
6. Word Search (LeetCode #79)
7. Combination Sum (LeetCode #39)
8. Palindrome Partitioning (LeetCode #131)
9. Letter Combinations (LeetCode #17)
10. Generate Parentheses (LeetCode #22)

## Notes
- Always copy result before adding to answer
- Remember to restore state after recursion
- Early pruning dramatically improves performance
- Often exponential time complexity
- Consider iterative alternatives for some problems