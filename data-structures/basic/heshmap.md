# Hashmap (Hash Table)

## Description
A data structure that maps keys to values using a hash function. It provides average constant-time operations for insertion, deletion, and lookup. Also known as a dictionary, map, or associative array.

## Time Complexity
- Insert: O(1) average, O(n) worst case
- Delete: O(1) average, O(n) worst case
- Search/Lookup: O(1) average, O(n) worst case
- Access by key: O(1) average, O(n) worst case

## Space Complexity
O(n) where n is the number of key-value pairs

## Implementation

```python
class HashMap:
    def __init__(self, initial_capacity=16):
        self.capacity = initial_capacity
        self.size = 0
        self.load_factor = 0.75
        self.buckets = [[] for _ in range(self.capacity)]
    
    def _hash(self, key):
        """Generate hash index for key"""
        return hash(key) % self.capacity
    
    def put(self, key, value):
        """Insert or update key-value pair"""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # Update existing key
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # Add new key-value pair
        bucket.append((key, value))
        self.size += 1
        
        # Resize if load factor exceeded
        if self.size / self.capacity > self.load_factor:
            self._resize()
    
    def get(self, key):
        """Get value for key, return None if not found"""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def remove(self, key):
        """Remove key-value pair, return True if found"""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
        return False
    
    def contains(self, key):
        """Check if key exists"""
        return self.get(key) is not None
    
    def _resize(self):
        """Double capacity and rehash all entries"""
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)
    
    def keys(self):
        """Return all keys"""
        result = []
        for bucket in self.buckets:
            for key, _ in bucket:
                result.append(key)
        return result
    
    def values(self):
        """Return all values"""
        result = []
        for bucket in self.buckets:
            for _, value in bucket:
                result.append(value)
        return result
    
    def items(self):
        """Return all key-value pairs"""
        result = []
        for bucket in self.buckets:
            for item in bucket:
                result.append(item)
        return result
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        items = self.items()
        return "{" + ", ".join(f"{k}: {v}" for k, v in items) + "}"

# Example usage
if __name__ == "__main__":
    hmap = HashMap()
    hmap.put("name", "Alice")
    hmap.put("age", 30)
    hmap.put("city", "Sydney")
    
    print(hmap)  # Output: {name: Alice, age: 30, city: Sydney}
    print(hmap.get("name"))  # Output: Alice
    print(hmap.contains("age"))  # Output: True
    hmap.remove("age")
    print(hmap)  # Output: {name: Alice, city: Sydney}
```

## Key Points
- Hash function converts keys to array indices
- Collisions handled via chaining (linked lists) or open addressing
- Load factor determines when to resize (typically 0.75)
- Good hash function is crucial for performance
- Keys must be immutable (hashable)

## Common Use Cases
- Caching and memoization
- Counting frequencies (character counts, word counts)
- Storing configuration settings
- Database indexing
- Implementing sets
- Fast lookups in algorithms

## Collision Resolution Strategies
- **Chaining**: Each bucket contains a list of entries (used in our implementation)
- **Open Addressing**: Find next available slot (linear probing, quadratic probing)
- **Double Hashing**: Use second hash function for probing

## Example Problems
1. Two Sum (LeetCode #1)
2. Group Anagrams (LeetCode #49)
3. Valid Anagram (LeetCode #242)
4. Longest Substring Without Repeating Characters (LeetCode #3)
5. Subarray Sum Equals K (LeetCode #560)
6. LRU Cache (LeetCode #146) - uses hashmap + doubly linked list
7. Top K Frequent Elements (LeetCode #347)

## Notes
- Python's dict and Java's HashMap use similar implementations
- Perfect hashing possible when keys are known in advance
- Consider using OrderedDict if insertion order matters
- For small datasets (<10 items), linear search might be faster
- Security: Be aware of hash collision attacks in production systems