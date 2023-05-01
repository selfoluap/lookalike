import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.title("Image Uploader")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)


if st.button("Search Image"):
    url = "http://localhost:5000/api"
    payload = {"key": "value"}


    with st.spinner("Searching Image..."):
        try:
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                st.success(f"POST request successful: {response.json()}")
            else:
                st.error(f"POST request failed with status code {response.status_code}: {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")
