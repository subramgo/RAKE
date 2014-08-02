# -*- coding: utf-8 -*-
"""
Created on Sat Aug 02 10:04:35 2014

A simple implementation of RAKE Algorithm for keyword extraction
Automatic keyword extraction from individual documents
Stuart Rose, Dave Engel, Nick Cramer
and Wendy Cowley


@author: gsubramanian
"""
import nltk
from nltk.corpus import stopwords
from collections import defaultdict

contents = open('sample.txt','r').read()

sentences = nltk.sent_tokenize(contents.lower())

phrases = []

for line in sentences:
    words = nltk.word_tokenize(line)
    phrase = ''
    for word in words:
        if word not in stopwords.words('english') and word not in [',','.','?',':',';']:
            phrase+=word + ' '
        else:
            if phrase != '':
                phrases.append(phrase.strip())
                phrase = ''

print '******** Candidate Phrases **********************'
print phrases

word_freq = defaultdict(int)
word_degree = defaultdict(int)
word_score = defaultdict(float)

for phrase in phrases:
    words = phrase.split(' ')
    phrase_length = len(words)
    for word in words:
        word_freq[word]+=1
        word_degree[word]+=phrase_length


for word,freq in word_freq.items():
    degree = word_degree[word]
    score = ( 1.0 * degree ) / (1.0 * freq )
    word_score[word] = score

phrase_scores = defaultdict(float)


for phrase in phrases:
    words = phrase.split(' ')
    score = 0.0
    for word in words:
        score+=word_score[word]
    phrase_scores[phrase] = score

print '******** Candidate Phrases scored ****************'
for k in sorted(phrase_scores,key = phrase_scores.get,reverse=True):
    print k,phrase_scores[k]
    