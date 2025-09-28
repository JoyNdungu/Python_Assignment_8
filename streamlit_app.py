# streamlit_app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# -----------------
# Load and clean data
# -----------------

def load_data():
    df = pd.read_csv("metadata.csv")

    # Clean publish_time
    df = df.dropna(subset=['publish_time'])
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year

    return df

df = load_data()

# -----------------
# Streamlit Layout
# -----------------
st.title("📊 CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Filter by year range
years = df['year'].dropna().astype(int)
min_year, max_year = years.min(), years.max()
year_range = st.slider("Select year range:", min_year, max_year, (2020, 2021))

filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Publications by Year
st.subheader("Publications by Year")
year_counts = filtered['year'].value_counts().sort_index()
st.bar_chart(year_counts)

# Top Journals
st.subheader("Top Journals")
top_journals = filtered['journal'].value_counts().head(10)
st.bar_chart(top_journals)

# Word Cloud of Titles
st.subheader("Word Cloud of Titles")
titles = " ".join(filtered['title'].dropna().tolist())
if titles.strip():
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)
    st.image(wordcloud.to_array())
else:
    st.write("No titles available in the selected range.")

# Show Sample Data
st.subheader("Sample Data")
st.write(filtered[['title','journal','publish_time']].head(20))
