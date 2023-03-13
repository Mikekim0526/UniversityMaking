import cv2

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
if not cam.isOpened():
    print("cam open fail")
    exit()

while True:
    ret, img01 = cam.read()
    ret, img02 = cam.read()
    ret, img03 = cam.read()
    if not ret:
        print("cam read fail")
        break

    gray_img01 = cv2.cvtColor(img01, cv2.COLOR_BGR2GRAY)
    gray_img02 = cv2.cvtColor(img02, cv2.COLOR_BGR2GRAY)
    gray_img03 = cv2.cvtColor(img03, cv2.COLOR_BGR2GRAY)

    diff_01 = cv2.absdiff(gray_img01, gray_img02)
    diff_02 = cv2.absdiff(gray_img02, gray_img03)

    ret, diff_01 = cv2.threshold(diff_01, 20, 255, cv2.THRESH_BINARY)
    ret, diff_02 = cv2.threshold(diff_02, 20, 255, cv2.THRESH_BINARY)

    diff = cv2.bitwise_and(diff_01, diff_02)
    diff_cnt = cv2.countNonZero(diff)

    cv2.imshow("motion cv", diff)

    print(diff_cnt)

    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()
