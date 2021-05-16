import cv2
import time
import datetime
import streamlit as st

import streamlit.components as stc

# Stolen from https://www.youtube.com/watch?v=PLKLsPDZ1t0&t=390s

#timestr = time.strftime("%Y%m%d-%H%M%S")

#For time counting
c = 0

#For file names
q = 0


#Count time
start = time.time()

#Web App
st.title("AI Security Webcam")
st.write("Face Detection with Computer Vision")

st.write("Streamlit library does not support the option to show the live video from your webcam, but every time it detects a face it will show you its photo.")

clickhere = st.button("Start Webcam")

#st.write("Press 'q' to close the App")


if clickhere == True:

    # Get haarcascade
    faces = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

    # Start Webcam
    cap = cv2.VideoCapture(0)


    while True:

        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, 0)

        face = faces.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)

        if (len(face) > 0):

            (x, y, w, h) = face[0]

            x = int(x)
            y = int(y)

            frame = cv2.rectangle(frame, (x, y), (x + w , y + h), (255, 0, 0), 2)

            c = c + 1


        cv2.imshow("frame", frame)

        if c == 1:
            print("Humanoide Detected")

            q = q + 1

            foto = f'intruder_picture#{q}.png'

            cv2.imwrite(foto, frame)

            st.image(foto, width=100)

            st.write(datetime.datetime.now())


        if time.time() - start > 15:
            c = 0
            start = time.time()

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


    cap.release()
    cv2.destroyAllWindows

    # for filename in glob.iglob('**/*.png', recursive=True):
    #     # read the image
    #     im = Image.open(filename)
    #
    #     # show image
    #     im.show()


