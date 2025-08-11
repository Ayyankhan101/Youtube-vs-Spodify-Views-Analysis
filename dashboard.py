import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('Spotify Youtube Dataset.csv.gz', compression='gzip')
    return df

df = load_data()

st.title('Spotify Youtube Analysis Dashboard')

st.sidebar.header('Filter Options')
danceability_range = st.sidebar.slider('Filter by Danceability', 0.0, 1.0, (0.0, 1.0))
df_filtered = df[(df['Danceability'] >= danceability_range[0]) & (df['Danceability'] <= danceability_range[1])]

energy_range = st.sidebar.slider('Filter by Energy', 0.0, 1.0, (0.0, 1.0))
df_filtered = df_filtered[(df_filtered['Energy'] >= energy_range[0]) & (df_filtered['Energy'] <= energy_range[1])]

loudness_range = st.sidebar.slider('Filter by Loudness', -60, 0, (-60, 0))
df_filtered = df_filtered[(df_filtered['Loudness'] >= loudness_range[0]) & (df_filtered['Loudness'] <= loudness_range[1])]

st.header('Dataset Overview')
st.dataframe(df_filtered.head())


st.header('Data Description')
st.dataframe(df_filtered.describe())


st.header('Correlation Analysis')
correlation_matrix = df_filtered[['Danceability', 'Energy', 'Loudness', 'Speechiness', 'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo', 'Views', 'Likes', 'Comments', 'Stream']].corr()
st.dataframe(correlation_matrix)
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
st.header('Correlation Heatmap')
st.pyplot(plt)

st.header('Distribution of Key Features')
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
sns.histplot(df_filtered['Danceability'], ax=axes[0], kde=True, color='blue')
sns.histplot(df_filtered['Energy'], ax=axes[1], kde=True, color='orange')
sns.histplot(df_filtered['Valence'], ax=axes[2], kde=True, color='green')
st.pyplot(fig)

st.header('Spotify Streams vs. YouTube Views')
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df_filtered, x='Stream', y='Views', ax=ax , alpha=0.6, edgecolor=None, s=50,hue='Danceability', palette='viridis')
st.pyplot(fig)
