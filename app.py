
import streamlit as st
from PIL import Image
from bobblehead_generator import generate_bobblehead_image

st.set_page_config(page_title="Bobblehead Generator", layout="centered")
st.title("🧠 Upload a Photo, Get a Bobblehead!")

uploaded_file = st.file_uploader("Upload your profile photo", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Photo", use_column_width=True)

    st.info("Generating your bobblehead...")

    bobblehead_bytes = generate_bobblehead_image(image)

    st.success("Here's your custom bobblehead!")
    st.image(bobblehead_bytes, caption="Bobblehead Result")

    st.download_button("Download PNG", bobblehead_bytes, file_name="bobblehead.png")
