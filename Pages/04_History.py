import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title='Predict Customer Churn!',
    page_icon='🔮',
    layout='wide'
)

def display_history_prediction():

    csv_path = "Data/history.csv"
    csv_exists = os.path.exists(csv_path)

    if csv_exists:
        history = pd.read_csv(csv_path)
        history = history.drop('Unnamed: 0', axis =1)
        st.dataframe(history)


if __name__ == '__main__':
    st.title('History Page')
    display_history_prediction()