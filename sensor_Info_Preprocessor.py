#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

class Sensor_Info_Preprocessor:
    def __init__(self):
        self.sensorInfoHistory = None  # Can be used to store sensor information history
        # pass

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

    def getFormatedBioData2(self, data):
        """
        Formats the raw biometric data into a standardized format (e.g., JSON).

        Args:
            data: The raw biometric data.

        Returns:
            The formatted biometric data. (Implementation depends on the chosen format)
        """
        # Implement logic to format data based on sensor type and desired output format (e.g., JSON)
        # This example assumes conversion to JSON for simplicity
        formatted_data = {"sensor_type": self.getBioInfo(), "data": data.tolist()}  # Replace with actual formatting logic
        return formatted_data

    def sendToLSTM(self, formatted_data, model):
        print("[Preprocessor] Sending formatted data to LSTM model.")
        model.predict(formatted_data)

# class Sensor_Info_Preprocessor:
#     def __init__(self):
#         self.sensorInfoHistory = None
#
#     def getFormatedBioData(self, ):
#         pass
