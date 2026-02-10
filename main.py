from trie import Trie
import random

# Pre-defined theme word lists
THEME_WORDS = {
    "ocean": [
        "wave", "tide", "coral", "reef", "shark", "whale", "dolphin", "fish",
        "seaweed", "kelp", "ocean", "sea", "beach", "coast", "shore", "sand",
        "shell", "starfish", "jellyfish", "octopus", "squid", "crab", "lobster",
        "shrimp", "seal", "otter", "turtle", "submarine", "shipwreck", "anchor",
        "sailor", "maritime", "nautical", "marine", "aquatic", "underwater",
        "deep sea", "abyss", "trench", "current", "whirlpool", "tsunami",
        "saltwater", "tidal pool", "bay", "gulf", "harbor", "port", "lighthouse",
        "buoy", "pier", "dock", "marina", "sailing", "surfing", "diving"
    ],
    "space": [
        "star", "planet", "moon", "sun", "galaxy", "nebula", "comet", "asteroid",
        "meteor", "satellite", "rocket", "spaceship", "astronaut", "cosmonaut",
        "orbit", "universe", "cosmos", "solar system", "milky way", "black hole",
        "supernova", "constellation", "telescope", "observatory", "mars", "venus",
        "jupiter", "saturn", "mercury", "uranus", "neptune", "pluto", "earth",
        "atmosphere", "gravity", "spacecraft", "shuttle", "apollo", "launch",
        "mission", "space station", "ISS", "lunar", "interstellar", "celestial",
        "aurora", "eclipse", "radiation", "vacuum", "zero gravity", "alien"
    ],
    "cooking": [
        "recipe", "ingredient", "chef", "kitchen", "oven", "stove", "pan", "pot",
        "knife", "cutting board", "whisk", "spatula", "spoon", "fork", "plate",
        "bowl", "measuring cup", "bake", "boil", "fry", "sauté", "grill", "roast",
        "simmer", "steam", "chop", "dice", "mince", "slice", "blend", "mix",
        "stir", "season", "marinate", "garnish", "serve", "taste", "flavor",
        "spice", "herb", "salt", "pepper", "garlic", "onion", "vegetable",
        "meat", "poultry", "fish", "pasta", "rice", "bread", "sauce", "soup",
        "salad", "dessert", "appetizer", "main course", "side dish"
    ],
    "technology": [
        "computer", "laptop", "smartphone", "tablet", "keyboard", "mouse",
        "monitor", "screen", "processor", "CPU", "RAM", "hard drive", "SSD",
        "motherboard", "GPU", "software", "hardware", "application", "program",
        "code", "algorithm", "database", "server", "cloud", "network", "internet",
        "wifi", "bluetooth", "USB", "cable", "router", "modem", "firewall",
        "encryption", "security", "password", "authentication", "programming",
        "developer", "engineer", "artificial intelligence", "machine learning",
        "AI", "robot", "automation", "digital", "virtual", "augmented reality",
        "VR", "AR", "blockchain", "cryptocurrency", "bitcoin", "cybersecurity"
    ],
    "fantasy": [
        "dragon", "wizard", "witch", "magic", "spell", "wand", "potion", "enchantment",
        "castle", "kingdom", "throne", "crown", "sword", "shield", "armor", "knight",
        "quest", "adventure", "dungeon", "treasure", "crystal", "amulet", "talisman",
        "elf", "dwarf", "goblin", "orc", "troll", "fairy", "pixie", "unicorn",
        "phoenix", "griffin", "centaur", "mermaid", "vampire", "werewolf", "ghost",
        "spirit", "demon", "angel", "sorcery", "necromancy", "prophecy", "legend",
        "myth", "folklore", "mystical", "magical", "enchanted", "cursed", "blessed",
        "portal", "realm", "dimension", "fantasy world", "epic", "hero", "villain"
    ],
    "sports": [
        "football", "soccer", "basketball", "baseball", "tennis", "golf", "hockey",
        "cricket", "rugby", "volleyball", "badminton", "swimming", "running",
        "cycling", "boxing", "wrestling", "martial arts", "karate", "judo", "taekwondo",
        "gymnastics", "track and field", "athletics", "marathon", "sprint", "relay",
        "jump", "throw", "catch", "kick", "pass", "shoot", "score", "goal", "point",
        "win", "lose", "draw", "tie", "match", "game", "tournament", "championship",
        "league", "team", "player", "athlete", "coach", "referee", "stadium", "arena",
        "field", "court", "pitch", "pool", "track", "medal", "trophy", "victory"
    ],
    "music": [
        "guitar", "piano", "drums", "violin", "flute", "saxophone", "trumpet",
        "clarinet", "bass", "keyboard", "synthesizer", "microphone", "amplifier",
        "speaker", "headphones", "song", "melody", "harmony", "rhythm", "beat",
        "tempo", "chord", "note", "scale", "key", "pitch", "tone", "octave",
        "verse", "chorus", "bridge", "intro", "outro", "solo", "riff", "lyrics",
        "composer", "musician", "singer", "band", "orchestra", "ensemble", "choir",
        "concert", "performance", "gig", "album", "track", "single", "record",
        "studio", "recording", "mixing", "mastering", "genre", "rock", "pop",
        "jazz", "classical", "hip hop", "electronic", "country", "blues"
    ],
    "mythical creatures": [
        "dragon", "phoenix", "unicorn", "griffin", "pegasus", "centaur", "minotaur",
        "cyclops", "hydra", "chimera", "sphinx", "basilisk", "cockatrice", "manticore",
        "cerberus", "kraken", "leviathan", "behemoth", "thunderbird", "roc",
        "wyvern", "wyrm", "drake", "lindworm", "fairy", "pixie", "sprite", "nymph",
        "dryad", "naiad", "mermaid", "siren", "selkie", "kelpie", "banshee",
        "leprechaun", "brownie", "goblin", "hobgoblin", "orc", "troll", "ogre",
        "giant", "titan", "golem", "gargoyle", "harpy", "gorgon", "medusa",
        "valkyrie", "yeti", "bigfoot", "sasquatch", "chupacabra", "wendigo",
        "kitsune", "tanuki", "oni", "tengu", "qilin", "fenghuang"
    ]
}

def generate_and_load_trie(theme: str, num_words: int, trie: Trie):
    """
    Loads words from pre-defined theme lists into the Trie.
    No API calls needed!
    """
    if not theme or not theme.strip():
        print("ERROR: Theme cannot be empty!")
        return []
    
    theme_lower = theme.lower()
    
    # Find matching theme (flexible matching)
    available_words = None
    for key in THEME_WORDS.keys():
        if theme_lower in key or key in theme_lower:
            available_words = THEME_WORDS[key].copy()
            break
    
    if not available_words:
        print(f"Warning: Theme '{theme}' not found in predefined lists.")
        print(f"Available themes: {', '.join(THEME_WORDS.keys())}")
        return []
    
    print(f"Loading words for theme: '{theme}'...")
    
    # Shuffle to get variety
    random.shuffle(available_words)
    
    # Take requested number of words (or all if requesting more than available)
    words_to_use = available_words[:num_words]
    
    # Load words into trie
    for word in words_to_use:
        trie.insert(word.lower())
    
    actual_count = len(words_to_use)
    print(f"Successfully loaded {actual_count} words into the Trie.")
    
    if actual_count < num_words:
        print(f"Note: Only {actual_count} words available for this theme (requested {num_words})")
    
    return words_to_use

def main():
    """Interactive autocomplete demo"""
    print("=" * 70)
    print("TRIE AUTOCOMPLETE ")
    print("=" * 70)
    
    print(f"\nAvailable themes: {', '.join(THEME_WORDS.keys())}")
    theme = input("Enter a theme: ").strip()
    
    if not theme:
        theme = "fantasy"
        print(f"Using default theme: '{theme}'")
    
    try:
        num_input = input("How many words to generate? (default 30): ").strip()
        num_words = int(num_input) if num_input else 30
        
        if num_words < 1:
            print("Number must be positive, using default (30)")
            num_words = 30
        elif num_words > 100:
            print("Large requests may use all available words...")
            
    except ValueError:
        print("Invalid number, using default (30)")
        num_words = 30
    
    my_trie = Trie()
    theme_words = generate_and_load_trie(theme, num_words, my_trie)
    
    if not theme_words:
        print("Failed to load words. Exiting.")
        return
    
    # Show sample of loaded words
    sample_size = min(10, len(theme_words))
    print(f"\nSample words: {', '.join(theme_words[:sample_size])}")
    if len(theme_words) > sample_size:
        print(f"... and {len(theme_words) - sample_size} more")
    
    print("\nTrie Structure:")
    my_trie.visualize(max_depth=20)
    
    print("\n" + "=" * 70)
    print("AUTOCOMPLETE DEMO")
    print("=" * 70)
    print("Type a prefix to get suggestions (or 'quit' to exit)")
    
    while True:
        try:
            prefix = input("\nEnter prefix: ").strip()
            
            if prefix.lower() == 'quit':
                break
            
            if not prefix:
                print("Please enter a non-empty prefix")
                continue
            
            suggestions = my_trie.search_prefix(prefix.lower())
            
            if suggestions:
                print(f"Suggestions for '{prefix}': {', '.join(suggestions)}")
            else:
                print(f"No suggestions found for '{prefix}'")
                
        except KeyboardInterrupt:
            print("\n\nInterrupted by user")
            break
        except Exception as e:
            print(f"Error during search: {e}")
    
    print("\nThanks for using Trie Autocomplete!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
    except Exception as e:
        print(f"\nUnexpected error: {e}")