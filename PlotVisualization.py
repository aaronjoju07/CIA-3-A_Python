import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('WomensClothingE-CommerceReviews.csv')

st.title('3D palot visualization')
st.subheader("Data Set")
st.dataframe(df)

st.title('Filter')
col = st.selectbox('Select Department Name', df['Department Name'].unique())
col1 = st.selectbox('Select Division Name', df['Division Name'].unique())
col2 = st.selectbox('Select Class Name', df['Class Name'].unique())


filtered_df = df[(df['Department Name'] == col) & 
                 (df['Division Name'] == col1) & 
                 (df['Class Name'] == col2)]

st.dataframe(filtered_df)
#3D Plot
st.title('3D Plot')
fig = plt.figure(figsize=(10, 5))
ax = plt.axes(projection='3d')
ax.scatter3D(df['Age'], df['Rating'], df['Positive Feedback Count'], color='green')
ax.set_xlabel('Age')
ax.set_ylabel('Rating')
ax.set_zlabel('Positive Feedback Count')
st.pyplot(fig)
