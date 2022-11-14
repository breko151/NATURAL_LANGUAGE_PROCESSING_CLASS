# Author: Suárez Pérez Juan Pablo
# Date: 13/11/2022


def get_most_freq_words(lemmatize_sents, vocabulary):
    tokens = dict()
    for word in vocabulary:
        tokens[word] = 0
    
    for sent in lemmatize_sents:
        for word in sent:
            tokens[word] += 1
    new_tokens = (sorted(tokens.items(), key = lambda item: item[1], reverse = True))
    with open('./most_freq_words/most_freq.txt', 'w', encoding = 'utf-8') as f:
        for item in new_tokens:
            f.write(str(item) + '\n')
    return tokens


def get_most_freq_words_prob(lemmatize_sents, vocabulary):
    tokens = dict()
    n = len(vocabulary)
    for word in vocabulary:
        tokens[word] = 0
    
    for sent in lemmatize_sents:
        for word in sent:
            tokens[word] += 1
    for k in tokens.keys():
        prob = tokens[k] /n
        tokens[k] = prob
    new_tokens = (sorted(tokens.items(), key = lambda item: item[1], reverse = True))
    with open('./most_freq_words/most_freq_prob.txt', 'w', encoding = 'utf-8') as f:
        for item in new_tokens:
            f.write(str(item) + '\n')
    return tokens


def get_most_freq_words_tf_idf(idf, freq, vocabulary):
    n = len(idf)
    tokens = dict()
    i = 0
    for word in vocabulary:
        tokens[word] = freq[word] * idf[i]
        i += 1
    tokens = (sorted(tokens.items(), key = lambda item: item[1], reverse = True))
    with open('./most_freq_words/most_freq_tf_idf.txt', 'w', encoding = 'utf-8') as f:
        for item in tokens:
            f.write(str(item) + '\n')
    return tokens


def get_distribution(titles, articles, topics):
    distribution_in_articles = dict()
    for n in range(len(titles)):
        distribution_in_articles[titles[n]] = get_freq(topics, articles[n])
    return distribution_in_articles


def get_freq(topics, article):
    freq = dict()
    for word in topics:
        freq[word] = 0
    for sent in article:
        for word in topics:
            if word in sent:
                freq[word] += 1
    pis = dict()
    sum = 0
    for v in freq.values():
        sum += v
    for k, v in freq.items():
        if sum != 0:
            pis[k] = v / sum
        else:
            pis[k] = 0
    return pis