import pandas as pd
import nltk
import streamlit as st
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
import re

st.title('Womens Clothing E-Commerce Reviews - Text Analysis')
df = pd.read_csv('WomensClothingE-CommerceReviews.csv')


# def tokenize_text(text):
#     tokens = word_tokenize(text.lower() if text.isalpha())
#     tokens = [token for token in tokens if token.isalnum()]
#     return tokens
# def stem_tokens(tokens):
#     stemmer = PorterStemmer()
#     stemmed_tokens = [stemmer.stem(token) for token in tokens]
#     return stemmed_tokens
# def remove_stopwords(tokens):
#     filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
#     return filtered_tokens

# def lemmatize_tokens(tokens):
#     lemmatizer = WordNetLemmatizer()
#     lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
#     # cleaned_tokens = [re.sub(r'[^a-zA-Z]', '', token) for token in lemmatized_tokens if token.isalpha()]
#     return lemmatized_tokens
# df['Review Text'] = df['Review Text'].apply(tokenize_text)
# df['Review Text'] = df['Review Text'].apply(remove_stopwords)
# df['Review Text'] = df['Review Text'].apply(stem_tokens)
# df['Review Text']  = df['Review Text'].apply(lemmatize_tokens)