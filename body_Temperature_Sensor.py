#!/usr/bin/python
# -*- coding: utf-8 -*-

from sensor_interface import SensorInterface

class Body_Temperature_Sensor(SensorInterface):
    def __init__(self):
        self.sensorInfo = "Body Temperature Sensor Data"

    def extractBioInfo(self):
        print("[Body_Temperature_Sensor] Extracting body temperature info")
        # 예시 데이터로 섭씨 온도를 반환
        return {"temperature": 36.6}

    def getBioInfo(self):
        print("[Body_Temperature_Sensor] Returning sensor info")
        return self.sensorInfo