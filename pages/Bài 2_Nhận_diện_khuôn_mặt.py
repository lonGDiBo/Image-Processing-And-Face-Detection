import streamlit as st
import numpy as np
import cv2 as cv
import joblib

st.markdown("# Bài 1: Nhận diện khuôn mặt")
FRAME_WINDOW = st.image([])
cap = cv.VideoCapture(0)


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

svc = joblib.load('./FaceRecognition/svc.pkl')
mydict = ['Ban Long', 'ThayDuc']

def visualize(input, faces, fps, thickness=2):
    if faces[1] is not None:
        for idx, face in enumerate(faces[1]):
            #print('Face {}, top-left coordinates: ({:.0f}, {:.0f}), box width: {:.0f}, box height {:.0f}, score: {:.2f}'.format(idx, face[0], face[1], face[2], face[3], face[-1]))

            coords = face[:-1].astype(np.int32)
            cv.rectangle(input, (coords[0], coords[1]), (coords[0]+coords[2], coords[1]+coords[3]), (0, 255, 0), thickness)
            cv.circle(input, (coords[4], coords[5]), 2, (255, 0, 0), thickness)
            cv.circle(input, (coords[6], coords[7]), 2, (0, 0, 255), thickness)
            cv.circle(input, (coords[8], coords[9]), 2, (0, 255, 0), thickness)
            cv.circle(input, (coords[10], coords[11]), 2, (255, 0, 255), thickness)
            cv.circle(input, (coords[12], coords[13]), 2, (0, 255, 255), thickness)
    cv.putText(input, 'FPS: {:.2f}'.format(fps), (1, 16), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


if __name__ == '__main__':
    detector = cv.FaceDetectorYN.create(
        './FaceRecognition/face_detection_yunet_2022mar.onnx',
        "",
        (320, 320),
        0.9,
        0.3,
        5000)
    
    recognizer = cv.FaceRecognizerSF.create(
    './FaceRecognition/face_recognition_sface_2021dec.onnx',"")

    tm = cv.TickMeter()

    frameWidth = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    detector.setInputSize([frameWidth, frameHeight])

    dem = 0
    while True:
        hasFrame, frame = cap.read()
        if not hasFrame:
            print('No frames grabbed!')
            break

        # Inference
        tm.start()
        faces = detector.detect(frame) # faces is a tuple
        tm.stop()
        
        if faces[1] is not None:
            face_align = recognizer.alignCrop(frame, faces[1][0])
            face_feature = recognizer.feature(face_align)
            test_predict = svc.predict(face_feature)
            result = mydict[test_predict[0]]
            cv.putText(frame,result,(1,50),cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Draw results on the input image
        visualize(frame, faces, tm.getFPS())

        # Visualize results
        FRAME_WINDOW.image(frame, channels='BGR')
    cv.destroyAllWindows()
