import streamlit as st
import time
import numpy as np
import cv2 as cv
import object_detection as od
import FaceDetection.Haarcascade.app as ha
import FaceDetection.Facebook.face_detect as fb
from PIL import Image

st.set_page_config(page_title="Phát hiện khuôn mặt", page_icon="📈")


page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://free4kwallpapers.com/uploads/originals/2015/11/03/wonderful-lighthouse-sea-%E2%80%8B%E2%80%8Bwaves-in-fog-wallpaper.jpg");
    background-size: 100% 100%;
}
[data-testid="stHeader"]{
    background: rgba(0,0,0,0);
}
[data-testid="stToolbar"]{
    right:2rem;
}
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)

st.markdown("# Phát hiện khuôn mặt")

options = ["Facebook", "Haarcascade"]
selected_chapter = st.sidebar.selectbox("Lựa chọn phương thức phát hiện: ", options)

if selected_chapter == "Facebook":
    fb.main_loop()
elif selected_chapter == "Haarcascade":
    ha.main_loop()


st.button("Re-run")
