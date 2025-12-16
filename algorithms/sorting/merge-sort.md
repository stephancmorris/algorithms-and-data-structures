# Merge Sort

## Description
A stable divide-and-conquer sorting algorithm that divides array into halves, recursively sorts them, and merges the sorted halves. Guarantees O(n log n) performance in all cases.

## Time Complexity
- All cases: O(n log n)

## Space Complexity
O(n) for temporary arrays

## Implementation

```python
def merge_sort(arr):
    """Standard merge sort"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# In-place merge sort
def merge_sort_inplace(arr, left=0, right=None):
    """In-place version"""
    if right is None:
        right = len(arr) - 1
    
    if left < right:
        mid = (left + right) // 2
        merge_sort_inplace(arr, left, mid)
        merge_sort_inplace(arr, mid + 1, right)
        merge_inplace(arr, left, mid, right)
    
    return arr

def merge_inplace(arr, left, mid, right):
    """In-place merge using temporary array"""
    temp = arr[left:right+1]
    i = 0
    j = mid - left + 1
    k = left
    
    while i <= mid - left and j < len(temp):
        if temp[i] <= temp[j]:
            arr[k] = temp[i]
            i += 1
        else:
            arr[k] = temp[j]
            j += 1
        k += 1
    
    while i <= mid - left:
        arr[k] = temp[i]
        i += 1
        k += 1
    
    while j < len(temp):
        arr[k] = temp[j]
        j += 1
        k += 1

# Example
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Sorted:", merge_sort(arr))
```

## Key Points
- Stable sorting algorithm
- Predictable O(n log n) performance
- Requires O(n) extra space
- Divide and conquer approach
- Good for linked lists (O(1) space)

## Example Problems
1. Sort an Array (LeetCode #912)
2. Sort List (LeetCode #148) - merge sort for linked lists
3. Count of Smaller Numbers After Self (LeetCode #315)
4. Reverse Pairs (LeetCode #493)

## Notes
- Stable: preserves relative order of equal elements
- Guaranteed O(n log n) unlike quicksort
- Parallelizable - good for external sorting
- Preferred when stability matters