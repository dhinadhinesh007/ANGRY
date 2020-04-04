import numpy as np
from collections import defaultdict

class FeatureGen:
    def __init__(self,chapter= "",n_grams = 2):
        # chapter = prep-processed text doc
        self.text = chapter
        self.n_grams = n_grams
        # let this be lists of lists, where each feature value is stored in a list with indices corresponding to sentence number
        self.feature_vector_list =[]



    def setdoc(self, new_chapter):
        self.text = new_chapter

    def set_n_grams(self,new_ngram):
        self.n_grams = new_ngram

    def create_ngrams(tokens, n):
        ngrams = defaultdict(int)
        for ngram in (tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)):
            ngrams[ngram] += 1
        return ngrams

    def get_Topic_Sentence_Feature(self):

        title = ''
        title_ngrams = set()

        feature_val_list = []

        for sentence in self.text:
            tsentence = sentence.split(" ")
            first_word = tsentence[0]
            if first_word == '@':
                title_tokens = tsentence[2:]
                title_2grams = self.create_ngrams(title_tokens, 2)
                title_3grams = self.create_ngrams(title_tokens, 3)
                title_ngrams = set(title_2grams + title_3grams)

            else:

                sent_2grams = self.create_ngrams(tsentence, 2)
                sent_3grams = self.create_ngrams(tsentence, 3)
                sent_ngrams = set(sent_2grams + sent_3grams)
                feature_val = sent_ngrams.intersection(title_ngrams)
                feature_val_list.append(feature_val)


    def getfeaturevec(self,doc = None,setngrams = None):
        if doc is not "":
            self.text = doc

        if setngrams is not None:
            self.n_grams = setngrams


        # put your feature functions below
        self.feature_vector_list.append(self.get_Topic_Sentence_Feature)





        return np.array(self.feature_vector_list)








