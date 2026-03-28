import streamlit as st
import pandas as pd

# 页面标题
st.title("Movie Recommendation System")
st.subheader("Student ID: 0390769")

# 说明文字
st.write("This application is successfully deployed on Streamlit!")

# 电影示例数据
movies = {
    "Movie Name": ["The Matrix", "Titanic", "Inception", "Avatar"],
    "Genre": ["Action", "Romance", "Sci-Fi", "Adventure"],
    "Release Year": [1999, 1997, 2010, 2009]
}

df = pd.DataFrame(movies)

st.dataframe(df)

st.success("App is running successfully!")
