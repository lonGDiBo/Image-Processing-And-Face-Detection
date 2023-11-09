import streamlit as st
import base64


st.set_page_config(
    page_title="Đồ án cuối kỳ",
    page_icon="🤖",
)

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://c4.wallpaperflare.com/wallpaper/429/879/798/nature-landscape-hd-wallpaper-preview.jpg");
    background-size: 100% 100%;
    
}
[data-testid="stHeader"]{
    background: rgba(0,0,0,0);
}
[data-testid="stToolbar"]{
    right:2rem;
}

h1, h2 ,h3{
    text-align: center;
}
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)

st.write("## Trường Đại Học Sư Phạm Kỹ Thuật TP.HCM")
st.write("## Đồ án cuối kỳ")
st.write("## Môn: Xử lý ảnh")
st.write("## Mã lớp : DIPR430685_22_2_10")
st.write("### Sinh viên thực hiện: Phạm Minh Long - 20133062")

st.markdown(
    """
    ## Giới thiệu đồ án
    ###### chức năng chính trong bài
    - Phát hiện khuôn mặt
    - Nhận dạng khuôn mặt của chính mình
    - Xử lý ảnh số (Gồm 4 chương:3, 4, 5, 9)

    
    """
)


