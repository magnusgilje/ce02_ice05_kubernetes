#pylint:disable=c0305,c0301,c0116,c0103,c0303,w0511,r0914,w0613,w0612,r1705,w0703,c0114,c0325,c0410,c0413,e0401,c0411,w0611,e0102,r1721,c0121,w0621,w0622
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 12:11:59 2022

@author: RobertMcLeod
"""

# Natural Language Toolkit
import nltk

# Imports
import re
import os

# Import NLTK stuff
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

def case_normalize(text):
    '''
    Takes in a text string and returns a string with all characters in lower case. 
    '''
    return(text.lower())
def remove_punctuation(text):
    '''
    Takes in a text string and returns a string with all the punctuation removed.
    '''
    return(re.sub(r'[^a-zA-Z0-9]', ' ', text))
def tokenize(text):
    '''
    Takes in a text string and returns a list where each item corresponds to a token.
    '''
    return(word_tokenize(text))
def remove_stopwords(tokenized_text):
    '''
    Takes in a list of text, and returns another list where the stop words have been removed.
    '''
    stopword_list = stopwords.words('english')
    return([word for word in tokenized_text if word not in stopword_list])
def remove_unknown_words(tokenized_text):
    '''
    Takes in a list of text, and returns another list where unknown words have been removed.
    '''
    word_dict = set(word.lower() for word in nltk.corpus.words.words())
    return([word for word in tokenized_text if word in word_dict])
def lemmatize(tokenized_text):
    '''
    Takes in a list of text, and returns another list where each word has been lemmatized.
    '''
    lemmatizer = WordNetLemmatizer()
    return([lemmatizer.lemmatize(word) for word in tokenized_text])

def process_text(text):
    '''
    Takes in a raw text document and performs the following steps in order:
    - punctuation removal
    - case normalization
    - tokenization
    - remove stopwords
    - lemmatization
    Then returns a string containing the processed text
    '''
    text_punc = remove_punctuation(text)
    text_norm = case_normalize(text_punc)
    text_tokenized = tokenize(text_norm)
    text_stop_removed = remove_stopwords(text_tokenized)
    text_lemmatized = lemmatize(text_stop_removed)
    output_text = ' '.join(text_lemmatized)
    # text_dict_words = remove_unknown_words(text_stop_removed)
    return(output_text)

def process_text_files(input_path):
    '''
    Takes all the cleaned text files in the input folder 
    and processes them into lists for NB classification
    '''
    with open(input_path,encoding="utf-8") as f:
        lines = f.read()
    processed_text = process_text(lines)        
    return(processed_text)

        