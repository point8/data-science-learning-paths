# This code is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).
# Copyright © [Point 8 GmbH](https://point-8.de)

import streamlit as st
import io
from PIL import Image
import base64
import pathlib

def add_logo():
    file = open(pathlib.Path(__file__).parent / "static/neps.png", "rb")
    contents = file.read()
    img_str = base64.b64encode(contents).decode("utf-8")
    buffer = io.BytesIO()
    file.close()
    img_data = base64.b64decode(img_str)
    img = Image.open(io.BytesIO(img_data))
    resized_img = img.resize((180, 80))  # x, y #450,200 
    resized_img.save(buffer, format="PNG")
    img_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    st.markdown(
        f"""
            <style>
                [data-testid="stSidebarNav"] {{
                    background-image: url('data:image/png;base64,{img_b64}');
                    background-repeat: no-repeat;
                    padding-top: 20px;
                    background-position: 20px 20px;
                }}
            </style>
        """,
        unsafe_allow_html=True,
    )


add_logo()

image = Image.open(pathlib.Path(__file__).parent / "static/energy.png")
st.image(image)