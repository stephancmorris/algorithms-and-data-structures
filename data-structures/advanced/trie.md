# Trie (Prefix Tree)

## Description
A tree-like data structure used to store strings where each node represents a character. Nodes share common prefixes, making it efficient for prefix-based operations. Also known as a prefix tree or digital tree.

## Time Complexity
- Insert: O(m) where m is the length of the word
- Search: O(m)
- StartsWith (prefix search): O(m)
- Delete: O(m)

## Space Complexity
O(ALPHABET_SIZE * N * M) where N is number of words and M is average length
In practice: O(total characters across all words)

## Implementation

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # Map character to TrieNode
        self.is_end_of_word = False  # True if node represents end of a word
        self.word_count = 0  # Number of words ending at this node

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Insert a word into the trie"""
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True
        node.word_count += 1
    
    def search(self, word):
        """Search for exact word match"""
        node = self._find_node(word)
        return node is not None and node.is_end_of_word
    
    def starts_with(self, prefix):
        """Check if any word starts with the given prefix"""
        return self._find_node(prefix) is not None
    
    def _find_node(self, prefix):
        """Helper: find node representing the prefix"""
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        
        return node
    
    def delete(self, word):
        """Delete a word from the trie"""
        def _delete_recursive(node, word, index):
            if index == len(word):
                # We've reached the end of the word
                if not node.is_end_of_word:
                    return False  # Word doesn't exist
                
                node.is_end_of_word = False
                node.word_count -= 1
                
                # Return True if node has no children (can be deleted)
                return len(node.children) == 0
            
            char = word[index]
            if char not in node.children:
                return False  # Word doesn't exist
            
            child_node = node.children[char]
            should_delete_child = _delete_recursive(child_node, word, index + 1)
            
            if should_delete_child:
                del node.children[char]
                # Return True if node has no children and is not end of another word
                return len(node.children) == 0 and not node.is_end_of_word
            
            return False
        
        _delete_recursive(self.root, word, 0)
    
    def find_all_words_with_prefix(self, prefix):
        """Find all words that start with the given prefix"""
        node = self._find_node(prefix)
        if node is None:
            return []
        
        words = []
        self._collect_words(node, prefix, words)
        return words
    
    def _collect_words(self, node, current_word, words):
        """Helper: collect all words from a node"""
        if node.is_end_of_word:
            words.append(current_word)
        
        for char, child_node in node.children.items():
            self._collect_words(child_node, current_word + char, words)
    
    def count_words_with_prefix(self, prefix):
        """Count words that start with the given prefix"""
        return len(self.find_all_words_with_prefix(prefix))
    
    def longest_common_prefix(self):
        """Find longest common prefix of all words"""
        if not self.root.children:
            return ""
        
        prefix = []
        node = self.root
        
        while len(node.children) == 1 and not node.is_end_of_word:
            char = list(node.children.keys())[0]
            prefix.append(char)
            node = node.children[char]
        
        return ''.join(prefix)

# Example usage
if __name__ == "__main__":
    trie = Trie()
    
    # Insert words
    words = ["apple", "app", "apricot", "banana", "band", "bandana"]
    for word in words:
        trie.insert(word)
    
    # Search for exact matches
    print("Search 'app':", trie.search("app"))  # True
    print("Search 'appl':", trie.search("appl"))  # False
    
    # Check prefixes
    print("Starts with 'app':", trie.starts_with("app"))  # True
    print("Starts with 'ban':", trie.starts_with("ban"))  # True
    print("Starts with 'cat':", trie.starts_with("cat"))  # False
    
    # Find all words with prefix
    print("Words with 'app':", trie.find_all_words_with_prefix("app"))
    # ['app', 'apple', 'apricot']
    
    print("Words with 'ban':", trie.find_all_words_with_prefix("ban"))
    # ['banana', 'band', 'bandana']
    
    # Delete a word
    trie.delete("app")
    print("After deleting 'app':", trie.search("app"))  # False
    print("'apple' still exists:", trie.search("apple"))  # True
```

## Key Points
- Each node represents a character (or prefix)
- Root is empty, edges are labeled with characters
- Words share common prefixes (space-efficient)
- Perfect for autocomplete and spell-checking
- Can store additional data at nodes (frequency, definitions)

## Common Use Cases
- Autocomplete/typeahead suggestions
- Spell checkers and correctors
- IP routing tables (longest prefix matching)
- Dictionary implementations
- String matching algorithms
- T9 predictive text
- DNA sequence analysis
- Browser history

## Trie Variations
- **Compressed Trie (Radix Tree)**: Merge nodes with single child
- **Suffix Trie**: Contains all suffixes of a string
- **Ternary Search Trie**: Three-way branching (less than, equal, greater than)
- **HAT-trie**: Hybrid of hash table and trie
- **Double Array Trie**: Space-efficient implementation

## Advantages
- Fast prefix searches: O(m) vs O(n log n) with sorting
- No hash collisions
- Alphabetically ordered traversal
- Common prefix sharing saves space
- Easy to implement prefix-based operations

## Disadvantages
- Can use more space than hash tables
- Not cache-friendly (many pointers)
- Slower than hash tables for exact matches
- Memory overhead for storing pointers

## Optimization Techniques
- Use arrays instead of hash maps for fixed alphabet
- Compress single-child chains (radix tree)
- Store only used characters per node
- Use bit manipulation for small alphabets

## Example Problems
1. Implement Trie (LeetCode #208)
2. Design Add and Search Words Data Structure (LeetCode #211)
3. Word Search II (LeetCode #212)
4. Replace Words (LeetCode #648)
5. Map Sum Pairs (LeetCode #677)
6. Longest Word in Dictionary (LeetCode #720)
7. Palindrome Pairs (LeetCode #336)
8. Word Squares (LeetCode #425)
9. Maximum XOR of Two Numbers (LeetCode #421)

## Notes
- Common in competitive programming
- Alphabet size matters (26 for lowercase English)
- Consider using array of size 26 for English letters
- For Unicode, use hash map in children
- Practice implementing from scratch
- Useful when multiple prefix queries are needed
- Can be combined with DFS for complex word problems