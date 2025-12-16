# Quick Sort

## Description
A divide-and-conquer sorting algorithm that picks a pivot element, partitions the array around it (smaller left, larger right), and recursively sorts the partitions. One of the fastest general-purpose sorting algorithms.

## Time Complexity
- Average: O(n log n)
- Worst: O(n²) - when pivot is always min/max
- Best: O(n log n)

## Space Complexity
- O(log n) - recursion stack (in-place sorting)
- O(n) worst case recursion stack

## Implementation

```python
def quick_sort(arr):
    """Quick sort with last element as pivot"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

def quick_sort_inplace(arr, low=0, high=None):
    """In-place quick sort"""
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, high)
    
    return arr

def partition(arr, low, high):
    """Lomuto partition scheme"""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Hoare partition (more efficient)
def partition_hoare(arr, low, high):
    """Hoare partition scheme"""
    pivot = arr[low]
    i = low - 1
    j = high + 1
    
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        
        j -= 1
        while arr[j] > pivot:
            j -= 1
        
        if i >= j:
            return j
        
        arr[i], arr[j] = arr[j], arr[i]

# 3-way partitioning (for duplicates)
def quick_sort_3way(arr, low=0, high=None):
    """3-way quick sort for arrays with duplicates"""
    if high is None:
        high = len(arr) - 1
    
    if low >= high:
        return arr
    
    lt, gt = partition_3way(arr, low, high)
    quick_sort_3way(arr, low, lt - 1)
    quick_sort_3way(arr, gt + 1, high)
    
    return arr

def partition_3way(arr, low, high):
    """3-way partition: < pivot | = pivot | > pivot"""
    pivot = arr[low]
    i = low
    lt = low
    gt = high
    
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

# Randomized quick sort
import random

def quick_sort_random(arr, low=0, high=None):
    """Quick sort with random pivot"""
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_index = partition_random(arr, low, high)
        quick_sort_random(arr, low, pivot_index - 1)
        quick_sort_random(arr, pivot_index + 1, high)
    
    return arr

def partition_random(arr, low, high):
    """Random pivot selection"""
    random_pivot = random.randint(low, high)
    arr[random_pivot], arr[high] = arr[high], arr[random_pivot]
    return partition(arr, low, high)

# Example
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", arr)
    print("Sorted:", quick_sort(arr.copy()))
    
    arr2 = [3, 7, 8, 5, 2, 1, 9, 5, 4]
    quick_sort_inplace(arr2)
    print("In-place sorted:", arr2)
```

## Key Points
- Divide and conquer algorithm
- In-place sorting (no extra array needed)
- Not stable (doesn't preserve relative order)
- Pivot selection crucial for performance
- Cache-friendly due to sequential access

## Optimizations
- Random pivot selection
- Median-of-three pivot
- 3-way partitioning for duplicates
- Insertion sort for small subarrays
- Tail recursion optimization

## Example Problems
1. Sort an Array (LeetCode #912)
2. Kth Largest Element (LeetCode #215) - uses partition
3. Sort Colors (LeetCode #75) - Dutch national flag
4. Wiggle Sort II (LeetCode #324)

## Notes
- Average O(n log n) makes it very fast in practice
- Randomization avoids worst case
- Use 3-way partition for many duplicates
- Typically faster than merge sort due to cache locality