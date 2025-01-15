import json
from nltk.corpus import wordnet as wn

def extract_wordnet_data():
    word_data = {}

    for synset in wn.all_synsets():
        word = synset.name().split('.')[0]  # Extract the word name
        definition = synset.definition()  # Get the definition
        examples = synset.examples()  # Get example sentences

        # Collect synonyms
        synonyms = set()
        for lemma in synset.lemmas():
            synonyms.add(lemma.name())

        # Collect antonyms
        antonyms = set()
        for lemma in synset.lemmas():
            if lemma.antonyms():
                for antonym in lemma.antonyms():
                    antonyms.add(antonym.name())

        # Structure the data
        word_data[word] = {
            "definition": definition,
            "examples": examples,
            "synonyms": list(synonyms),
            "antonyms": list(antonyms),
        }

    return word_data

# Save the data as a JSON file for later use
if __name__ == "__main__":
    print("Extracting WordNet data...")
    data = extract_wordnet_data()

    with open("wordnet_data.json", "w") as f:
        json.dump(data, f, indent=4)
    print("WordNet data has been saved to 'wordnet_data.json'.")
