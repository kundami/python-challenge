
import os
import csv
import string
import re
from nltk import tokenize

# Finding the info to some of netlfix's most popular videos
#files = ['1']
files = ['1','2']


for filename_ext in files:
    tokens = []
    newline = 0

    print("processing File :"+"paragraph_"+filename_ext+".txt")
    txtpath = os.path.join('Resources', 'paragraph_'+filename_ext+'.txt')

    # Improved Reading using CSV module

    with open(txtpath) as textfile:
        paragraph = textfile.read().replace("\n"," ")
       # tokens.append(re.split('(\W+)', str(paragraph)))
        tokens = re.split(r' ', str(paragraph))
        letter_counts = []
        for token in tokens:
            letter_counts.append(len(token))
        #print(tokens)
        word_count=len(tokens)
        #print ("word len "+str(word_count))
        average_letter_count = sum(letter_counts)/float(len(letter_counts))
        split_sentence = re.split("(?<=[.!?]) +",  str(paragraph) )
        sentence_count = len(split_sentence)
        
       
        wordlen_per_sentence = []
        for each_sentence in split_sentence:
        # print( "-------------\n")
            #print( each_sentence +"\n")
            words_per_sentence = []
            words_per_sentence =  re.split(" ",  str(each_sentence) )
            #print ( words_per_sentence )
            wordlen_per_sentence.append(len(words_per_sentence))
        
        average_sentence_length = sum(wordlen_per_sentence)/float(len(wordlen_per_sentence))
        #print ("Approximate sentence count:"+str(newline) +" out of tokens"+str(len(tokens)))

# Assess the passage for each of the following:

        print("Approximate word count for file paragraph_"+filename_ext+".txt-------------\n")
        print (str(word_count))
        print("Approximate letter count (per word)")
        print(str(average_letter_count))
        print("Average sentence length (in words)\n")
        print(str(average_sentence_length))
         
 