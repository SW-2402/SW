#!/usr/bin/python
# -*- coding: utf-8 -*-

from sensor_interface import SensorInterface

from sensor_data_generator import generate_ecg_data

class ESG_Sensor(SensorInterface):
    def __init__(self):
        self.sensorInfo = "ESG Sensor Data"
        self.data = generate_ecg_data(samples=1000)

    def extractBioInfo(self):
        print("[ESG_Sensor] Extracting electrocardiogram data")
        return self.data
        # 예시 데이터로 ESG 데이터를 반환
        # return {"ecg_waveform": [0.1, 0.3, 0.5, 0.2, 0.0]}

    def getBioInfo(self):
        print("[ESG_Sensor] Returning sensor info")
        return self.sensorInfo
