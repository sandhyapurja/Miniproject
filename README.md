# DSA Assignment 3
## Trie Autocomplete

A Python-based autocomplete system using a Trie (prefix tree) data structure with themed word collections.

## 📌 About the Program

This project implements an interactive autocomplete system that uses a Trie data structure to efficiently store and search words. It comes with 8 pre-defined themed word collections, making it perfect for learning about Tries or building autocomplete features.

## Features

 **Efficient Prefix Search**: Fast autocomplete suggestions using Trie data structure
 
**8 Themed Word Collections** : Pre-loaded word lists including:

Ocean (marine life, nautical terms)

Space (astronomy, celestial objects)

Cooking (culinary terms, kitchen items)

Technology (computing, digital terms)

Fantasy (magical creatures, medieval elements)

Sports (games, equipment, competitions)

Music (instruments, musical terms)

Mythical Creatures (legendary beings from various cultures)


**Trie Visualization**: View the structure of your loaded Trie

**Interactive Demo**: Command-line interface for testing autocomplete

**Flexible Theme Matching**: Fuzzy matching for theme selection

## Usage

### Interactive Mode
Run the program and follow the prompts:
 **main.py**

Select a theme from the available options

Specify number of words to load (default: 30)

View the Trie structure and sample words

Enter prefixes to get autocomplete suggestions

Type quit to exit

## How It Works

**Word Loading**: Pre-defined word lists are stored in the THEME_WORDS dictionary

**Randomization**: Words are shuffled to provide variety each run

**Trie Construction**: Selected words are inserted into the Trie data structure

**Prefix Search**: User enters a prefix, and the Trie returns all matching words

## Limitations

Maximum words per theme varies (55-60 words typically)

Requesting more words than available will use all available words

Theme matching is case-insensitive and uses partial matching

## Error Handling
The application handles:

Invalid theme names (shows available themes)

Invalid number inputs (uses default of 30)

Empty prefixes

Keyboard interrupts (Ctrl+C)
General exceptions during operation

