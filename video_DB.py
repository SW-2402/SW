#!/usr/bin/python
# -*- coding: utf-8 -*-

class Video_DB:
    def __init__(self):
        self.videoList = []
        self.storage = 20 # 20 videos
        self.remainingStorage = 10

    def addVideo(self, image_list):
        if len(self.videoList) < self.storage:
            self.videoList.append(image_list)

    def deleteVideo(self, ):
        if len(self.videoList) > self.remainingStorage:
            self.videoList.pop(0)

    def getVideo(self, index):
        return self.videoList[index]
