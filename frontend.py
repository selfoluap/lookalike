import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.title("Image Uploader")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("")

    # Call the Flask REST API using the POST method
    with st.spinner("Calling REST API..."):
        files = {"image": uploaded_file.getvalue()}
        response = requests.post("http://localhost:5000/api", files=files)
        print("Response: ", response)
        try:
            response_json = response.json()
            st.success("Your lookalike animal: " + response_json)
        except ValueError:
            st.error("Failed to decode JSON. Please check the response content.")