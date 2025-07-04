import streamlit as st
from PIL import Image
import cv2
import numpy as np
from backend import *

filter_info = {
    "Edge Detection": """
        **Edge Detection** detects sharp changes in image brightness, known as edges. 
        It’s used to identify object boundaries. Algorithms like Canny work by 
        detecting intensity gradients.
    """,
    "Grayscale": """
        **Grayscale** converts a color image into shades of gray by removing color information. 
        It simplifies analysis by reducing data complexity.
    """,
    "Negative Transformation": """
        **Negative Transformation** inverts the colors of an image by subtracting each 
        pixel value from 255. It enhances details in dark regions.
    """,
    "Gaussian Blur": """
        **Gaussian Blur** smooths the image using a Gaussian kernel, which helps in 
        reducing noise and detail. Useful in preprocessing.
    """,
    "Reduce Noise": """
        **Reduce Noise** uses Non-Local Means to remove grain/noise while preserving detail.
    """,
    "Sharping": """
        **Sharpening** enhances fine details and edges by increasing contrast using a kernel filter.
    """
}

def main():
    st.header("Welcome to PixCart")
    image_upload = st.file_uploader("Please upload an image file", type=['jpg', 'png', 'jpeg'])

    if image_upload is not None:
        image = Image.open(image_upload)
        image_cv2 = np.array(image)

        # Convert RGBA to RGB if needed
        if image_cv2.shape[-1] == 4:
            image_cv2 = cv2.cvtColor(image_cv2, cv2.COLOR_RGBA2RGB)

        option = st.selectbox('Select your filter', (
            'Select',
            'Edge Detection',
            'Grayscale',
            'Negative Transformation',
            'Gaussian Blur',
            'Reduce noise',
            'Sharping',
            # 'Affine Transform'  # Optional
        ))

        st.write('You selected:', option)

        if option == 'Select':
            st.image(image, caption="Original Image")

        elif option == 'Edge Detection':
            st.header('Edge Detection')
            st.image(image, caption="Original Image")
            st.image(edge_detetion(image_cv2), caption="Edge Detected Image")

            # 📘 Explanation Block
            with st.expander("🔍 What does this filter do?"):
                st.markdown(filter_info["Edge Detection"])

        elif option == 'Grayscale':
            st.header('Grayscale')
            st.image(image, caption="Original Image")
            st.image(gray_scale(image_cv2), caption="Grayscale Image")

            # 📘 Explanation Block
            with st.expander("🔍 What does this filter do?"):
                st.markdown(filter_info["Grayscale"])

        elif option == 'Negative Transformation':
            st.header('Negative Transformation')
            st.image(image, caption="Original Image")
            st.image(neg_trans(image_cv2), caption="Negative Image")

            # 📘 Explanation Block
            with st.expander("🔍 What does this filter do?"):
                st.markdown(filter_info["Negative Transformation"])

        elif option == 'Gaussian Blur':
            st.header('Gaussian Blur')
            st.image(image, caption="Original Image")
            st.image(gaussian_blur(image_cv2), caption="Blurred Image")

            # 📘 Explanation Block
            with st.expander("🔍 What does this filter do?"):
                st.markdown(filter_info["Gaussian Blur"])

        elif option == 'Reduce noise':
            st.header('Reduce Noise')
            st.image(image, caption="Original Image")
            st.image(reduce_noise(image_cv2), caption="Denoised Image")

            # 📘 Explanation Block
            with st.expander("🔍 What does this filter do?"):
                st.markdown(filter_info["Reduce Noise"])

        elif option == 'Sharping':
            st.header('Sharpening')
            st.image(image, caption="Original Image")
            st.image(sharp_image(image_cv2), caption="Sharpened Image")

            # 📘 Explanation Block
            with st.expander("🔍 What does this filter do?"):
                st.markdown(filter_info["Sharping"])


if __name__ == "__main__":
    main()
