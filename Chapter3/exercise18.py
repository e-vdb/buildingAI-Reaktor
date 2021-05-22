#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 10:17:07 2021

@author: Emeline

Exercise 18: TF-IDF

"""
import numpy as np
text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

text2 = '''he really really loves coffee
my sister dislikes coffee
my sister loves tea'''

def manhattan_distance(listA,listB):
    return np.sum(np.abs(listA-listB))

def main(text):
    # 1. split the text into words, and get a list of unique words that appear in it
    docs = [line.lower().split() for line in text.split('\n')]
    docsNb=len(docs)
    words=sorted(list(set([word.lower() for word in text.split()])))
    wordsNb=len(words)
                
    # 2. go over each unique word and calculate its term frequency, and its document frequency
    df = np.empty((1,len(words)), dtype=np.float) # contains document frequency
    tf = np.empty((docsNb,wordsNb), dtype=np.float) # contains term frequency
    
    for count,word in enumerate(words):
        occurence=0
        for i,doc in enumerate(docs):
            occInDoc=doc.count(word)
            tf[i][count]=occInDoc/len(doc)
            if occInDoc>0:
                occurence+=1
        df[0][count]=occurence/docsNb
    
    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector   
    tf_idf=tf*np.log10(1/df)

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.
    N=len(tf_idf)
    dist = np.empty((N, N), dtype=np.float)
    for i in range(N):
        for j in range(N):
            if i!=j:
                dist[i][j]=manhattan_distance(tf_idf[i],tf_idf[j])
            else:
                dist[i][j]=np.inf
    print(np.unravel_index(np.argmin(dist), dist.shape))
    
main(text)
