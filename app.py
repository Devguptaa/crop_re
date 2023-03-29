import streamlit as st
import pandas as pd
import pickle
import requests
import numpy as np
from sklearn.naive_bayes import GaussianNB
movie_dict = pickle.load(open('NBClassifier.pkl', 'rb'))
# movies = pd.DataFrame(movie_dict)
def recommend(a,b,c,d,e,f,g):
    data = np.array([[a,b,c,d,e,f,g]])
    prediction = movie_dict.predict(data)
    return prediction
a=st.number_input('Enter Nitrogen')
b=st.number_input('Enter Phosphorus')
c=st.number_input('Enter Pottasium')
d=st.number_input('Enter Temperature')
e=st.number_input('Enter Humidity')
f=st.number_input('Enter Ph')
g=st.number_input('Enter Rainfall')

if st.button('Recommend'):
    p=recommend(a,b,c,d,e,f,g)
    st.text(p[0])