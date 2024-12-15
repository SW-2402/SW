#!/usr/bin/python
# -*- coding: utf-8 -*-
from dotenv import load_dotenv
import os
import cv2
from pathlib import Path
import numpy as np
import pandas as pd
import progressbar

load_dotenv()

class Video_Preprocessor:
    def __init__(self, camera, video_db):
        self.__skeletonResult = None
        self.__video_db = video_db
        self.__model_path = os.getenv('MODEL_PATH')

    def __convertFormat(self, df):
        # Convert the CSV file to a format that the model can use
        df = df.fillna(0)
        df = df.astype(int)
        df = df.values.tolist()
        return df


    def getSkeleton(self, record_num):
        # 각 파일 path
        data_path = os.getenv('DATA_PATH')
        protoFile = os.path.join(self.__model_path, "pose_deploy_linevec.prototxt") # pose_deploy_linevec_faster_4_stages
        weightsFile = os.path.join(self.__model_path, "pose_iter_440000.caffemodel")
        
        record_path = self.__video_db.getVideo(record_num)
        
        # 위의 path에 있는 network 불러오기
        net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

        video = cv2.VideoCapture(record_path)
        n_frames=int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        fps=int(video.get(cv2.CAP_PROP_FPS))
        ok, frame = video.read()
        (frameHeight, frameWidth) = frame.shape[:2]
        h=640
        w=480
        inHeight=368
        inWidth=368
        freq = 15

        n_frames //= freq

        out_path = os.path.join(data_path, f'{record_num}_out.mp4')
        # Define the output
        output = cv2.VideoWriter(out_path, 0, fps, (w, h))

        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        writer = None
        (f_h, f_w) = (h, w)
        zeros = None

        data = []
        previous_x, previous_y = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        # There are 15 points in the skeleton
        pairs = [[0,1], # head
                [1,2],[1,5], # sholders
                [2,3],[3,4],[5,6],[6,7], # arms
                [1,14],[14,11],[14,8], # hips
                [8,9],[9,10],[11,12],[12,13]] # legs

        # probability threshold for prediction of the coordinates
        thresh = 0.1 
        circle_color, line_color = (0,255,255), (0,255,0)
        # Set up the progressbar
        widgets = ["--[INFO]-- Analyzing Video: ", progressbar.Percentage(), " ",
                progressbar.Bar(), " ", progressbar.ETA()]
        pbar = progressbar.ProgressBar(maxval = n_frames+1,
                                    widgets=widgets).start()
        p = 0

        frame_count = 0
        # Start the iteration
        while True:
            ok, frame = video.read()
            if ok != True:
                break
            if frame_count % 15 != 0:
                frame_count += 1
                continue
            
            frame = cv2.resize(frame, (w, h), cv2.INTER_AREA)    
            frame_copy = np.copy(frame)
            
            # Input the frame into the model
            inpBlob = cv2.dnn.blobFromImage(frame_copy, 1.0 / 255, (inWidth, inHeight), (0, 0, 0), swapRB=False, crop=False)
            net.setInput(inpBlob)
            output = net.forward()
            H = output.shape[2]
            W = output.shape[3]
            
            points = []
            x_data, y_data = [], []
            
            # Iterate through the returned output and store the data
            for i in range(15):
                probMap = output[0, i, :, :]
                minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
                x = (w * point[0]) / W
                y = (h * point[1]) / H
                
                if prob > thresh:
                    points.append((int(x), int(y)))
                    x_data.append(x)
                    y_data.append(y)
                else :
                    points.append((0, 0))
                    x_data.append(previous_x[i])
                    y_data.append(previous_y[i])
            
            for i in range(len(points)):
                cv2.circle(frame_copy, (points[i][0], points[i][1]), 2, circle_color, -1)
            for pair in pairs:
                partA = pair[0]
                partB = pair[1]
                if points[partA] == (0, 0) or points[partB] == (0, 0):
                    continue
                cv2.line(frame_copy, points[partA], points[partB], line_color, 1, lineType=cv2.LINE_AA)
            
            if writer is None:
                writer = cv2.VideoWriter(out_path, fourcc, fps,
                                        (f_w, f_h), True)
                zeros = np.zeros((f_h, f_w), dtype="uint8")
            writer.write(cv2.resize(frame_copy,(f_w, f_h)))
            
            cv2.imshow('frame' ,frame_copy)
            
            data.append(x_data + y_data)
            previous_x, previous_y = x_data, y_data
            
            p += 1
            pbar.update(p)

            frame_count += 1
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

        csv_path = os.path.join(data_path, f'{record_num}.csv')
        # Save the output data from the video in CSV format
        df = pd.DataFrame(data)
        df.to_csv(csv_path, index = False)
        print('save complete')

        pbar.finish()
        video.release()
        cv2.destroyAllWindows()

        self.__skeletonResult = self.__convertFormat(df)

        return self.__skeletonResult