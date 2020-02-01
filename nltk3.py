#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import io #io interaction
import random
import string # to process standard python strings
import warnings 
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer  #Tf-Idf for frequency counting and sequencing
from sklearn.metrics.pairwise import cosine_similarity  #calculating the actual similarity using the above tf-idf
import warnings 
warnings.filterwarnings('ignore')

import nltk #nlp toolkit
from nltk.stem import WordNetLemmatizer #lemmatization of words (" identifying meaningful / choosing from similar words (stemming) " )


# In[ ]:


f=open(r'chat.txt','r',errors = 'ignore')
raw=f.read()                         #Corpus Reading...


# In[ ]:


#Tokenization ( "  breaking down / text preprocessing begins ")
sent_tokens=nltk.sent_tokenize(raw)
word_tokens=nltk.word_tokenize(raw)


# In[ ]:


#preprocessing  - lemmetization

lem= WordNetLemmatizer()

def LemTokens(tokens):
    return [lem.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)          #remove unwanted punctuations

def LemNormalize(text):                       #normalize what was lemmatized
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# In[ ]:


#Defaul keyword matching ! -- for user basic input [ Default ]

greeting_input = ("hello", "hi", "greetings", "sup", "what's up","hey",)
greeting_output = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me", "Hey ! , What's up ?"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in greeting_input:
            return random.choice(greeting_output)


# In[ ]:


#using of tdf-idf and cosine similarity to generate ouputs based on user input Vs corpus availablity

def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response


# In[ ]:


#ending - bot basic responses

flag=True
print("Bot: Hey. I will answer your queries about food. If you want to exit, type bye!") #train with X to answer! 
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("Bot: Sure Thing ! ")
        else:
            if(greeting(user_response)!=None):
                print("Bot: "+greeting(user_response))
            else:
                print("Bot: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("Bot: Bye! take care..")


# In[ ]:





# In[ ]:




