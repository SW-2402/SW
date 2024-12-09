#!/usr/bin/python
# -*- coding: utf-8 -*-

from dotenv import load_dotenv
import os
import cv2
import numpy as np

load_dotenv()

class Camera:
    def __init__(self):
        self.recordingTime = None
        self.videoList = None
        self.data_path = os.getenv('DATA_PATH')

    def record(self, ):
        # Open the default camera
        cam = cv2.VideoCapture(0)

        # Get the default frame width and height 640x480
        frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(os.path.join(self.data_path, 'output.mp4'), fourcc, 30.0, (frame_width, frame_height))

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

    def getVideo(self, ):
        cap = cv2.VideoCapture(os.path.join(self.data_path, 'output.mp4'))

        image_list = []
        while(cap.isOpened()):
            ret, frame = cap.read()
            if frame is not None:
                # frame is ndarray 640x480x3
                image_list.append(frame)
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()
        
        return image_list