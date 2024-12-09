#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

class Sensor_Info_Preprocessor:
    def __init__(self):
        pass

    def getFormattedBioData(self, data_type, data):
        """
        데이터를 규격화하여 JSON 형식으로 변환.
        - data_type: 데이터 종류 (e.g., "temperature", "blood_pressure", "ecg")
        - data: 센서 데이터
        """
        if data_type == "temperature":
            return json.dumps({"temperature": data.tolist()})
        elif data_type == "blood_pressure":
            return json.dumps({
                "systolic": data[:, 0].tolist(),
                "diastolic": data[:, 1].tolist()
            })
        elif data_type == "ecg":
            return json.dumps({"ecg_signal": data.tolist()})
        else:
            raise ValueError("Unknown data type")






# class Sensor_Info_Preprocessor:
#     def __init__(self):
#         self.sensorInfoHistory = None
#
#     def getFormatedBioData(self, ):
#         pass
