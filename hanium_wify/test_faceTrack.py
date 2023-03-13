import cv2

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

faceCascade = cv2.CascadeClassifier("files/haarcascade_frontalface_default.xml")


if not cam.isOpened():
    print("cam open fail")
    exit()

while cv2.waitKey(25) < 0:
    ret, frame = cam.read()
    if not ret:
        print("cam read fail")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray, scaleFactor=1.1,
        minNeighbors=5, minSize=(30,30),
        )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        print("x = ", x, ",  y = ", y)

    cv2.imshow("Face Sensing Test", frame)

cam.release()
cv2.destroyAllWindows()
