#pylint: disable=c0305,c0301,c0116,c0103,c0303,w0511,r0914,w0613,w0612,r1705,w0703,c0114,c0325,c0410,c0413,e0401,c0411,w0611,e0102,r1721,c0121,w0621,w0622,w0107,e0012
'''
Author : Albert Tran
Created: 2020-08-07

The Loughran-McDonald Master Dictionary can be downloaded here:
https://sraf.nd.edu/textual-analysis/resources/#Master%20Dictionary

Additional documentation:
https://www.uts.edu.au/sites/default/files/ADG_Cons2015_Loughran%20McDonald%20JE%202011.pdf

'''

# %% 
# ------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import os
import pandas as pd
import pkg_resources


# %% 
# ------------------------------------------------------------------------------
# File Path
#-------------------------------------------------------------------------------
# Setting up the file path
DATA_PATH = pkg_resources.resource_filename(__name__, '../ref_data/csv/')
file_path = os.path.join(DATA_PATH,'LoughranMcDonald_MasterDictionary_2018.csv')


# %% 
# ------------------------------------------------------------------------------
# Loughran-McDonald Dictionary
#-------------------------------------------------------------------------------
sentiment_list = ['Negative','Positive','Uncertainty','Litigious',
                  'Constraining','Superfluous','Interesting','Modal']


def get_lmdict_df(lemmatize=False, relevant_cols_only=True):
    '''
    Returns the LM dictionary as a table.
    '''
    # Read in the data path
    df = pd.read_csv(file_path)
    # TODO: Figure out what the numbers in the cells mean...

    # Remove irrelevant columns
    if relevant_cols_only:
        df = df[['Word'] + sentiment_list]
    
    # Remove words that are not associated with any sentiment
    df[sentiment_list] = df[sentiment_list].astype(bool)
    df = df[df[sentiment_list].any(axis=1)]

    # Change all words to lowercase
    df['Word'] = df['Word'].str.lower()

    # Lemmatization
    if lemmatize:
        # TODO: Lemmatization and duplicate dropping?
        print('Implement lemmatization!')
        pass

    return df


def get_sentiment_word_dict(**params):
    '''
    Returns a dictionary where:
    - The keys are the sentiments
    - The value is a list of words associated with the sentiments
    '''
    # Get the LM table
    df = get_lmdict_df(**params)

    # Create the sentiment dictionary
    sentiment_dict = {}
    for sentiment in sentiment_list:
        sentiment_dict[sentiment] = df[df[sentiment]]['Word'].tolist()
    
    return sentiment_dict
















