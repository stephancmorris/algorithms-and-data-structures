# Divide and Conquer

## Description
Breaks problem into smaller subproblems, solves them recursively, and combines results. Three steps: Divide, Conquer, Combine. Used in merge sort, quick sort, binary search, and many efficient algorithms.

## Time Complexity
Often O(n log n) but varies by problem
T(n) = aT(n/b) + f(n) - use Master Theorem

## Space Complexity
O(log n) to O(n) depending on recursion depth

## Implementation

```python
# Merge Sort (classic example)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Conquer & Combine
    return merge(left, right)

def merge(left, right):
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

# Maximum Subarray (Kadane's with D&C alternative)
def max_subarray_dc(arr, left, right):
    """Divide and conquer approach"""
    if left == right:
        return arr[left]
    
    mid = (left + right) // 2
    
    # Conquer
    left_sum = max_subarray_dc(arr, left, mid)
    right_sum = max_subarray_dc(arr, mid + 1, right)
    cross_sum = max_crossing_sum(arr, left, mid, right)
    
    # Combine
    return max(left_sum, right_sum, cross_sum)

def max_crossing_sum(arr, left, mid, right):
    """Find max sum crossing the midpoint"""
    left_sum = float('-inf')
    total = 0
    for i in range(mid, left - 1, -1):
        total += arr[i]
        left_sum = max(left_sum, total)
    
    right_sum = float('-inf')
    total = 0
    for i in range(mid + 1, right + 1):
        total += arr[i]
        right_sum = max(right_sum, total)
    
    return left_sum + right_sum

# Count Inversions
def count_inversions(arr):
    """Count pairs (i,j) where i<j and arr[i]>arr[j]"""
    def merge_count(arr, temp, left, mid, right):
        i = left
        j = mid + 1
        k = left
        inv_count = 0
        
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1
        
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
        
        for i in range(left, right + 1):
            arr[i] = temp[i]
        
        return inv_count
    
    def merge_sort_count(arr, temp, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            inv_count += merge_sort_count(arr, temp, left, mid)
            inv_count += merge_sort_count(arr, temp, mid + 1, right)
            inv_count += merge_count(arr, temp, left, mid, right)
        return inv_count
    
    n = len(arr)
    temp = [0] * n
    return merge_sort_count(arr, temp, 0, n - 1)

# Closest Pair of Points
def closest_pair(points):
    """Find closest pair of points in 2D"""
    def distance(p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
    
    def brute_force(points):
        min_dist = float('inf')
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                min_dist = min(min_dist, distance(points[i], points[j]))
        return min_dist
    
    def strip_closest(strip, d):
        min_dist = d
        strip.sort(key=lambda p: p[1])
        
        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and (strip[j][1] - strip[i][1]) < min_dist:
                min_dist = min(min_dist, distance(strip[i], strip[j]))
                j += 1
        
        return min_dist
    
    def closest_util(px, py):
        if len(px) <= 3:
            return brute_force(px)
        
        mid = len(px) // 2
        midpoint = px[mid]
        
        pyl = [p for p in py if p[0] <= midpoint[0]]
        pyr = [p for p in py if p[0] > midpoint[0]]
        
        dl = closest_util(px[:mid], pyl)
        dr = closest_util(px[mid:], pyr)
        
        d = min(dl, dr)
        
        strip = [p for p in py if abs(p[0] - midpoint[0]) < d]
        
        return min(d, strip_closest(strip, d))
    
    px = sorted(points, key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])
    return closest_util(px, py)

# Matrix Multiplication (Strassen's)
# Power(x, n)
def power(x, n):
    """Calculate x^n using divide and conquer"""
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n
    
    if n % 2 == 0:
        half = power(x, n // 2)
        return half * half
    else:
        half = power(x, n // 2)
        return half * half * x

# Example
if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Sorted:", merge_sort(arr))
    print("Inversions:", count_inversions([2, 4, 1, 3, 5]))
    print("Power:", power(2, 10))
```

## Key Points
- Divide into smaller subproblems
- Solve subproblems recursively
- Combine solutions
- Base case crucial
- Often logarithmic depth

## Example Problems
1. Merge Sort (sorting)
2. Quick Sort (sorting)
3. Binary Search (searching)
4. Maximum Subarray (LeetCode #53)
5. Merge k Sorted Lists (LeetCode #23)
6. Count of Smaller Numbers After Self (LeetCode #315)
7. Reverse Pairs (LeetCode #493)
8. Pow(x, n) (LeetCode #50)

## Notes
- Master Theorem for analyzing complexity
- Often reduces O(n²) to O(n log n)
- Recursive overhead to consider
- Base case handles small inputs
EOF

cat > /mnt/user-data/outputs/algorithms-repo/patterns/reservoir-sampling.md << 'EOF'
# Reservoir Sampling

## Description
An algorithm for randomly sampling k items from a stream of unknown size n. Each item has equal probability k/n of being selected. Useful when you can't store all items in memory or don't know the total count upfront.

## Time Complexity
O(n) - single pass through stream

## Space Complexity
O(k) - stores k samples

## Implementation

```python
import random

# Basic Reservoir Sampling
def reservoir_sample(stream, k):
    """
    Sample k items from stream with uniform probability
    stream: iterator/generator of items
    k: number of samples
    Returns: list of k samples
    """
    reservoir = []
    
    for i, item in enumerate(stream):
        if i < k:
            # Fill reservoir
            reservoir.append(item)
        else:
            # Random index from 0 to i
            j = random.randint(0, i)
            
            # Replace element with decreasing probability
            if j < k:
                reservoir[j] = item
    
    return reservoir

# Single Element Sampling
def random_pick(stream):
    """
    Pick one random element from stream
    Each element has equal 1/n probability
    """
    result = None
    
    for i, item in enumerate(stream):
        # Pick current item with probability 1/(i+1)
        if random.randint(0, i) == 0:
            result = item
    
    return result

# Weighted Reservoir Sampling
def weighted_reservoir_sample(stream, k):
    """
    Sample k items based on weights
    stream: iterator of (item, weight) tuples
    """
    import heapq
    
    reservoir = []
    
    for item, weight in stream:
        # Generate key: uniform^(1/weight)
        key = random.random() ** (1.0 / weight)
        
        if len(reservoir) < k:
            heapq.heappush(reservoir, (key, item))
        elif key > reservoir[0][0]:
            heapq.heapreplace(reservoir, (key, item))
    
    return [item for key, item in reservoir]

# Linked List Random Node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedListRandom:
    """
    LeetCode #382: Linked List Random Node
    """
    def __init__(self, head):
        self.head = head
    
    def getRandom(self):
        """Get random node value"""
        result = None
        current = self.head
        i = 0
        
        while current:
            # Reservoir sampling with k=1
            if random.randint(0, i) == 0:
                result = current.val
            current = current.next
            i += 1
        
        return result

# Random Pick Index
class RandomPickIndex:
    """
    LeetCode #398: Pick random index of target
    """
    def __init__(self, nums):
        self.nums = nums
    
    def pick(self, target):
        """Pick random index where nums[i] == target"""
        count = 0
        result = -1
        
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                # Pick with probability 1/count
                if random.randint(1, count) == 1:
                    result = i
        
        return result

# Sample from Infinite Stream
def sample_infinite_stream(stream_generator, k):
    """
    Sample k elements from infinite stream
    stream_generator: function that yields items
    """
    reservoir = []
    stream = stream_generator()
    
    for i, item in enumerate(stream):
        if i < k:
            reservoir.append(item)
        else:
            j = random.randint(0, i)
            if j < k:
                reservoir[j] = item
        
        # Could add stopping condition
        if i >= 1000000:  # Example limit
            break
    
    return reservoir

# Distributed Reservoir Sampling
def distributed_sample(streams, k):
    """
    Combine samples from multiple streams
    streams: list of iterators
    k: total samples needed
    """
    reservoir = []
    total_seen = 0
    
    for stream in streams:
        for item in stream:
            if len(reservoir) < k:
                reservoir.append(item)
            else:
                j = random.randint(0, total_seen)
                if j < k:
                    reservoir[j] = item
            total_seen += 1
    
    return reservoir

# Example usage
if __name__ == "__main__":
    # Sample from list
    data = range(1, 101)  # 1 to 100
    sample = reservoir_sample(iter(data), 10)
    print("Sample of 10:", sample)
    
    # Single random pick
    pick = random_pick(iter(range(10)))
    print("Random pick:", pick)
    
    # Weighted sampling
    weighted_data = [(i, i) for i in range(1, 11)]
    weighted = weighted_reservoir_sample(iter(weighted_data), 5)
    print("Weighted sample:", weighted)
```

## Key Points
- O(k) space for unknown size stream
- Single pass through data
- Each item has equal probability k/n
- No need to know stream size
- Perfect for streaming data

## How It Works
1. Fill reservoir with first k items
2. For item i (where i > k):
   - Generate random j in [0, i]
   - If j < k, replace reservoir[j] with item i
3. Each item has probability k/i → k/n

## Proof of Correctness
Probability that item i ends in reservoir:
- P(selected at i) = k/i
- P(not replaced later) = (k/(i+1)) * (k/(i+2)) * ... * (k/n)
- Combined: k/i * i/(i+1) * (i+1)/(i+2) * ... * (n-1)/n = k/n ✓

## Common Use Cases
- Sampling from logs/streams
- Random selection from database
- Online algorithms
- Network packet sampling
- Large dataset sampling
- Unknown size data

## Example Problems
1. Linked List Random Node (LeetCode #382)
2. Random Pick Index (LeetCode #398)
3. Random Pick with Weight (LeetCode #528)
4. Random Pick with Blacklist (LeetCode #710)

## Notes
- Perfect for streaming/online scenarios
- Space-efficient: only O(k) memory
- Each element equally likely in final sample
- Can extend to weighted sampling
- Used in real systems (Apache Spark, databases)
- No bias toward beginning or end of stream