#!/usr/bin/python
# -*- coding: utf-8 -*-

from sensor_interface import SensorInterface

from sensor_data_generator import generate_blood_pressure_data

class Blood_Pressure_Sensor(SensorInterface):
    def __init__(self):
        self.sensorInfo = "Blood Pressure Sensor"
        self.data = generate_blood_pressure_data(samples=1000)

    def extractBioInfo(self):
        print("[Blood_Pressure_Sensor] Extracting blood pressure info")
        return self.data

    def getBioInfo(self):
        print("[Blood_Pressure_Sensor] Returning sensor info")
        return self.sensorInfo
