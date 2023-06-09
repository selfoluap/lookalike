import streamlit as st
import requests
from io import BytesIO
import base64
from PIL import Image

st.title("Image Uploader")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = image.convert("RGB")  # Convert to RGB mode
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    image_bytes = buffered.getvalue()
    img_b64 = base64.b64encode(image_bytes).decode('utf-8')
    st.image(image, caption="Uploaded Image", use_column_width=True)

if st.button("Search Image"):
    url = "http://localhost:5000/api"

    payload = {'image': img_b64}

    with st.spinner("Searching Image..."):
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                st.success(f"POST request successful: {response.json()}")
            else:
                st.error(f"POST request failed with status code {response.status_code}: {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")
