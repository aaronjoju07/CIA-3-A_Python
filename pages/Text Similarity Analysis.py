import pandas as pd
import numpy as np
import nltk
import streamlit as st
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
import re



st.title("Womens Clothing E-Commerce Reviews Similarity Analysis")

df = pd.read_csv('WomensClothingE-CommerceReviews.csv')

any_missing_in_columns = df.isnull().any()


df['Division Name']=df['Division Name'].fillna(df['Division Name'].mode()[0])

df['Review Text']=df['Review Text'].fillna('.')

def lowercase(text):
    text = text.lower()
    return(text)

def punctuation(text):
    text = re.sub(r'[^\w\s]', '', text)
    return(text)

    
def tokenize(text):
    tokens = word_tokenize(text)
    return(tokens)
    
def stopword(tokens):
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    preprocessed_text = ' '.join(tokens)
    # st.write(preprocessed_text)
    return(preprocessed_text)

df['lowercase']= df['Review Text'].apply(lowercase)
df['punctuation'] = df['lowercase'].apply(punctuation)
df['tokenized'] = df['punctuation'].apply(tokenize)
df['review_text_preprocessed'] = df['tokenized'].apply(stopword)

st.header("Preprocessed Review Text")

st.write(df['review_text_preprocessed'])

st.header('Jaccard Similarity')
#do df['review_text_preprocessed'] using jaccard similarity identidy the text similarity for General,GeneralPetite and Initmate from the "Division Name" Column
