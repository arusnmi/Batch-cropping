import streamlit as st

st.title("Batch Image Cropper")
st.write(
    "This is a tool used for cropping images in batch using the autocrop library."
)
st.write("Upload your images below:")

uploaded_files = st.file_uploader(
    "Choose image files", accept_multiple_files=True, type=["jpg", "jpeg", "png"]
)

print (uploaded_files)