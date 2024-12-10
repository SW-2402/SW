import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import json


def build_model():
    """
    간단한 LSTM 모델 생성.
    """
    model = Sequential()
    model.add(LSTM(50, return_sequences=False, input_shape=(100, 1)))  # 입력 차원: 100 타임스텝, 1 특성
    model.add(Dense(1, activation="sigmoid"))  # 이진 분류
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    print("[Model] LSTM model initialized.")
    return model


class Model:
    def __init__(self):
        self.modelName = "LSTM Model"
        self.lstm_model = build_model()

    def predict(self, formatted_data):
        """
        JSON 데이터를 처리하여 LSTM 모델로 예측 수행
        """
        print("[Model] Predicting using LSTM model...")
        data_dict = json.loads(formatted_data)
        data = np.array(data_dict["data"])  # JSON에서 데이터 추출

        # 데이터 크기 맞추기 (100 타임스텝, 1 특성)
        data = data[:100].reshape(1, 100, 1)

        # 모델 예측
        prediction = self.lstm_model.predict(data)
        print("[Model] Prediction result:", prediction)

        # 결과 해석 (0.5 기준으로 정상/위험 판단)
        if prediction[0][0] > 0.5:
            print("[Model] Status: 위험")
            return "위험"
        else:
            print("[Model] Status: 정상")
            return "정상"


# #!/usr/bin/python
# # -*- coding: utf-8 -*-
#
# import numpy as np
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import LSTM, Dense
#
# import json
#
# def build_model():
#     """
#     간단한 LSTM 모델 생성.
#     """
#     model = Sequential()
#     model.add(LSTM(50, return_sequences=False, input_shape=(100, 3)))  # 특성 수를 3으로 변경
#     model.add(Dense(1, activation="sigmoid"))  # 이진 분류
#     model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
#     print("[Model] LSTM model initialized.")
#     return model
#
#
# class Model:
#     def __init__(self):
#         self.modelName = "LSTM Model"
#         self.lstm_model = build_model()
#
#     def predict(self, formatted_data):
#         """
#         JSON 데이터를 처리하여 LSTM 모델로 예측 수행
#         """
#         print("[Model] Predicting using LSTM model...")
#
#         # JSON 데이터를 디코딩
#         data_dict = json.loads(formatted_data)
#
#         # 각 데이터 유형에서 데이터를 추출하고, NumPy 배열로 변환
#         temperature_data = np.array(data_dict["temperature"])
#         blood_pressure_data = np.array(data_dict["blood_pressure"])
#         ecg_data = np.array(data_dict["ecg"])
#
#         # 데이터를 합쳐서 모델 입력 형식으로 정리 (100개의 타임스텝, 3개의 특성)
#         combined_data = np.stack([temperature_data, blood_pressure_data, ecg_data], axis=1)
#         combined_data = combined_data[:100].reshape(1, 100, 3)  # 입력 크기 조정
#
#         # 모델 예측
#         prediction = self.lstm_model.predict(combined_data)
#         print("[Model] Prediction result:", prediction)
#
#         # 결과 해석 (임계값을 기준으로 판단)
#         threshold = 0.5  # sigmoid 결과 기준
#         if prediction[0][0] > threshold:
#             print("[Model] Status: 위험")
#             return "위험"
#         else:
#             print("[Model] Status: 정상")
#             return "정상"
#
#
# # 사용 예시
# if __name__ == "__main__":
#     # 가상의 입력 데이터 (JSON 형식)
#     input_data = {
#         "temperature": [36.5] * 100,  # 체온 데이터 (100개)
#         "blood_pressure": [120] * 100,  # 혈압 데이터 (수축기 평균값, 100개)
#         "ecg": [0.8] * 100  # 심전도 데이터 (100개)
#     }
#
#     # JSON 문자열로 변환
#     formatted_data = json.dumps(input_data)
#
#     # 모델 인스턴스 생성 및 예측 수행
#     model = Model()
#     result = model.predict(formatted_data)
#     print("[Result] Final Status:", result)
