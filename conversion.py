import streamlit as st
import pandas as pd

st.title("Data Type Conversion in Pandas (Streamlit)")

# Create DataFrame
df = pd.DataFrame({
    'Product': ['A', 'B', 'A', 'C', 'B'],
    'Sales': ['100', '150', '200', '180', '120'],
    'Date': [
        '2024-01-01', '2024-01-02',
        '2024-01-03', '2024-01-04',
        '2024-01-05'
    ]
})

st.subheader("Original DataFrame")
st.dataframe(df)

st.subheader("Original Data Types")
st.write(df.dtypes)

# Convert data types
df['Sales'] = pd.to_numeric(df['Sales'])
df['Date'] = pd.to_datetime(df['Date'])
df['Product'] = df['Product'].astype('category')

st.subheader("DataFrame After Type Conversion")
st.dataframe(df)

st.subheader("Updated Data Types")
st.write(df.dtypes)
