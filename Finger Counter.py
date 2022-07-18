import cv2
from cvzone.HandTrackingModule import HandDetector

video = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
fingers = 0

while True:
    grapped , img = video.read()
    img = cv2.flip(img,1)
    hand = detector.findHands(img , draw = False)
    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            if fingerup == [0,0,0,0,0]:
                fingers = 0 
            if fingerup == [0,1,0,0,0]:
                fingers = 1
            if fingerup == [0,1,1,0,0]:
                fingers = 2
            if fingerup == [0,1,1,1,0]:
                fingers = 3
            if fingerup == [0,1,1,1,1]:
                fingers = 4
            if fingerup == [1,1,1,1,1]:
                fingers = 5
    print (fingers)

    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF == ord ("q"):
        break

video.release()
cv2.destroyAllWindows()