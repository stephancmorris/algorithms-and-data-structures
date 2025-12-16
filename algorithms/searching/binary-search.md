# Binary Search

## Description
An efficient search algorithm for sorted arrays that repeatedly divides the search interval in half. Compares the target value to the middle element and eliminates half of the remaining elements each iteration.

## Time Complexity
- Search: O(log n)
- Worst case: O(log n)
- Best case: O(1) - target is middle element

## Space Complexity
- Iterative: O(1)
- Recursive: O(log n) - call stack

## Implementation

```python
# Standard Binary Search - Iterative
def binary_search(arr, target):
    """
    Search for target in sorted array
    Returns index if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    
    return -1  # Not found

# Recursive Binary Search
def binary_search_recursive(arr, target, left=0, right=None):
    """Recursive implementation"""
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Find first occurrence
def find_first(arr, target):
    """Find leftmost (first) occurrence of target"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

# Find last occurrence
def find_last(arr, target):
    """Find rightmost (last) occurrence of target"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

# Lower bound (first element >= target)
def lower_bound(arr, target):
    """
    Find index of first element >= target
    If no such element exists, return len(arr)
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left

# Upper bound (first element > target)
def upper_bound(arr, target):
    """
    Find index of first element > target
    If no such element exists, return len(arr)
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    
    return left

# Search in rotated sorted array
def search_rotated(arr, target):
    """Search in rotated sorted array"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        
        # Determine which half is sorted
        if arr[left] <= arr[mid]:  # Left half is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# Find peak element
def find_peak(arr):
    """
    Find a peak element (greater than neighbors)
    Works for any array, not necessarily sorted
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] > arr[mid + 1]:
            # Peak is in left half (including mid)
            right = mid
        else:
            # Peak is in right half
            left = mid + 1
    
    return left

# Find minimum in rotated sorted array
def find_min_rotated(arr):
    """Find minimum element in rotated sorted array"""
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] > arr[right]:
            # Minimum is in right half
            left = mid + 1
        else:
            # Minimum is in left half (including mid)
            right = mid
    
    return arr[left]

# Square root (integer)
def sqrt(x):
    """Find integer square root using binary search"""
    if x < 2:
        return x
    
    left, right = 1, x // 2
    
    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right  # Return floor(sqrt(x))

# Binary search on answer
def min_capacity(weights, days):
    """
    Find minimum ship capacity to ship packages in given days
    Example of "binary search on answer" pattern
    """
    def can_ship(capacity):
        """Check if we can ship with given capacity"""
        current_weight = 0
        days_needed = 1
        
        for weight in weights:
            if current_weight + weight > capacity:
                days_needed += 1
                current_weight = weight
            else:
                current_weight += weight
        
        return days_needed <= days
    
    left = max(weights)  # Minimum possible capacity
    right = sum(weights)  # Maximum possible capacity
    
    while left < right:
        mid = left + (right - left) // 2
        
        if can_ship(mid):
            right = mid  # Try smaller capacity
        else:
            left = mid + 1  # Need larger capacity
    
    return left

# Binary search in 2D matrix
def search_matrix(matrix, target):
    """
    Search in 2D matrix where:
    - Each row is sorted
    - First element of each row > last element of previous row
    """
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        # Convert 1D index to 2D
        row = mid // cols
        col = mid % cols
        mid_value = matrix[row][col]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

# Example usage
if __name__ == "__main__":
    # Standard search
    arr = [1, 3, 5, 7, 9, 11, 13]
    print("Search 7:", binary_search(arr, 7))  # 3
    print("Search 6:", binary_search(arr, 6))  # -1
    
    # First/last occurrence
    arr_dup = [1, 2, 2, 2, 3, 4, 5]
    print("First 2:", find_first(arr_dup, 2))  # 1
    print("Last 2:", find_last(arr_dup, 2))   # 3
    
    # Bounds
    print("Lower bound 2:", lower_bound(arr_dup, 2))  # 1
    print("Upper bound 2:", upper_bound(arr_dup, 2))  # 4
    
    # Rotated array
    rotated = [4, 5, 6, 7, 0, 1, 2]
    print("Search 0 in rotated:", search_rotated(rotated, 0))  # 4
    
    # Peak element
    peak_arr = [1, 2, 3, 1]
    print("Peak index:", find_peak(peak_arr))  # 2
    
    # Square root
    print("sqrt(8):", sqrt(8))  # 2
    print("sqrt(16):", sqrt(16))  # 4
```

## Key Points
- Requires sorted array
- Divides search space in half each iteration
- Logarithmic time complexity
- Be careful with mid calculation to avoid overflow
- Watch for off-by-one errors with left/right boundaries
- Can be applied to non-array problems (answer searching)

## Common Use Cases
- Searching in sorted arrays
- Finding boundaries (first/last occurrence)
- Finding insertion position
- Optimization problems (minimize/maximize with constraint)
- Square root calculation
- Searching in rotated sorted arrays
- Peak finding

## Binary Search Variations

### Standard Binary Search
Find exact match in sorted array.

### First/Last Occurrence
Find leftmost or rightmost occurrence of target.

### Lower/Upper Bound
Find first element >= or > target.

### Search on Answer
Binary search on the answer space (capacity, speed, etc.).

### Rotated Arrays
Handle sorted arrays that have been rotated.

### 2D Binary Search
Treat 2D matrix as 1D sorted array.

## Common Patterns

### Pattern 1: Exact Match
```python
while left <= right:
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

### Pattern 2: Lower Bound
```python
while left < right:
    mid = left + (right - left) // 2
    if arr[mid] < target:
        left = mid + 1
    else:
        right = mid
```

### Pattern 3: Binary Search on Answer
```python
while left < right:
    mid = left + (right - left) // 2
    if is_feasible(mid):
        right = mid  # or left = mid + 1
    else:
        left = mid + 1  # or right = mid - 1
```

## Example Problems
1. Binary Search (LeetCode #704)
2. Search Insert Position (LeetCode #35)
3. Find First and Last Position (LeetCode #34)
4. Search in Rotated Sorted Array (LeetCode #33)
5. Find Minimum in Rotated Sorted Array (LeetCode #153)
6. Find Peak Element (LeetCode #162)
7. Sqrt(x) (LeetCode #69)
8. Valid Perfect Square (LeetCode #367)
9. Search a 2D Matrix (LeetCode #74)
10. Koko Eating Bananas (LeetCode #875)
11. Capacity To Ship Packages (LeetCode #1011)
12. Median of Two Sorted Arrays (LeetCode #4)

## Notes
- Use `mid = left + (right - left) // 2` to avoid integer overflow
- Be careful with `left <= right` vs `left < right`
- For finding boundaries, adjust search after finding target
- "Binary search on answer" pattern: search answer space instead of array
- Always verify array is sorted before applying binary search
- Can binary search on implicit sequences (not just arrays)
- Practice both iterative and recursive implementations
- Common bug: infinite loop when mid calculation is wrong