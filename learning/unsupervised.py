from nltk.corpus import wordnet

class UnsupervisedLearning:
    @staticmethod
    def get_synonyms(word):
        synonyms = []
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
        return set(synonyms)

    @staticmethod
    def get_antonyms(word):
        antonyms = []
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                if lemma.antonyms():
                    antonyms.append(lemma.antonyms()[0].name())
        return set(antonyms)
