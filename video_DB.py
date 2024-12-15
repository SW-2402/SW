#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

load_dotenv()

class Video_DB:
    def __init__(self, __camera):
        self.__videoList = {}
        self.__storage = 20 # 20 videos
        self.__remaining__Storage = 10
        self.__camera = __camera
        self.__data_path = os.getenv('DATA_PATH')

    def addVideo(self, record_num):
        if len(self.__videoList) < self.__storage:
            self.__videoList[record_num] = (os.path.join(self.__data_path, f'{record_num}.mp4'))

    def deleteVideo(self, ):
        if len(self.__videoList) > self.__remaining__Storage:
            self.__videoList.pop(0)

    def getVideo(self, index):
        try:
            video = self.__videoList[index]
        except:
            self.__camera.record(index)
            video = self.__camera.getVideo(index)

        return video