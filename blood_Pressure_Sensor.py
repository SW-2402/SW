#!/usr/bin/python
# -*- coding: utf-8 -*-

from sensor_interface import SensorInterface

from sensor_data_generator import generate_blood_pressure_data

class Blood_Pressure_Sensor(SensorInterface):
    def __init__(self):
        self.sensorInfo = "Blood Pressure Sensor Data"
        self.data = generate_blood_pressure_data(samples=1000)

    def extractBioInfo(self):
        return self.data
        # print("[Blood_Pressure_Sensor] Extracting blood pressure info")
        # return {"systolic": 120, "diastolic": 80}

    def getBioInfo(self):
        print("[Blood_Pressure_Sensor] Returning sensor info")
        return self.sensorInfo
