#!/usr/bin/python
# -*- coding: utf-8 -*-

from model import Model
from dotenv import load_dotenv
from video_Preprocessor import Video_Preprocessor

load_dotenv()

class DL_Model(Model):
    def __init__(self, video_processor):
        self.model = None
        self.modelName = 'DL_Model'
        self.video_processor = video_processor
        self.observer_list = []
        self.isEmergency = False

    def predict(self, record_num):
        model_input = self.video_processor.getSkeleton(record_num)

        skeleton_count = 0
        for frame in model_input:
            for skeleton in frame:
                if skeleton:
                    skeleton_count += 1
        
        if skeleton_count > len(model_input) * 25 * 0.5:
            self.isEmergency = True

        print('DL_Model predict')

        if self.isEmergency:
            self.notifyState()
        else:
            print('No emergency detected')
