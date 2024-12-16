#!/usr/bin/python
# -*- coding: utf-8 -*-

from sensor_interface import SensorInterface

from sensor_data_generator import generate_ecg_data

class ECG_Sensor(SensorInterface):

    def __init__(self):
        self.sensorInfo = "ECG Sensor"
        self.data = None

    def getBioInfo(self):
        print("[ECG Sensor] Returning sensor information...")
        return self.data

    def extractBioInfo(self):
        print("[ECG Sensor] Extracting electrocardiogram data...")
        self.data = generate_ecg_data(samples=1000)

