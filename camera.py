#!/usr/bin/python
# -*- coding: utf-8 -*-

from dotenv import load_dotenv
import os
import cv2
import numpy as np
from video_DB import Video_DB

load_dotenv()

class Camera:
    def __init__(self, ):
        self.recordingTime = None
        self.data_path = os.getenv('DATA_PATH')


    def record(self, record_num):
        # Open the default camera
        cam = cv2.VideoCapture(0)

        # Get the default frame width and height 640x480
        frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        out = cv2.VideoWriter(os.path.join(self.data_path, f'{record_num}.mp4'), fourcc, 30.0, (frame_width, frame_height))

        while True:
            ret, frame = cam.read()

            # Write the frame to the output file
            out.write(frame)

            # Display the captured frame
            cv2.imshow('Camera', frame)

            # Press 'q' to exit the loop
            if cv2.waitKey(1) == ord('q'):
                break

        # Release the capture and writer objects
        cam.release()
        out.release()
        cv2.destroyAllWindows()


    def getVideo(self, record_num):
        cap = cv2.VideoCapture(os.path.join(self.data_path, f'{record_num}.mp4'))

        while(cap.isOpened()):
            ret, frame = cap.read()
            try:
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            except:
                break

        cap.release()
        cv2.destroyAllWindows()
        
        return record_num