import dlib
import cv2

detector = dlib.simple_object_detector('/home/shammyz/repos/dlib-pupil/detector.svm')
image = cv2.imread('/home/shammyz/Downloads/eye.jpg')
boxes = detector(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

# loop over the bounding boxes and draw them
for b in boxes:
    (x, y, w, h) = (b.left(), b.top(), b.right(), b.bottom())
    cv2.rectangle(image, (x, y), (w, h), (0, 255, 0), 2)
    
    # show the image
    cv2.imshow("Image", image)
    cv2.waitKey(0)
