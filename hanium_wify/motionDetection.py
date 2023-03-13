import cv2
import numpy as np

frameWidth, frameHeight = 640, 480
fps = 20

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, frameWidth)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, frameHeight)

if not cam.isOpened():
    print("cam open fail")
    exit()

def detectMove(name, image):
    userMovement = False
    maxMove = 0
    maxMoveX, maxMoveY = 0, 0
    cell = 80;
    
    for i in range (0, frameWidth-20, 20):
        for j in range (0, frameHeight-20, 20):
            tempMove = cv2.countNonZero(image[j:j+cell, i:i+cell])
            if maxMove < tempMove :
                maxMoveX, maxMoveY = i, j
                maxMove = tempMove
    
    if maxMove > 500:
        userMovement = True
        cv2.rectangle(image,
                      (maxMoveX, maxMoveY),
                      (maxMoveX+cell, maxMoveY+cell),
                      255, 3)
    else :
        userMovement = False
    
    cv2.imshow("movement of "+name, image)
    return userMovement

deleteBG = cv2.createBackgroundSubtractorMOG2(500,16,False)
morphSE = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))

while cam.isOpened():
    delay = int(1000/fps)
    ret, frame = cam.read()
    
    if not ret:
        break
    
    frame_noBG = deleteBG.apply(frame)
    frame_denoised = cv2.erode(frame_noBG, morphSE)
    print("userMovement=", detectMove("denoised video", frame_denoised))
    
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
