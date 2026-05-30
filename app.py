import pickle
import streamlit as st  # ✅ removed wrong turtle import
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

nltk.download('punkt')        # ✅ required for word_tokenize
nltk.download('stopwords')    # ✅ required for stopwords

ps = PorterStemmer()

def data_preprocessing(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    
    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    
    text = y[:]
    y.clear()
    
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)

st.title("Email/SMS Spam Detection")  # ✅ moved outside the button click

input_sms = st.text_area("Enter the message")  # ✅ moved outside the button click
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if st.button("Predict"):
    tfidf_vectorizer = pickle.load(open(os.path.join(BASE_DIR, 'notebooks', 'vectorizer.pkl'), 'rb'))
    stacking_classifier = pickle.load(open(os.path.join(BASE_DIR, 'notebooks', 'stacking_classifier.pkl'), 'rb'))

    transformed_sms = data_preprocessing(input_sms)
    vector_input = tfidf_vectorizer.transform([transformed_sms]).toarray()
    result = stacking_classifier.predict(vector_input)

    if result[0] == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")