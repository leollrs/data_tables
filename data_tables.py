import streamlit as st
import pandas as pd

st.title("Individual Data Tables")

# Load and display the Grants Data table
try:
    grants_df = pd.read_csv("grants_data.csv")
    st.header("Grants Data")
    st.dataframe(grants_df)
except Exception as e:
    st.error(f"Error loading grants_data.csv: {e}")

# Load and display the Subastas Data table
try:
    subastas_df = pd.read_csv("subastas_data.csv")
    st.header("Subastas Data")
    st.dataframe(subastas_df)
except Exception as e:
    st.error(f"Error loading subastas_data.csv: {e}")

# Load and display the Licitaciones Data table
try:
    licitaciones_df = pd.read_csv("licitaciones_data.csv")
    st.header("Licitaciones Data")
    st.dataframe(licitaciones_df)
except Exception as e:
    st.error(f"Error loading licitaciones_data.csv: {e}")
