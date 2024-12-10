#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

import json

class Model:
    def __init__(self):
        self.modelName = "LSTM Model"
        self.observer = None
        self.lstm_model = self.build_model()
        self.thresholds = {
            "temperature": {"min": 35.0, "max": 38.0},  # 체온 기준
            "blood_pressure": {"systolic": {"min": 90, "max": 140},
                               "diastolic": {"min": 60, "max": 90}},  # 혈압 기준
            "ecg": {"min": 0.4, "max": 1.2}  # ECG 신호 기준
        }

    def build_model(self):
        """
        간단한 LSTM 모델 생성.
        """
        model = Sequential()
        model.add(LSTM(50, activation='relu', input_shape=(100, 1)))  # 입력 형태에 맞게 조정
        model.add(Dense(1))
        model.compile(optimizer='adam', loss='mse')
        print("[Model] LSTM model initialized.")
        return model

    def normalize_data(data):
        """
        데이터 정규화 (0~1 사이 값으로 변환)
        """
        return (data - data.min()) / (data.max() - data.min())

    def predict(self, formatted_data):
        """
        JSON 데이터를 처리하여 LSTM 모델에 입력 및 예측 수행.
        """
        print("[Model] Predicting using LSTM model.")
        # JSON 데이터를 디코딩
        data_dict = json.loads(formatted_data)

        # 데이터를 NumPy 배열로 변환
        if "temperature" in data_dict:
            data = np.array(data_dict["temperature"]).reshape(-1, 1)
        elif "systolic" in data_dict and "diastolic" in data_dict:
            # 혈압 데이터를 처리
            data = np.stack(
                (np.array(data_dict["systolic"]), np.array(data_dict["diastolic"])), axis=-1
            )
        elif "ecg_signal" in data_dict:
            data = np.array(data_dict["ecg_signal"]).reshape(-1, 1)
        else:
            raise ValueError("Unknown data format for prediction.")

        # LSTM 입력 데이터로 변환 (예: 타임스텝 맞추기)
        data = data[:100].reshape(1, 100, 1)  # 예제 기준으로 100개의 타임스텝

        # 모델 예측
        prediction = self.lstm_model.predict(data)
        print("[Model] Prediction result:", prediction)
        return prediction

    def notifyState(self, data_type, prediction):
        """
        데이터 종류에 따라 임계값 기반 위험 상태 알림.
        """
        if data_type == "temperature":
            if prediction < self.thresholds["temperature"]["min"] or prediction > self.thresholds["temperature"]["max"]:
                return "위험 상태 (체온 비정상)"
            return "정상 상태 (체온)"

        elif data_type == "blood_pressure":
            systolic, diastolic = prediction
            if (systolic < self.thresholds["blood_pressure"]["systolic"]["min"] or
                    systolic > self.thresholds["blood_pressure"]["systolic"]["max"] or
                    diastolic < self.thresholds["blood_pressure"]["diastolic"]["min"] or
                    diastolic > self.thresholds["blood_pressure"]["diastolic"]["max"]):
                return "위험 상태 (혈압 비정상)"
            return "정상 상태 (혈압)"

        elif data_type == "ecg":
            if prediction < self.thresholds["ecg"]["min"] or prediction > self.thresholds["ecg"]["max"]:
                return "위험 상태 (ECG 비정상)"
            return "정상 상태 (ECG)"

        return "알 수 없는 데이터 유형"

    def min(self):
        pass


