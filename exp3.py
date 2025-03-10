import cv2
import numpy as np
from tkinter import *

def adjust_image():
    cap = cv2.VideoCapture(0)
    
    def update(val=None):
        ret, frame = cap.read()
        if not ret:
            return
        
        contrast = cv2.getTrackbarPos('Contrast', 'Adjustments') / 50
        brightness = cv2.getTrackbarPos('Brightness', 'Adjustments') - 100
        sharpness = cv2.getTrackbarPos('Sharpness', 'Adjustments') / 50
        hue = cv2.getTrackbarPos('Hue', 'Adjustments') - 50
        saturation = cv2.getTrackbarPos('Saturation', 'Adjustments') / 50
        
        adjusted = cv2.convertScaleAbs(frame, alpha=contrast, beta=brightness)
        
        hsv = cv2.cvtColor(adjusted, cv2.COLOR_BGR2HSV).astype(np.float32)
        hsv[..., 0] += hue
        hsv[..., 1] *= saturation
        hsv = np.clip(hsv, 0, 255).astype(np.uint8)
        adjusted = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        
        kernel = np.array([[0, -1, 0], [-1, sharpness + 4, -1], [0, -1, 0]]) / (sharpness + 1)
        adjusted = cv2.filter2D(adjusted, -1, kernel)
        
        cv2.imshow('Webcam', adjusted)
    
    cv2.namedWindow('Adjustments')
    cv2.createTrackbar('Contrast', 'Adjustments', 50, 100, update)
    cv2.createTrackbar('Brightness', 'Adjustments', 100, 200, update)
    cv2.createTrackbar('Sharpness', 'Adjustments', 50, 100, update)
    cv2.createTrackbar('Hue', 'Adjustments', 50, 100, update)
    cv2.createTrackbar('Saturation', 'Adjustments', 50, 100, update)
    
    while True:
        update()
        if cv2.waitKey(1) & 0xFF == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()

adjust_image()
