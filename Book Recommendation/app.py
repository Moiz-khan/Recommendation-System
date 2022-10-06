import streamlit as st
import pickle
import pandas as pd

st.title("Book Recommendation System")

def recommend(product_ID):
    correlation_product_ID = correlation_matrix[product_ID]
    recommend = list(X.index[correlation_product_ID > 0.90])
        
    bk_title = []
    for i in recommend[:5]:
        title = df[df.book_id == i][:1].book_title.item()
        bk_title.append(title)
    return bk_title

if __name__ == '__main__':
    book_dict = pickle.load(open('book_dict.pkl','rb'))
    df = pd.DataFrame(book_dict)
    correlation_matrix = pickle.load(open("correlation_matrix.pkl", "rb"))
    X = pickle.load(open("X.pkl", "rb"))

    selected_book_name = st.selectbox('Select the book name?', df['book_title'].unique())
    bookid =  df[df['book_title']== selected_book_name].index.values
    print(bookid[0])
    if st.button("Recommend"):
        recmd = recommend(bookid[0])
        for i in range(len(recmd)):
            st.write(i+1,'. ', recmd[i])
