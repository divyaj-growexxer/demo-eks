import cv2
import numpy as np
from PIL import Image
import streamlit as st

def get_laplacian_score(image):
    """Calculates the Laplacian score for sharpness detection."""
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    return laplacian_var

def is_blurred(image, threshold=85):
    """Checks if an image is blurred based on Laplacian variance."""
    laplacian_var = get_laplacian_score(image)
    return laplacian_var < threshold, laplacian_var

def main():
    st.title("Blur Detection Tool")
    
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "webp", "avif"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)  # Updated line
        
        is_blur, laplacian_score = is_blurred(image)
        
        st.write(f"Laplacian Score: {laplacian_score:.2f}")
        
        if is_blur:
            st.error("The image is blurred.")
        else:
            st.success("The image is not blurred.")

if __name__ == "__main__":
    main()
