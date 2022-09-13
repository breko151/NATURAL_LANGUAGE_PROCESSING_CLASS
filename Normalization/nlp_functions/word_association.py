# Author: Suárez Pérez Juan Pablo
# Date: 11/09/2022

from ast import In
from os import execv
import numpy as np


def get_contexts(vocabulary, text, window = 8):
    contexts = dict()
    for w in vocabulary:
        context = list()
        for i in range(len(text)):
            if text[i] == w:
                for j in range(i - int(window / 2), i):
                    if j >= 0:
                        context.append(text[j])
                try: 
                    for j in range(i + 1, i + (int(window / 2) + 1)):
                        context.append(text[j])
                except IndexError:
                        pass
        contexts[w] = context
    return contexts


def get_contexts_sents(vocabulary, text, window = 8):
    contexts = dict()
    for w in vocabulary:
        context = list()
        for sent in text:
            words = sent.split()
            for i in range(len(words)):
                if words[i] == w:
                    for j in range(i - int(window / 2), i):
                        if j >= 0:
                            context.append(words[j])
                    try:
                        for j in range(i + 1, i + (int(window / 2) + 1)):
                            context.append(words[j])
                    except IndexError:
                        pass
        contexts[w] = context
    return contexts


def get_probabilities(vocabulary, contexts):
    vectors = dict()
    for v in vocabulary:
        context = contexts[v]
        vector = []
        for voc in vocabulary:
            vector.append(context.count(voc))
        vector = np.array(vector)
        s = np.sum(vector)
        try:
            vector = vector / s
        except:
            vector = vector / 1
        vectors[v] = vector
    return vectors


def s_dot_product(word, vectors, aux_path = ''):
    similarities = dict()
    v = vectors[word]
    for w in vectors.keys():
        similarities[w] = np.dot(vectors[w], v)
    similarities = (sorted(similarities.items(), key = lambda item: item[1], reverse = True))
    with open('./dot_product/similar_to_' + word + aux_path + '.txt', 'w', encoding = 'utf-8') as f:
        for item in similarities:
            f.write(str(item) + '\n')


def s_cosine(word, vectors, aux_path = ''):
    similarities = dict()
    v = vectors[word]
    for w in vectors.keys():
        v2 = vectors[w]
        similarities[w] = np.dot(v, v2) / np.linalg.norm(v) * np.linalg.norm(v2)
    similarities = (sorted(similarities.items(), key = lambda item: item[1], reverse = True))
    with open('./cosine/similar_to_' + word + aux_path + '.txt', 'w', encoding = 'utf-8') as f:
        for item in similarities:
            f.write(str(item) + '\n')


def similar_words(word, vectors, aux_path = '', tf_idf = False, dot_product = False, cosine = False):        
    if dot_product:
        s_dot_product(word, vectors, aux_path)
                
    if cosine:
        s_cosine(word, vectors, aux_path)