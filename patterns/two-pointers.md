# Two Pointers

## Description
A technique using two pointers to iterate through a data structure. Pointers can move toward each other, in the same direction, or at different speeds. Often reduces O(n²) to O(n).

## Time Complexity
Typically O(n) for single pass

## Space Complexity
O(1) - constant extra space

## Implementation

```python
# Opposite Direction (converging)
def two_sum_sorted(arr, target):
    """Find pair that sums to target in sorted array"""
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return [-1, -1]

# Same Direction (fast/slow)
def remove_duplicates(arr):
    """Remove duplicates in-place from sorted array"""
    if not arr:
        return 0
    
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    
    return slow + 1

# Different Speeds (cycle detection)
def has_cycle(head):
    """Detect cycle in linked list"""
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False

# Three Pointers
def three_sum(nums):
    """Find all triplets that sum to zero"""
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result

# Partition (Dutch National Flag)
def sort_colors(nums):
    """Sort 0s, 1s, 2s in-place"""
    left = 0  # Next position for 0
    right = len(nums) - 1  # Next position for 2
    i = 0
    
    while i <= right:
        if nums[i] == 0:
            nums[left], nums[i] = nums[i], nums[left]
            left += 1
            i += 1
        elif nums[i] == 2:
            nums[right], nums[i] = nums[i], nums[right]
            right -= 1
        else:
            i += 1

# Container With Most Water
def max_area(height):
    """Find max water container area"""
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        width = right - left
        current_area = width * min(height[left], height[right])
        max_water = max(max_water, current_area)
        
        # Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

# Palindrome Check
def is_palindrome(s):
    """Check if string is palindrome"""
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Example
if __name__ == "__main__":
    print("Two sum:", two_sum_sorted([1, 2, 3, 4, 6], 6))
    print("Three sum:", three_sum([-1, 0, 1, 2, -1, -4]))
```

## Common Patterns

### Pattern 1: Opposite Direction
Start from both ends, move toward center.
- Two Sum (sorted)
- Container With Most Water
- Valid Palindrome

### Pattern 2: Same Direction (Fast/Slow)
Both start at beginning, move at different speeds.
- Remove Duplicates
- Move Zeroes
- Cycle Detection

### Pattern 3: Three Pointers
Extension for problems needing three elements.
- Three Sum
- Sort Colors
- Dutch National Flag

## Example Problems
1. Two Sum II (LeetCode #167)
2. 3Sum (LeetCode #15)
3. Container With Most Water (LeetCode #11)
4. Remove Duplicates (LeetCode #26)
5. Valid Palindrome (LeetCode #125)
6. Linked List Cycle (LeetCode #141)
7. Sort Colors (LeetCode #75)
8. Trapping Rain Water (LeetCode #42)

## Notes
- Often reduces space from O(n) to O(1)
- Works well on sorted arrays
- Can replace hash maps in some cases
- Consider sorting first if not sorted