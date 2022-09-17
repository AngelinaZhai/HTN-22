# -*- coding: utf-8 -*-
"""similarity_score.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bJ1TxZh16M3rXwT58CVwQ7tKIqxDPhec
"""

# from sentence_transformer import SentenceTransformer
import torch
import torchtext
import numpy as np
import scipy
from scipy import spatial
import re

glove = torchtext.vocab.GloVe(name='6B', dim=50)

# def preprocess(s):
#     return [i.lower() for i in s.split()]

def preprocess(input):
    #remove special symbols
    cleaned = re.sub("[^a-zA-Z]", " ", input)
    #convert to lowercase and split
    cleaned = cleaned.lower().split()
    return cleaned

def get_vector(s):
    # return np.sum([glove[i] for i in preprocess(s)])
    elements = []
    for i in preprocess(s):
      try:

        if (glove[i] != None) and (torch.count_nonzero(glove[i]) > 0):
          elements.append(glove[i])
      except:
        continue
    return sum(elements)

def similarity_score(s1, s2):
    v1 = get_vector(s1)
    v2 = get_vector(s2)
    if ((len(s1) == 0) or (len(s2) == 0)):
      return 0
    elif ((v1 == None) or (v2 == None)):
      return 0
    else:
      return (1-spatial.distance.cosine(v1, v2))

#glove['cat']

# glove['poop']

#similarity_score('', '')
