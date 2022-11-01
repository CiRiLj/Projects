import cv2
from cvzone.HandTrackingModule import HandDetector
from pygame import mixer
 
detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(0)
 
while True:
    _, img = video.read()
    img = cv2.flip(img, 1)
    hand = detector.findHands(img, draw=False)
    mixer.init()
    
    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            if fingerup == [0, 1, 0, 0, 0]:
                mixer.music.load('//musicfile')
                mixer.music.play()
            if fingerup == [0, 1, 1, 0, 0]:
                mixer.music.load('//musicfile')
                mixer.music.play()
            if fingerup == [0, 1, 1, 1, 0]:
                mixer.music.load('//musicfile')
                mixer.music.play()
            if fingerup == [0, 1, 1, 1, 1]:
                mixer.music.load('//musicfile')
                mixer.music.play()
            if fingerup == [1, 1, 1, 1, 1]:
                mixer.music.load('//musicfile')
                mixer.music.play()
            if fingerup == [0, 0, 0, 0, 0]:
                mixer.music.stop()

    width = img.shape[1]
    height = img.shape[0]

    img = cv2.rectangle(img,(width//2 + 35,0),(width,height//2),(0,0,255),1)
    cv2.imshow("Web-Cam", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
         
video.release()
cv2.destroyAllWindows()
