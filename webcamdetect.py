# face detection through webcam finished
import face_recognition
import numpy as np
import cv2
import numpy

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]
    
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # loop through each face within the picture 
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        cv2.rectangle(frame, (left,top), (right, bottom), (0, 0, 255), 2)

    cv2.imshow('Video', frame)

    #press q to quit program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destoryAllWindows()

