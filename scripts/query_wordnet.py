from nltk.corpus import wordnet as wn

# Example: Get synonyms for 'happiness'
word = 'happiness'
synonyms = wn.synsets(word)

if synonyms:
    print(f"Synonyms and definitions for the word '{word}':")
    for syn in synonyms:
        print(f"\nDefinition: {syn.definition()}")
        print(f"Examples: {syn.examples()}")
else:
    print(f"No synonyms found for the word '{word}'.")
