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