import numpy as np
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
data = pd.read_csv('Data/train.csv')  # Replace with your actual dataset path

# Set page configuration
st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")

# Dashboard title
st.title("Customer Churn Dashboard")

# Overview Section
st.header("Overview")
st.markdown("""
This dashboard provides insights into customer churn data, helping you understand the factors influencing churn and make data-driven decisions to improve customer retention.
""")

# Display key metrics side by side
total_customers = len(data)
churned_customers = (data['churn'] == 'Yes').sum()
churn_rate = (churned_customers / total_customers) * 100
avg_monthly_charge = data['monthlycharges'].mean()
avg_total_charge = data['totalcharges'].mean()
avg_tenure = data['tenure'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", total_customers)
col2.metric("Churned Customers", churned_customers)
col3.metric("Churn Rate", f"{churn_rate:.2f}%")

col4, col5, col6 = st.columns(3)
col4.metric("Avg Monthly Charge", f"${avg_monthly_charge:.2f}")
col5.metric("Avg Total Charge", f"${avg_total_charge:.2f}")
col6.metric("Avg Tenure (months)", f"{avg_tenure:.2f}")

# Churn Distribution
# st.header("Churn Distribution")
# fig, ax = plt.subplots()
# sns.barplot(x=data['churn'].value_counts().index, y=data['churn'].value_counts().values, ax=ax)
# ax.set_title('Churn Distribution')
# ax.set_xlabel('Churn')
# ax.set_ylabel('Count')
# st.pyplot(fig)

# Layout for the graphs
st.header("Churn Distribution & Customer Demographics")
col1, col2 = st.columns(2)
with col1:
    fig, ax = plt.subplots()
    sns.barplot(x=data['churn'].value_counts().index, y=data['churn'].value_counts().values, ax=ax)
    ax.set_title('Churn Distribution')
    ax.set_xlabel('Churn')
    ax.set_ylabel('Count')
    st.pyplot(fig)

# Gender Distribution
with col2:
    fig, ax = plt.subplots()
    sns.countplot(x='gender', data=data, ax=ax)
    ax.set_title('Gender Distribution')
    st.pyplot(fig)

# Service Usage
st.header("Service Usage")
col1, col2 = st.columns(2)

# Internet Service
with col1:
    fig, ax = plt.subplots()
    sns.countplot(x='internetservice', hue='churn', data=data, ax=ax)
    ax.set_title('Internet Service Usage by Churn')
    st.pyplot(fig)

# Phone Service
with col2:
    fig, ax = plt.subplots()
    sns.countplot(x='phoneservice', hue='churn', data=data, ax=ax)
    ax.set_title('Phone Service Usage by Churn')
    st.pyplot(fig)

