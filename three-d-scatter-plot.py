import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Define the dataset
data = {
    'TV': [230.1, 44.5, 17.2, 151.5, 180.8, 8.7, 57.5, 120.2, 8.6, 199.8, 66.1, 214.7, 23.8, 97.5, 204.1, 195.4, 67.8, 281.4, 69.2, 147.3],
    'Radio': [37.8, 39.3, 45.9, 41.3, 10.8, 48.9, 32.8, 19.6, 2.1, 2.6, 5.8, 24.0, 35.1, 7.6, 32.9, 47.7, 36.6, 39.6, 20.5, 23.9],
    'Newspaper': [69.2, 45.1, 69.3, 58.5, 58.4, 75.0, 23.5, 11.6, 1.0, 21.2, 24.2, 4.0, 65.9, 7.2, 46.0, 52.9, 114.0, 55.8, 18.3, 19.1],
    'Sales': [22.1, 10.4, 9.3, 18.5, 12.9, 7.2, 11.8, 13.2, 4.8, 10.6, 8.6, 17.4, 9.2, 9.7, 19.0, 22.4, 12.5, 24.4, 11.3, 14.6]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set title of the web app
st.title('Advertising Sales Analysis')

# Scatter plot
st.write("## Scatter plot between advertising channels and sales")
x_axis = st.selectbox('Select X-axis:', ['TV', 'Radio', 'Newspaper'])
y_axis = 'Sales'

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df[x_axis], df[y_axis], color='blue', alpha=0.5)
ax.set_xlabel(x_axis)
ax.set_ylabel(y_axis)
ax.set_title(f'{x_axis} vs {y_axis}')
st.pyplot(fig)

# Summary statistics
st.write("## Summary Statistics")
st.write(df.describe())

# Correlation matrix
st.write("## Correlation Matrix")
st.write(df.corr())
