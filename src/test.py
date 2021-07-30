from imutils.video import VideoStream
from imutils import face_utils
import imutils
import time
import cv2
import dlib

# print("Training accuracy: {}".format(
#     dlib.test_shape_predictor('/home/shammyz/repos/dlib-pupil/annotations.xml','/home/shammyz/repos/dlib-pupil/predictor.dat')))

video_stream = VideoStream(src=0).start()
time.sleep(1.0)
detector = dlib.simple_object_detector("/home/shammyz/repos/dlib-pupil/detector.svm") 
predictor = dlib.shape_predictor("/home/shammyz/repos/dlib-pupil/predictor.dat") 

while 1:
    frame = video_stream.read()
    # frame = imutils.resize(frame, width=400)
    colored = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    rects = detector(colored)

    for b in rects:
        # convert the dlib rectangle into an OpenCV bounding box and
        # draw a bounding box surrounding the face
        (x, y, w, h) = (b.left(), b.top(), b.right(), b.bottom())
        cv2.rectangle(frame, (x, y), (w, h), (0, 255, 0), 2)
        # use our custom dlib shape predictor to predict the location
        # of our landmark coordinates, then convert the prediction to
        # an easily parsable NumPy array
        shape = predictor(colored, b)
        
        shape = face_utils.shape_to_np(shape)

        # loop over the (x, y)-coordinates from our dlib shape
        # predictor model draw them on the image
        # for center in shape.parts():
        for (sX, sY) in shape:
            cv2.circle(frame, (sX, sY), 1, (0, 0, 255), -1)
            # cv2.circle(frame, (center.x, center.y), 1, (0, 0, 255), -1)
   
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
video_stream.stop()
