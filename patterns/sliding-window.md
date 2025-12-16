# Sliding Window

## Description
A technique for problems involving subarrays/substrings. Maintains a window of elements and slides it across the data structure. Two variants: fixed-size and variable-size windows.

## Time Complexity
O(n) - each element visited at most twice

## Space Complexity
O(1) to O(k) depending on tracking needs

## Implementation

```python
from collections import defaultdict, Counter

# Fixed-Size Window
def max_sum_subarray(arr, k):
    """Maximum sum of subarray of size k"""
    if len(arr) < k:
        return None
    
    # Initial window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide window
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Variable-Size Window - Longest
def longest_substring_k_distinct(s, k):
    """Longest substring with at most k distinct characters"""
    char_count = {}
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        # Expand window
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Shrink window while invalid
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len

# Variable-Size Window - Shortest
def min_subarray_sum(arr, target):
    """Minimum length subarray with sum >= target"""
    left = 0
    current_sum = 0
    min_len = float('inf')
    
    for right in range(len(arr)):
        current_sum += arr[right]
        
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= arr[left]
            left += 1
    
    return min_len if min_len != float('inf') else 0

# Longest Substring Without Repeating
def length_of_longest_substring(s):
    """Longest substring without repeating characters"""
    char_index = {}
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1
        
        char_index[s[right]] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len

# Find All Anagrams
def find_anagrams(s, p):
    """Find starting indices of anagrams of p in s"""
    if len(p) > len(s):
        return []
    
    p_count = Counter(p)
    window_count = Counter()
    result = []
    
    for right in range(len(s)):
        # Add character to window
        window_count[s[right]] += 1
        
        # Remove leftmost character if window too large
        if right >= len(p):
            left_char = s[right - len(p)]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
        
        # Check if window is anagram
        if window_count == p_count:
            result.append(right - len(p) + 1)
    
    return result

# Permutation in String
def check_inclusion(s1, s2):
    """Check if s2 contains permutation of s1"""
    if len(s1) > len(s2):
        return False
    
    s1_count = Counter(s1)
    window_count = Counter(s2[:len(s1)])
    
    if s1_count == window_count:
        return True
    
    for i in range(len(s1), len(s2)):
        # Add new character
        window_count[s2[i]] += 1
        
        # Remove old character
        left_char = s2[i - len(s1)]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]
        
        if s1_count == window_count:
            return True
    
    return False

# Maximum of Sliding Window
def max_sliding_window(nums, k):
    """Max of each window of size k"""
    from collections import deque
    
    result = []
    window = deque()  # Stores indices
    
    for i in range(len(nums)):
        # Remove indices outside window
        while window and window[0] < i - k + 1:
            window.popleft()
        
        # Remove smaller elements
        while window and nums[window[-1]] < nums[i]:
            window.pop()
        
        window.append(i)
        
        # Add to result if window is full
        if i >= k - 1:
            result.append(nums[window[0]])
    
    return result

# Example
if __name__ == "__main__":
    print("Max sum k=3:", max_sum_subarray([2, 1, 5, 1, 3, 2], 3))
    print("Longest k=2:", longest_substring_k_distinct("eceba", 2))
    print("Find anagrams:", find_anagrams("cbaebabacd", "abc"))
```

## Common Patterns

### Pattern 1: Fixed Window
Window size is constant, slide one element at a time.

### Pattern 2: Variable Window (Longest)
Expand window until invalid, track maximum size.

### Pattern 3: Variable Window (Shortest)
Expand until valid, shrink while valid.

### Pattern 4: Window with Counter
Track frequency of elements in window.

## Example Problems
1. Maximum Average Subarray (LeetCode #643)
2. Longest Substring Without Repeating (LeetCode #3)
3. Minimum Window Substring (LeetCode #76)
4. Find All Anagrams (LeetCode #438)
5. Longest Repeating Character Replacement (LeetCode #424)
6. Sliding Window Maximum (LeetCode #239)
7. Permutation in String (LeetCode #567)
8. Fruit Into Baskets (LeetCode #904)

## Notes
- Use for contiguous sequence problems
- HashMap/Counter often needed for tracking
- Two pointers (left, right) define window
- Deque useful for window max/min