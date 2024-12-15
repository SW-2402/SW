#!/usr/bin/python
# -*- coding: utf-8 -*-

from model import Model
from dotenv import load_dotenv
from video_Preprocessor import Video_Preprocessor

load_dotenv()

class DL_Model(Model):
    def __init__(self, video_processor):
        self.__model = None
        self.__modelName = 'DL_Model'
        self.__video_processor = video_processor
        self.observer_list = []
        self.__isEmergency = False

    def predict(self, record_num):
        model_input = self.__video_processor.getSkeleton(record_num)

        skeleton_count = 0
        for frame in model_input:
            for skeleton in frame:
                if skeleton:
                    skeleton_count += 1
        
        if skeleton_count > len(model_input) * 25 * 0.5:
            self.__isEmergency = True

        print('-'*20)
        print('DL_Model predict')
        print('-'*20)

        if self.__isEmergency:
            self.notifyState()
        else:
            print('-'*20)
            print('No emergency detected')
            print('-'*20)
