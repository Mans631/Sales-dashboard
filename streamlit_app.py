import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('train.csv')

# Convert 'Order Date' to datetime with the correct format before filtering
data['Order Date'] = pd.to_datetime(data['Order Date'], format='%d/%m/%Y') # Use the correct format '%d/%m/%Y'

# Sidebar filters
region = st.sidebar.selectbox('Select a Region:', data['Region'].unique())
filtered_data = data[data['Region'] == region]

# Sales by Product
product_sales = filtered_data.groupby('Product Name')['Sales'].sum()

# Display sales by product
st.title('Sales Dashboard')
st.subheader(f'Sales in {region}')
st.bar_chart(product_sales)

# Monthly sales trend
# Already converted, so this is unnecessary:
# data['Order Date'] = pd.to_datetime(data['Order Date']) 
data['Month'] = data['Order Date'].dt.to_period('M')
monthly_sales = data.groupby('Month')['Sales'].sum()

# Plot sales trend
st.line_chart(monthly_sales)
