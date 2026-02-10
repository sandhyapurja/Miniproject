class TrieNode:
    """A node in the Trie structure"""
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """Trie data structure for efficient prefix-based autocomplete"""
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        """Insert a word into the Trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search_prefix(self, prefix: str) -> list[str]:
        """Find all words that start with the given prefix"""
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        results = []
        self._collect_words(node, prefix, results)
        return sorted(results)
    
    def _collect_words(self, node: TrieNode, current_word: str, results: list):
        """Recursively collect all words from a given node"""
        if node.is_end_of_word:
            results.append(current_word)
        
        for char, child_node in node.children.items():
            self._collect_words(child_node, current_word + char, results)
    
    def visualize(self, max_depth: int = 10):
        """Display the Trie structure"""
        print("\n" + "=" * 70)
        print("TRIE STRUCTURE VISUALIZATION")
        print("=" * 70)
        self._visualize_helper(self.root, "", 0, max_depth)
    
    def _visualize_helper(self, node: TrieNode, prefix: str, depth: int, max_depth: int):
        """Recursive helper for visualization"""
        if depth > max_depth:
            return
        
        if node.is_end_of_word:
            print(f"{'  ' * depth}✓ {prefix}")
        
        for char, child_node in sorted(node.children.items()):
            if not node.is_end_of_word or child_node.children:
                print(f"{'  ' * depth}├─ {char}")
            self._visualize_helper(child_node, prefix + char, depth + 1, max_depth)



