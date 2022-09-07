from collections import Counter

def make_vocabulary(words):
    vocabulry = sorted(list(set(words)))
    return vocabulry


def find_context(word, words, window_size = 4):
    context = list()
    for i in range(len(words)):
        if words[i] == word:
            context += words[i - window_size:i] + words[i + 1:i + window_size + 1]
    return context


def create_vector_space(words, vocabulary):
    vector_space = list()
    for word in vocabulary:
        context = find_context(word, words)
        counter = Counter(context)
        vector_space.append(counter)
    return vector_space