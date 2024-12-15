#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

load_dotenv()

class Video_DB:
    def __init__(self, camera):
        self.videoList = {}
        self.storage = 20 # 20 videos
        self.remainingStorage = 10
        self.camera = camera
        self.data_path = os.getenv('DATA_PATH')

    def addVideo(self, record_num):
        if len(self.videoList) < self.storage:
            self.videoList[record_num] = (os.path.join(self.data_path, f'{record_num}.mp4'))

    def deleteVideo(self, ):
        if len(self.videoList) > self.remainingStorage:
            self.videoList.pop(0)

    def getVideo(self, index):
        try:
            video = self.videoList[index]
        except:
            self.camera.record(index)
            video = self.camera.getVideo(index)

        return video