#!/usr/bin/python
# -*- coding: utf-8 -*-

from sensor_interface import SensorInterface

from sensor_data_generator import generate_blood_pressure_data

class Blood_Pressure_Sensor(SensorInterface):

    def __init__(self):
        self.sensorInfo = "Blood Pressure Sensor"
        self.data = None

    def getBioInfo(self):
        print("[Blood Pressure Sensor] Returning sensor information...")
        return self.data

    def extractBioInfo(self):
        print("[Blood Pressure Sensor] Extracting blood pressure data...")
        self.data = generate_blood_pressure_data(samples=1000)
