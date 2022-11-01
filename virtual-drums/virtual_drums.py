import numpy as np
import time
import cv2
from pygame import mixer

def play_beat(detected,sound):
	
	play = (detected) > hat_thickness[0]*hat_thickness[1]*0.8

	if play and sound==1:
		drum_snare.play()
		
	elif play and sound==2:
		drum_hat.play()
		time.sleep(0.001)

def detect_in_region(frame,sound):
	
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	mask = cv2.inRange(hsv, greenLower, greenUpper)
	
	detected = np.sum(mask)
	
	play_beat(detected,sound)

	return mask
verbose = False

mixer.init()
drum_hat = mixer.Sound('./sounds/high_hat_1.ogg')
drum_snare = mixer.Sound('./sounds/snare_1.wav')

greenLower = (25,52,72)
greenUpper = (102,255,255)

camera = cv2.VideoCapture(0)
ret,frame = camera.read()
H,W = frame.shape[:2]

kernel = np.ones((7,7),np.uint8)

hat = cv2.resize(cv2.imread('./images/high_hat.png'),(200,100),interpolation=cv2.INTER_CUBIC)
snare = cv2.resize(cv2.imread('./images/snare_drum.png'),(200,100),interpolation=cv2.INTER_CUBIC)


hat_center = [np.shape(frame)[1]*2//8,np.shape(frame)[0]*6//8]
snare_center = [np.shape(frame)[1]*6//8,np.shape(frame)[0]*6//8]

hat_thickness = [200,100]
hat_top = [hat_center[0]-hat_thickness[0]//2,hat_center[1]-hat_thickness[1]//2]
hat_btm = [hat_center[0]+hat_thickness[0]//2,hat_center[1]+hat_thickness[1]//2]

snare_thickness = [200,100]
snare_top = [snare_center[0]-snare_thickness[0]//2,snare_center[1]-snare_thickness[1]//2]
snare_btm = [snare_center[0]+snare_thickness[0]//2,snare_center[1]+snare_thickness[1]//2]

time.sleep(1)

while True:
	
	ret, frame = camera.read()
	frame = cv2.flip(frame,1)

	if not(ret):
	    break
    
	snare_region = np.copy(frame[snare_top[1]:snare_btm[1],snare_top[0]:snare_btm[0]])
	mask = detect_in_region(snare_region,1)

	hat_region = np.copy(frame[hat_top[1]:hat_btm[1],hat_top[0]:hat_btm[0]])
	mask = detect_in_region(hat_region,2)

	cv2.putText(frame,'Virtual Drums',(10,30),2,1,(20,20,20),2)
    
	if verbose:
		frame[snare_top[1]:snare_btm[1],snare_top[0]:snare_btm[0]] = cv2.bitwise_and(frame[snare_top[1]:snare_btm[1],snare_top[0]:snare_btm[0]],frame[snare_top[1]:snare_btm[1],snare_top[0]:snare_btm[0]], mask=mask[snare_top[1]:snare_btm[1],snare_top[0]:snare_btm[0]])
		frame[hat_top[1]:hat_btm[1],hat_top[0]:hat_btm[0]] = cv2.bitwise_and(frame[hat_top[1]:hat_btm[1],hat_top[0]:hat_btm[0]],frame[hat_top[1]:hat_btm[1],hat_top[0]:hat_btm[0]],mask=mask[hat_top[1]:hat_btm[1],hat_top[0]:hat_btm[0]])
    
	else:
		frame[snare_top[1]:snare_btm[1],snare_top[0]:snare_btm[0]] = cv2.addWeighted(snare, 1, frame[snare_top[1]:snare_btm[1],snare_top[0]:snare_btm[0]], 1, 0)
		frame[hat_top[1]:hat_btm[1],hat_top[0]:hat_btm[0]] = cv2.addWeighted(hat, 1, frame[hat_top[1]:hat_btm[1],hat_top[0]:hat_btm[0]], 1, 0)
    
    
	cv2.imshow('Output',frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break

camera.release()
cv2.destroyAllWindows()
