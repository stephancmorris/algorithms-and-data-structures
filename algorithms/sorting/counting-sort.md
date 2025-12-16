# Counting Sort

## Description
A non-comparison based sorting algorithm that counts occurrences of each element and uses arithmetic to determine positions. Works well when range of elements (k) is not much larger than number of elements (n).

## Time Complexity
O(n + k) where n = number of elements, k = range

## Space Complexity
O(n + k)

## Implementation

```python
def counting_sort(arr):
    """
    Standard counting sort for non-negative integers
    """
    if not arr:
        return arr
    
    # Find range
    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1
    
    # Count occurrences
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1
    
    # Build output
    output = []
    for i, freq in enumerate(count):
        output.extend([i + min_val] * freq)
    
    return output

def counting_sort_stable(arr):
    """
    Stable version using cumulative counts
    """
    if not arr:
        return arr
    
    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1
    
    # Count occurrences
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1
    
    # Convert to cumulative counts
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Build output in reverse to maintain stability
    output = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        index = count[num - min_val] - 1
        output[index] = num
        count[num - min_val] -= 1
    
    return output

# Example
if __name__ == "__main__":
    arr = [4, 2, 2, 8, 3, 3, 1]
    print("Original:", arr)
    print("Sorted:", counting_sort(arr))
    print("Stable:", counting_sort_stable(arr))
```

## Key Points
- Non-comparison based
- O(n + k) time complexity
- Only works for integers or items that can be mapped to integers
- Stable if implemented correctly
- Efficient when k = O(n)

## When to Use
- Small range of integers
- Need linear time sorting
- Stability required
- As subroutine in radix sort

## Example Problems
1. Sort Colors (LeetCode #75) - counting sort application
2. Maximum Gap (LeetCode #164) - can use counting/radix sort
3. Sort Characters By Frequency (LeetCode #451)

## Notes
- Not comparison-based like quicksort/mergesort
- Inefficient if range >> n
- Can adapt for negative numbers
- Foundation for radix sort