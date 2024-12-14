import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import json

from sensor_Info_Preprocessor import Sensor_Info_Preprocessor


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
        self.preprocessor = Sensor_Info_Preprocessor()
        self.lstm_model = build_model()

    def predict(self, raw_data, sensor_type):
        """
        주어진 raw_data를 preprocessor를 통해 전처리하고, 모델 예측을 실행합니다.
        """
        print(f"[Model] Preparing data for prediction (Sensor: {sensor_type})...")
        # 데이터 전처리
        formatted_data = self.preprocessor.getFormattedBioData(raw_data, sensor_type)
        # 모델 예측
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
            return True
            # return "위험"
        else:
            print("[Model] Status: 정상")
            return False
            # return "정상"

