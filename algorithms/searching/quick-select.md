# Quick Select

## Description
An efficient selection algorithm to find the kth smallest/largest element in an unordered array. Based on the QuickSort partition algorithm but only recurses into one partition. On average, faster than sorting the entire array.

## Time Complexity
- Average case: O(n)
- Worst case: O(n²) - with bad pivot selection
- Best case: O(n)
- With randomization: O(n) expected

## Space Complexity
- Iterative: O(1)
- Recursive: O(log n) average (call stack)

## Implementation

```python
import random

# Standard Quick Select
def quick_select(arr, k):
    """
    Find kth smallest element (0-indexed)
    arr: input array
    k: index of element to find (0 = smallest)
    """
    def partition(left, right, pivot_index):
        """Partition array around pivot"""
        pivot_value = arr[pivot_index]
        
        # Move pivot to end
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        
        # Move all smaller elements to left
        store_index = left
        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        
        # Move pivot to final position
        arr[right], arr[store_index] = arr[store_index], arr[right]
        
        return store_index
    
    def select(left, right, k):
        """Recursive selection"""
        if left == right:
            return arr[left]
        
        # Choose random pivot for better average performance
        pivot_index = random.randint(left, right)
        
        # Partition and get pivot position
        pivot_index = partition(left, right, pivot_index)
        
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return select(left, pivot_index - 1, k)
        else:
            return select(pivot_index + 1, right, k)
    
    return select(0, len(arr) - 1, k)

# Iterative Quick Select
def quick_select_iterative(arr, k):
    """Iterative version to avoid recursion"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # Choose random pivot
        pivot_index = random.randint(left, right)
        
        # Partition
        pivot_value = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        
        store_index = left
        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        
        arr[right], arr[store_index] = arr[store_index], arr[right]
        pivot_index = store_index
        
        # Check if we found kth element
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            right = pivot_index - 1
        else:
            left = pivot_index + 1
    
    return arr[k]

# Find kth largest (instead of kth smallest)
def find_kth_largest(arr, k):
    """
    Find kth largest element (1-indexed)
    Example: k=1 means largest element
    """
    # Convert to kth smallest problem
    return quick_select(arr.copy(), len(arr) - k)

# Three-way partition (for arrays with duplicates)
def quick_select_three_way(arr, k):
    """
    Quick select with three-way partitioning
    Handles duplicates efficiently
    """
    def partition_three_way(left, right):
        """
        Three-way partition:
        [< pivot | = pivot | > pivot]
        Returns (lt, gt) where:
        - Elements < pivot are in [left, lt)
        - Elements = pivot are in [lt, gt]
        - Elements > pivot are in (gt, right]
        """
        pivot = arr[random.randint(left, right)]
        i = left
        lt = left  # Next position for elements < pivot
        gt = right  # Next position for elements > pivot
        
        while i <= gt:
            if arr[i] < pivot:
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else:
                i += 1
        
        return lt, gt
    
    def select(left, right, k):
        if left >= right:
            return arr[left]
        
        lt, gt = partition_three_way(left, right)
        
        if k < lt:
            return select(left, lt - 1, k)
        elif k > gt:
            return select(gt + 1, right, k)
        else:
            return arr[k]
    
    return select(0, len(arr) - 1, k)

# Median finding
def find_median(arr):
    """Find median using quick select"""
    n = len(arr)
    if n % 2 == 1:
        return quick_select(arr.copy(), n // 2)
    else:
        # Average of two middle elements
        arr_copy = arr.copy()
        return (quick_select(arr_copy, n // 2 - 1) + 
                quick_select(arr_copy, n // 2)) / 2

# Top K elements
def find_top_k(arr, k):
    """
    Find k largest elements using quick select
    Returns array of k largest elements (not necessarily sorted)
    """
    n = len(arr)
    arr_copy = arr.copy()
    
    # Find (n-k)th smallest element
    quick_select(arr_copy, n - k)
    
    # All elements from index n-k onwards are the k largest
    return arr_copy[n - k:]

# Median of medians (deterministic O(n))
def median_of_medians(arr, k):
    """
    Deterministic O(n) selection using median of medians
    for pivot selection. More complex but guarantees O(n).
    """
    def select_pivot(arr, left, right):
        """Select good pivot using median of medians"""
        if right - left < 5:
            return sorted(arr[left:right + 1])[len(arr[left:right + 1]) // 2]
        
        medians = []
        for i in range(left, right + 1, 5):
            sub_right = min(i + 4, right)
            median = sorted(arr[i:sub_right + 1])[(sub_right - i + 1) // 2]
            medians.append(median)
        
        return median_of_medians(medians, len(medians) // 2)
    
    def partition(left, right, pivot_value):
        # Find pivot value in array
        for i in range(left, right + 1):
            if arr[i] == pivot_value:
                arr[i], arr[right] = arr[right], arr[i]
                break
        
        # Standard partition
        store_index = left
        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        
        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index
    
    def select(left, right, k):
        if left == right:
            return arr[left]
        
        pivot_value = select_pivot(arr, left, right)
        pivot_index = partition(left, right, pivot_value)
        
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return select(left, pivot_index - 1, k)
        else:
            return select(pivot_index + 1, right, k)
    
    return select(0, len(arr) - 1, k)

# Example usage
if __name__ == "__main__":
    arr = [3, 2, 1, 5, 6, 4]
    
    # Find kth smallest
    print("2nd smallest:", quick_select(arr.copy(), 1))  # 2
    print("4th smallest:", quick_select(arr.copy(), 3))  # 4
    
    # Find kth largest
    print("2nd largest:", find_kth_largest(arr.copy(), 2))  # 5
    print("1st largest:", find_kth_largest(arr.copy(), 1))  # 6
    
    # Find median
    print("Median:", find_median(arr))  # 3.5
    
    # Top k elements
    print("Top 3:", find_top_k(arr, 3))  # [5, 6, 4] (not sorted)
    
    # Array with duplicates
    arr_dup = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    print("3rd smallest (with dups):", quick_select_three_way(arr_dup.copy(), 2))
```

## Key Points
- Based on QuickSort partition but only recurses on one side
- Average O(n) - much faster than sorting O(n log n)
- Randomized pivot selection improves average case
- Modifies input array (use copy if needed)
- Three-way partition handles duplicates efficiently
- Can be made deterministic with median of medians

## Common Use Cases
- Finding kth smallest/largest element
- Finding median
- Top K problems
- Selection in streaming data
- Percentile calculations
- Order statistics

## Quick Select vs Other Approaches

### vs. Sorting
- Quick Select: O(n) average
- Sorting: O(n log n)
- Use Quick Select when you only need kth element

### vs. Heap
- Quick Select: O(n) average, modifies array
- Heap: O(n log k), preserves array
- Use heap for multiple queries or small k

### vs. Median of Medians
- Quick Select: O(n) average, O(n²) worst
- Median of Medians: O(n) worst case guaranteed
- Median of medians is more complex

## Common Patterns

### Pattern 1: Kth Largest/Smallest
Convert between kth largest and kth smallest.

### Pattern 2: Top K Elements
Partition at (n-k)th position.

### Pattern 3: Median Finding
Find element at position n/2.

## Example Problems
1. Kth Largest Element in Array (LeetCode #215)
2. Top K Frequent Elements (LeetCode #347) - can use quick select on frequencies
3. K Closest Points to Origin (LeetCode #973)
4. Wiggle Sort II (LeetCode #324)
5. Find K Pairs with Smallest Sums (LeetCode #373)
6. Kth Smallest Element in Sorted Matrix (LeetCode #378)

## Notes
- Always use randomized pivot to avoid O(n²) worst case
- For production, consider median of medians for guaranteed O(n)
- Three-way partition is crucial for arrays with many duplicates
- Quick select modifies the array - use copy if original needed
- For multiple queries, consider building heap or sorting
- Common bug: off-by-one errors with k (0-indexed vs 1-indexed)
- In interviews, clarify if k is 0-indexed or 1-indexed
- Can be implemented iteratively to save stack space