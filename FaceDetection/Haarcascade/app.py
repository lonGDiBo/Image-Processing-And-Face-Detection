import cv2 as cv
import streamlit as st

def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)

    face_cascade_name = './FaceDetection/Haarcascade/haarcascade_frontalface_alt.xml'
    eyes_cascade_name = './FaceDetection/Haarcascade/haarcascade_eye_tree_eyeglasses.xml'

    face_cascade = cv.CascadeClassifier()
    eyes_cascade = cv.CascadeClassifier()

    face_cascade.load(cv.samples.findFile(face_cascade_name))
    eyes_cascade.load(cv.samples.findFile(eyes_cascade_name))
                      
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)

        faceROI = frame_gray[y:y+h,x:x+w]
        #-- In each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv.circle(frame, eye_center, radius, (255, 0, 0 ), 4)

    return frame
def main_loop():
    camera_device = 0
    cap = cv.VideoCapture(camera_device)
    stframe = st.empty()
    while True:
        ret, frame = cap.read()
        if frame is None:
            st.error('No captured frame')
            break
        frame = detectAndDisplay(frame)
        stframe.image(frame, channels="BGR")