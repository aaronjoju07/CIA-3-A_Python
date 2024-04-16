import streamlit as st
from PIL import Image

# take image input from user in streamlit
st.title("Image Processing")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
#Resize image and display
if st.button('Resize'):
    image = image.resize((100,100))
    st.image(image, caption='Resized Image.resize((100,100)', use_column_width=True)

#Convert image to grayscale and display
if st.button('Grayscale'):
    image = image.convert('L')
    st.image(image, caption='Grayscale Image.', use_column_width=True)

#Crop the image and display
if st.button('Crop'):
    image = image.crop((0, 0, 256, 256))
    st.image(image, caption='Cropped Image.crop((0, 0, 256, 256)', use_column_width=True)

#Rotate the image and display
if st.button('Rotate'):
    image = image.rotate(60)
    st.image(image, caption='Rotated Image.rotate(60)', use_column_width=True)
