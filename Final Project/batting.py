import streamlit as st
import pandas as pd
data = pd.read_csv("Batting.csv")

st.write(data)
