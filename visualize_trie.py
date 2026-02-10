"""
Trie Visualization Demo
Shows how words are stored in the Trie structure
"""

from trie import Trie

def demo_small_trie():
    """Demonstrate with a small set of words"""
    print("\n" + "=" * 70)
    print("DEMO 1: Small Word Set")
    print("=" * 70)
    
    trie = Trie()
    words = ["cat", "car", "card", "care", "dog", "door", "dot"]
    
    print(f"\nInserting words: {words}")
    for word in words:
        trie.insert(word)
    
    # Visualize the entire trie
    trie.visualize(max_depth=10)
    
    # Show some autocomplete examples
    print("\n📝 Autocomplete Examples:")
    print("-" * 70)
    
    prefixes = ["ca", "car", "d", "do"]
    for prefix in prefixes:
        suggestions = trie.search_prefix(prefix)
        print(f"  '{prefix}' → {suggestions}")


def demo_fantasy_trie():
    """Demonstrate with fantasy-themed words"""
    print("\n" + "=" * 70)
    print("DEMO 2: Fantasy Theme")
    print("=" * 70)
    
    trie = Trie()
    words = [
        "dragon", "druid", "dungeon", "dwarf",
        "elf", "elixir", "enchant",
        "wizard", "wand", "witch",
        "magic", "mage", "mana",
        "quest", "castle", "sword"
    ]
    
    print(f"\nInserting {len(words)} fantasy words...")
    for word in words:
        trie.insert(word)
    
    # Visualize first 3 levels
    trie.visualize(max_depth=3)
    
    # Show some autocomplete examples
    print("\n📝 Autocomplete Examples:")
    print("-" * 70)
    
    prefixes = ["d", "dr", "e", "wi", "ma"]
    for prefix in prefixes:
        suggestions = trie.search_prefix(prefix)
        print(f"  '{prefix}' → {suggestions}")


def demo_with_user_input():
    """Interactive demo where user can add words and see the trie"""
    print("\n" + "=" * 70)
    print("DEMO 3: Interactive Trie Builder")
    print("=" * 70)
    
    trie = Trie()
    
    print("\nEnter words one by one (type 'done' when finished):")
    while True:
        word = input("Add word: ").strip().lower()
        if word == 'done':
            break
        if word:
            trie.insert(word)
            print(f"  ✓ Added '{word}'")
    
    # Visualize the trie
    trie.visualize(max_depth=5)
    
    # Let user test autocomplete
    print("\n📝 Test Autocomplete:")
    print("Type prefixes to see suggestions (type 'quit' to exit)")
    while True:
        prefix = input("\nPrefix: ").strip().lower()
        if prefix == 'quit':
            break
        if prefix:
            suggestions = trie.search_prefix(prefix)
            if suggestions:
                print(f"  ✓ Suggestions: {suggestions}")
            else:
                print(f"  ✗ No suggestions found")


def main():
    """Run all demos"""
    print("🌳" * 35)
    print("TRIE DATA STRUCTURE VISUALIZATION")
    print("🌳" * 35)
    
    # Demo 1: Small simple example
    demo_small_trie()
    
    input("\n\nPress Enter to continue to Demo 2...")
    
    # Demo 2: Fantasy theme
    demo_fantasy_trie()
    
    input("\n\nPress Enter to continue to Demo 3...")
    
    # Demo 3: Interactive
    demo_with_user_input()
    
    print("\n" + "=" * 70)
    print("✨ Visualization Complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()
