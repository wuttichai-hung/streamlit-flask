import streamlit as st
import pandas as pd
import requests

# Create a file upload widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# If an image is uploaded
if uploaded_file is not None:

    # Display the image
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

    # Make a POST request with the uploaded file
    url = "http://localhost:5000/predict"  # Replace with your own endpoint
    files = {"file": uploaded_file.getvalue()}
    with st.spinner('Model is predicting, Wait for it...'):
        response = requests.post(url, files=files).json()

    # Display the response
    st.write("Response")
    st.dataframe(pd.DataFrame(response['prediction'], columns=['class', 'score']))