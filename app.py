import streamlit as st
import pandas as pd
 
df=pd.read_csv('whs2021.csv')
st.header('UNESCO World Heritage Sites')
st.dataframe(df)
