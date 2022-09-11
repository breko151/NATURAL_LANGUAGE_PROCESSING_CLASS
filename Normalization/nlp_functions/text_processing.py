# Author: Suárez Pérez Juan Pablo
# Date: 10/09/2022

# Import the libraries needed for the module...
from lib2to3.pgen2 import token
from nltk.corpus import PlaintextCorpusReader
from bs4 import BeautifulSoup
import re
import nltk

def clean_corpus(path_origin, path_destiny):
    """
        Here, you can clean your corpus, so if you can get
        a text free HTML tags and save the corpus in an unique 
        arhive 'clean_corpus.txt'.
        path_origin: the path of your original corpus.
        path_destiny: the path of yout clean corpus.
    """
    corpus = PlaintextCorpusReader(path_origin, '.*')
    file_list = corpus.fileids()
    all_text = ''
    # Get all text of the corpus
    for file in file_list:
        with open(path_origin + file, encoding = 'utf-8') as rfile:
            text = rfile.read()
            all_text += text
    # Remove HTML tags
    soup = BeautifulSoup(all_text, 'lxml')
    clean_text = soup.get_text()
    # Apply the function lower to the text
    clean_text = clean_text.lower()
    # Save the file
    with open(path_destiny + 'clean_corpus.txt', 'w', encoding = 'utf-8') as file:
        file.write(clean_text)


def word_tokenize(path):
    """
        Here you can tokenize yor clean corpus by words.
        path: the path of your clean corpus
    """
    # Read the file
    text = ''
    with open(path, encoding = 'utf-8') as file:
        text = file.read()
    words = text.split()
    # Get only alphabetic words
    alphabetic_words = list()
    for word in words:
        token = list()
        for character in word:
            if re.match(r'^[a-záéíóúñü+$]', character):
                token.append(character)
        token = ''.join(token)
        if token != '':
            alphabetic_words.append(token)
    # Return tokens
    return alphabetic_words


def sentence_tokenize(path):
    """
        Here you can tokenize yor clean corpus by words.
        path: the path of your clean corpus 
    """
    # Read the file
    text = ''
    with open(path, encoding = 'utf-8') as file:
        text = file.read() 
    tokens = nltk.data.load("tokenizers/punkt/spanish.pickle") 
    sents = tokens.tokenize(text)
    alphabetic_sents = list()
    for sent in sents:
        sent_token = list()
        words = sent.split()
        for word in words:
            token = list()
            for character in word:
                if re.match(r'^[a-záéíóúñü+$]', character):
                    token.append(character)
            token = ''.join(token)
            if token != '':
                sent_token.append(token)
        sent_token = " ".join(sent_token)
        if sent_token != '':
            alphabetic_sents.append(sent_token)



        # for word in words:
        #     token = list()
        #     for character in word:
        #         if re.match(r'^[a-záéíóúñü+$]', character):
        #             token.append(character)
        #         token = ''.join(character)
        #         if token != '':
        #             sent_token = token.join(' ')
        # if sent_token != '':
        #     alphabetic_sents.append(sent_token)

    return alphabetic_sents


