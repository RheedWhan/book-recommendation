import numpy as np
import pandas as pd
import pickle
import streamlit as st

def recommend(book_name):    
    index = np.where(model.index == book_name)[0][0]
    distances = similarity[index]
    similar_items = sorted(list(enumerate(distances)), key=lambda x:x[1], reverse = True)[1:11]
    recommended_books = []
    for i in similar_items:
        recommended_books.append(model.index[i[0]])
    return recommended_books
        

loaded_model = pickle.load(open('C:\Users\Ojo Ridwan\Downloads\archive (13)\books.pkl' , 'rb'))
model = pd.DataFrame(loaded_model)

similarity = pickle.load(open('C:\Users\Ojo Ridwan\Downloads\archive (13)\similarity.pkl', 'rb'))


st.title('Books Recommender System')

selected_books_name = st.selectbox('Books', model.index.values)


if st.button('Recommend'):
    Recommendations = recommend(selected_books_name)
    for i in Recommendations:
        st.write(i)
    


        
        
    


