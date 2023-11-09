import streamlit as st
import time
import numpy as np
import ImageProcessing.Chapter3 as c3
import ImageProcessing.Chapter4 as c4
import ImageProcessing.Chapter5 as c5
import ImageProcessing.Chapter9 as c9
import cv2
import object_detection as od
from PIL import Image

st.set_page_config(page_title="Xử lý ảnh", page_icon="📈")

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://st.quantrimang.com/photos/image/2019/11/12/Hinh-Nen-Den-23.jpg");
    background-size: 100% 100%;
}
[data-testid="stHeader"]{
    background: rgba(0,0,0,0);
}
h3,h1 {
    text-align: center;
}
[data-testid="stToolbar"]{
    right:2rem;
}

}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)


st.markdown("# Xử lý ảnh")
st.write()

image_file = st.sidebar.file_uploader("Tải ảnh của bạn vào đây", type=[
                                  'jpg', 'png', 'jpeg', 'tif'])
global imgin
if image_file is not None:
    file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
    imgin = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE) 

    chapter_options = ["Chapter 3", "Chapter 4", "Chapter 5", "Chapter 9"]
    selected_chapter = st.sidebar.selectbox("Select an option", chapter_options)


    if selected_chapter == "Chapter 3":
        st.markdown("### Chương 3: Biến đổi độ sáng và lọc trong không gian")
        chapter3_options = ["Negative", "Logarit", "Power", "PiecewiseLinear", "Histogram", "HistogramEqualization",
                                                "HistogramEqualizationColor", "LocalHistogram", "HistogramStatistics", 
                                                "BoxFilter", "GaussFilter","Threshold", "MedianFilter", "Sharpen", "Gradient"]
        
        chapter3_selected = st.sidebar.selectbox("Select an option", chapter3_options)    
        if chapter3_selected  == "Negative":
            st.markdown("### 3.1: Negaive")
            st.markdown("##### Giới thiệu Negative: Hàm làm âm ảnh. Kết quả làm âm ảnh, trắng thành đen và ngược lại")
            processed_image = c3.Negative(imgin)
        elif chapter3_selected  == "Logarit":
            st.markdown("### 3.2: Logarit")
            st.markdown("##### Giới thiệu Logarit: Hàm xử lý ảnh bằng phương pháp Logarit. Kết quả: Sáng ít thì làm cho sáng nhiều. Đen nhiều thì cho đen ít")
            processed_image = c3.Logarit(imgin)
        elif chapter3_selected  == "Power":
            st.markdown("### 3.3: Power")
            st.markdown("##### Giới thiệu Power: Hàm xử lý ảnh bằng phương pháp luỹ thừa hình ảnh. Kết quả hàm Power: Làm cho ảnh trở nên tối hơn, hay sáng hơn,..")
            processed_image = c3.Power(imgin)
        elif chapter3_selected  == "PiecewiseLinear":
            st.markdown("### 3.4: PiecewiseLinear: Biến đổi tuyến tính từng phần")
            st.markdown("##### Giới thiệu PiecewiseLinear: Hàm xử lý ảnh bằng phương pháp Piecewise. Kết quả: kéo dài độ tương phản, phạm vi và mức cường độ sáng hơn")
            processed_image = c3.PiecewiseLinear(imgin)
        elif chapter3_selected  == "Histogram":
            st.markdown("### 3.5: Histogram")
            st.markdown("##### Giới thiệu Histogram: Hàm thống kê mô tả phân bố tần số xuất hiện của các mức xám trong một hình ảnh, biểu thị  số lượng pixel có cùng mức xám trên trục ngang và tần suất xuất hiện của mỗi mức xám trên trục dọc")
            processed_image = c3.Histogram(imgin)
        elif chapter3_selected  == "HistogramEqualization":
            st.markdown("### 3.6: HistogramEqualization: Cân bằng Histogram")
            st.markdown("##### Giới thiệu HistogramEqualization: Hàm xử lý ảnh để tăng cường độ tương phản và cân bằng phân bố mức xám trong hình ảnh. kết quả: Hình ảnh cải thiện độ tương phản, mức xám được phân bố đồng đều và tỷ lệ tần suất xuất hiện của các mức xám trở nên cân đối")
            processed_image = c3.HistEqual(imgin)
        elif chapter3_selected == "HistogramEqualizationColor":
            imgin = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            st.markdown("### 3.7: HistogramEqualizationColor: Cân bằng Histogram của ảnh màu")
            st.markdown("##### Giới thiệu HistogramEqualizationColor: Hàm cân bằng histogram cho ảnh màu, nhằm cải thiện độ tương phản và phân bố màu của ảnh. Kết quả của Histogram Equalization Color là ảnh được cân bằng histogram màu")
            processed_image = c3.HistEqualColor(imgin)
        elif chapter3_selected  == "LocalHistogram":
            st.markdown("### 3.8: LocalHistogram")
            st.markdown("##### Giới thiệu LocalHistogram: Hàm xử lý ảnh bằng phương pháp LocalHistogram. kết quả hàm LocalHistogram: làm rõ 1 vùng trong ảnh  ")
            processed_image = c3.LocalHist(imgin)
        elif chapter3_selected  == "HistogramStatistics":
            st.markdown("### 3.9: HistogramStatistics: Thống kê Histogram")
            st.markdown("##### Giới thiệu HistogramStatistics: Hàm xử lý ảnh bằng phương pháp HistogramStatistics. Kết quả hàm: thống kê 1 vùng trong ảnh")
            processed_image = c3.HistStat(imgin)
        elif chapter3_selected  == "BoxFilter":
            st.markdown("### 3.10: BoxFilter")
            st.markdown("##### Giới thiệu BoxFilter: Hàm làm mờ hoặc làm trơn ảnh bằng cách áp dụng một bộ lọc có hình dạng hộp chữ nhật trên các pixel của ảnh. Kết quả: Ảnh được làm mờ")
            processed_image = c3.BoxFilter(imgin)
        elif chapter3_selected  == "GaussFilter":
            st.markdown("### 3.11: GaussFilter")
            st.markdown("##### Giới thiệu GaussFilter: Hàm làm mờ hoặc làm trơn ảnh bằng cách áp dụng một bộ lọc Gauss (bộ lọc Gaussian) trên các pixel của ảnh. Kết quả của GaussFilter là ảnh được làm mờ một cách tự nhiên, với các chi tiết cục bộ giảm đi và độ tương phản giảm")
            processed_image = c3.GaussFilter(imgin)
        elif chapter3_selected  == "Threshold":
            st.markdown("### 3.12: Threshold: Phân ngưỡng")
            st.markdown("##### Giới thiệu Threshold: Hàm phân loại các pixel trong ảnh thành hai nhóm dựa trên một giá trị ngưỡng (threshold value) cho trước. Kết quả của Threshold là ảnh được chia thành hai vùng: vùng trắng và vùng đen")
            processed_image = c3.Threshold(imgin)
        elif chapter3_selected  == "MedianFilter":
            st.markdown("### 3.13: MedianFilter")
            st.markdown("##### Giới thiệu MedianFilter: Hàm xử lý ảnh bằng phương pháp MedianFilter. Kết quả hàm: Lọc nhiều ảnh, lọc các điểm nhiễu ảnh")
            processed_image = c3.MedianFilter(imgin)
        elif chapter3_selected  == "Sharpen":
            st.markdown("### 3.13: Sharpen")
            st.markdown("##### Giới thiệu Sharpen: Hàm làm tăng độ rõ nét và độ tương phản của các chi tiết trong ảnh. Kết quả: một ảnh mới có độ rõ nét và độ tương phản cao hơn so với ảnh gốc")
            processed_image = c3.Sharpen(imgin)
        elif chapter3_selected  == "Gradient":
            st.markdown("### 3.13: Gradient")
            st.markdown("##### Giới thiệu Gradient:  Hàm xử lý bằng phương pháp Gradient. Kết quả: Đạo hàm ống kính tách biên của ảnh")
            processed_image = c3.Gradient(imgin) 
            
                      
    elif selected_chapter == "Chapter 4":
        st.markdown("### Chương 4: Lọc trong miền tần số")
        chapter4_options = ["Spectrum", "FrequencyFilter", "DrawFilter", "RemoveMoire"]
        
        chapter4_selected = st.sidebar.selectbox("Select an option", chapter4_options)   
        
        
        if chapter4_selected == "Spectrum":
            st.markdown("### 4.1: Spectrum")
            st.markdown("##### Giới thiệu Spectrum: Giới thiệu Spectrum: Hàm xử lý ảnh bằng phương pháp phổ. Kết quả là phổ màu của ảnh. ")

            processed_image = c4.Spectrum(imgin)
        elif chapter4_selected == "FrequencyFilter":
            st.markdown("### 4.2: FrequencyFilter")
            st.markdown("##### Giới thiệu FrequencyFilter: Hàm xử lý ảnh bằng phương pháp lọc tần số. Kết quả là cho tín hiệu có tần số thấp hơn tần số cắt đã chọn và làm cho suy giảm tín hiệu có tần số cao hơn tần số cắt để xử lý ảnh.")
            processed_image = c4.FrequencyFilter(imgin)
        elif chapter4_selected == "DrawFilter":
            st.markdown("### 4.3: DrawFilter")
            st.markdown("##### Giới thiệu DrawFilter: Hàm xử lý ảnh bằng cách vẽ các bộ lọc trên không gian tần số. ")
            imgin = Image.new('RGB', (5, 5),  st.get_option("theme.backgroundColor"))
            processed_image = c4.DrawNotchRejectFilter()
        elif chapter4_selected == "RemoveMoire":
            st.markdown("### 4.4: RemoveMoire: Xoá nhiễu Moire")
            st.markdown("##### Giới thiệu RemoveMoire: Hàm xử lý ảnh để loại bỏ hiện tượng moiré. Kết quả: moiré đã được giảm thiểu hoặc loại bỏ, từ đó cải thiện độ rõ nét và chất lượng của hình ảnh")

            processed_image = c4.RemoveMoire(imgin)
            

    elif selected_chapter == "Chapter 5":
        st.markdown("### Chương 5: Khôi phục ảnh")
        chapter5_options = ["CreateMotionNoise", "DenoiseMotion", "DenoisestMotion"]
        chapter5_selected = st.sidebar.selectbox("Select an option", chapter5_options)   
        
        if chapter5_selected == "CreateMotionNoise":
            st.markdown("### 5.1: CreateMotionNoise: Tạo nhiễu chuyển động")
            st.markdown("##### Giới thiệu CreateMotionNoise: Giới thiệu CreateMotionNoise: Hàm tạo nhiễu chuyển động trên ảnh. Kết quả: một ảnh đã được tạo nhiễu chuyển động")
            processed_image = c5.CreateMotionNoise(imgin)
        elif chapter5_selected == "DenoiseMotion":
            st.markdown("### 5.2: DenoiseMotion: Gỡ nhiễu của ảnh có ít nhiễu")
            st.markdown("##### Giới thiệu DenoiseMotion: Hàm DenoiseMotion được sử dụng để loại bỏ nhiễu chuyển động từ một bức ảnh (ít nhiễu). Kết quả: ảnh sẽ được làm sạch khỏi nhiễu chuyển động và trở nên rõ ràng hơn ")
            processed_image = c5.DenoiseMotion(imgin)
        elif chapter5_selected == "DenoisestMotion":
            st.markdown("### 5.3: DenoisestMotion: Gỡ nhiễu của ảnh có nhiều nhiễu")
            st.markdown("##### Giới thiệu DenoisestMotion: Hàm DenoiseMotion được sử dụng để loại bỏ nhiễu chuyển động từ một bức ảnh (nhiều nhiễu). Kết quả: ảnh sẽ được làm sạch khỏi nhiễu chuyển động và trở nên rõ ràng hơn  ")
            temp = cv2.medianBlur(imgin, 7)
            processed_image = c5.DenoiseMotion(temp)   
            
                 
    elif selected_chapter == "Chapter 9":
        st.markdown("### Chương 9: Xử lý ảnh hình thái")
        chapter9_options = ["ConnectedComponent", "CountRice"]
        chapter9_selected = st.sidebar.selectbox("Select an option", chapter9_options)   
        
        if chapter9_selected  == "ConnectedComponent":
            st.markdown("### 9.1. ConnectedComponent: Đếm thành phần liên thông của miếng phi lê gà ")
            st.markdown("##### Giới thiệu ConnectedComponent: Phương pháp phân đoạn ảnh để tìm và nhóm các vùng liên thông trong ảnh dựa trên tính chất hình học hoặc màu sắc của các pixel. kết quả: đếm số lượng đối tượng trong ảnh ")
            processed_image = c9.ConnectedComponent(imgin)    
        elif chapter9_selected  == "CountRice":
            st.markdown("### 9.2: CountRice: Đếm hạt gạo (Count Rice)")
            st.markdown("##### Giới thiệu CountRice: Phương pháp đếm số hạt gạo ")

            processed_image = c9.CountRice(imgin)
    

    st.subheader("Ảnh gốc và ảnh đã xử lý")
    st.image([imgin, processed_image], width = 350)
st.button("Re-run")
