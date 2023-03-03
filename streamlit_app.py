import streamlit as st
import requests
url = "http://localhost:5000/"

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    file_path = uploaded_file.name
    with open(file_path, 'wb') as f:
        f.write(bytes_data)
    res = requests.post(url, files={'file': open(file_path, 'rb')})
    st.write(res.json())
