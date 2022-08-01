import streamlit as st
import pandas as pd
import folium
  
df=pd.read_csv('whs2021.csv')
st.header('UNESCO World Heritage Sites')
fm=folium.Map()
for _, row in df.iterrows():
    folium.Marker([row['latitude'],row['longitude']]).add_to(fm)
st.write(fm)
st.dataframe(df)

col1, col2 = st.columns([1,1])
with col1:
    st.dataframe(df.Region.value_counts())
  
with col2:
    st.dataframe(df['Country name'].value_counts().head(7))
#
