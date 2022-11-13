# Author: Suárez Pérez Juan Pablo
# Date: 11/09/2022

# Import the libraries needed for the module...
import numpy as np


def get_Entropy(target, word, sents):
    """
        Here you can get entropy between words.
        target: principal word.
        word: secundary word.
        sents: set of sents.
    """
    n = len(sents)
    # Get sentences where are the following conditions
    only_target = [sent for sent in sents if target in sent]
    target_word = [sent for sent in sents if (target in sent) and (word in sent)]
    target_no_word = [sent for sent in sents if (target in sent) and (word not in sent)]
    no_target_word = [sent for sent in sents if (target not in sent) and (word in sent)]
    no_target_no_word = [sent for sent in sents if (target not in sent) and (word not in sent)]
    # Get individual probabilities
    prob_1 = (len(only_target) + 0.5) / (n + 1)
    prob_0 = 1 - prob_1
    # Get joint probabilites
    prob_1_1 = (len(target_word) + 0.225) / (n + 1)
    prob_1_0 = (len(target_no_word) + 0.25) / (n + 1)
    prob_0_1 = (len(no_target_word) + 0.25) / (n + 1)
    prob_0_0 = (len(no_target_no_word) + 0.25) / (n + 1)
    # Get conditional probabilities
    c_prob_1_1 = prob_1_1 / prob_1
    c_prob_1_0 = prob_1_0 / prob_1
    c_prob_0_1 = prob_0_1 / prob_0
    c_prob_0_0 = prob_0_0 / prob_0
    # Get entropy
    a = prob_0 * c_prob_0_0 * np.log2(c_prob_0_0)
    b = prob_0 * c_prob_0_1 * np.log2(c_prob_0_1)
    c = prob_1 * c_prob_1_0 * np.log2(c_prob_1_0)
    d = prob_1 * c_prob_1_1 * np.log2(c_prob_1_1) 
    entropy = (-1) * (a + b + c + d)
    return entropy  

