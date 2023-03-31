#!/usr/bin/env python3
import cv2
import numpy as np
import sys

def read_frame(frame):
    cv2.imshow('Frame', frame)
    print(frame.shape)

def show_mp4(file):
    cap = cv2.VideoCapture(file)
    if(cap.isOpened() == False):
        print("file error")

    while(cap.isOpened()):
        ret, frame = cap.read()

        if ret == True:
            read_frame(frame)
            
            if cv2.waitKey(5) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # Model Architecture
    # --------------------
    # INPUT
    # Get input from video
    file = 'video.hevc'

    show_mp4(file)

    # Previous Frame (3, 128, 256)
    # Current Frame (3, 128, 256)
    
    # Concat BOTH images --> (6, 128, 256)

    # APPLY EFFICIENTNET-B2

