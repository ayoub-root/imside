#!/usr/bin/env python
# coding: utf-8
#preprocessing
#import libriries
# In[11]:


import nltk
import re
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
import matplotlib.pyplot as plt
import json
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
warnings.filterwarnings("ignore")

##read dataset
# In[12]:


with open("data/ProgrammWebScrapy.txt", 'rb') as data:
    df = pd.read_json(data)


# In[13]:


#shows first lines
df['Description']


# In[14]:


#shows columns
df.columns


# In[15]:


# remove ponctuation 
punctuation_signs = list("?:!.,;({[&#<>]})'1234567890\"")
print(punctuation_signs)
stop_words = list(stopwords.words('english'))###########################
def clean_text():
    # Dataframe creation
    lemmatized_text_list = []
    data = pd.DataFrame(df)
   # print(data['Description'])
   # df.loc[0] = text
    data['Content_Parsed_1'] = data['Description'].str.replace("\r", " ")
    data['Content_Parsed_1'] = data['Content_Parsed_1'].str.replace("\n", " ")
    data['Content_Parsed_1'] = data['Content_Parsed_1'].str.replace("    ", " ")
    data['Content_Parsed_1'] = data['Content_Parsed_1'].str.replace('"', '')
    data['Content_Parsed_1'] = data['Content_Parsed_1'].str.lower()
    data['Content_Parsed_1'] = data['Content_Parsed_1']
    #print(data['Content_Parsed_1'][157])
    for punct_sign in punctuation_signs:
        data['Content_Parsed_1'] = data['Content_Parsed_1'].str.replace(punct_sign, '')
    #print(data['Content_Parsed_1'][157])
    data['Content_Parsed_1'] = data['Content_Parsed_1'].str.replace("'s", "")
    data['Content_Parsed_1'] = data['Content_Parsed_1'].str.replace("s'", "")
    
   #####################################################################
    wordnet_lemmatizer = WordNetLemmatizer()
    #########################
    nrows = len(data)
    lemmatized_text_list = []
    for row in range(0, nrows):
        # Create an empty list containing lemmatized words
        lemmatized_list = []
        # Save the text and its words into an object
        text = data.loc[row]['Content_Parsed_1']
        text_words = text.split(" ")
        # Iterate through every word to lemmatize
        for word in text_words:
            lemmatized_list.append(wordnet_lemmatizer.lemmatize(word, pos="v"))
        # Join the list
        lemmatized_text = " ".join(lemmatized_list)
        # Append to the list containing the texts
        lemmatized_text_list.append(lemmatized_text)
    data['Content_Parsed_1'] = lemmatized_text_list
    data['Content_Parsed_1'] = data['Content_Parsed_1']
    data['Content_Parsed_1'].replace('', np.nan,inplace=True)
   # df['Tenant'].replace('', np.nan, inplace=True)
    #data['Content_Parsed_6'] = data['Content_Parsed_6'].str.replace("  ", " ")
    for stop_word in stop_words:
        regex_stopword = r"\b" + stop_word + r"\b"
        data['Content_Parsed_1'] = data['Content_Parsed_1'].str.replace(regex_stopword,'')
    data['Content_Parsed_1'] =  data['Content_Parsed_1'].str.replace("\s\s+", ' ')
   # data = data['Content_Parsed_6']
    code_cat={}
    data.fillna('unknow', inplace=True)
    #data.dropna(subset=['Content_Parsed_6'])
   # data.loc[350]['data']="no description"
    data.loc[350]
    for i, val in enumerate(data['PrimaryCategory'].unique()):
       # print(i)
        code_cat[str(val)] = i
    data['class_code'] = data['PrimaryCategory']
    data = data.replace({'class_code':code_cat})
    data = data.rename(columns={'Content_Parsed_1': 'data','Title':'name','PrimaryCategory':'class_1','SecondaryCategories':'class_2'})
    dataset=pd.DataFrame(data)#,columns=['data','name','class_1','class_code','class_2']
    dataset=dataset.drop('Description', 1)
    #return data
##############################################################################
    # TF-IDF
   # print(dataset.head())
    return dataset

    
dataset=clean_text()


# In[16]:


print(dataset.loc[352]['class_code'])


# In[17]:




# In[18]:


#dataset.to_csv('data/microservicesall.csv', encoding='utf-8', index=False, header=True)
dataset.to_json('data/temp.json', orient='records', lines=True)

# In[ ]:





# In[ ]:




