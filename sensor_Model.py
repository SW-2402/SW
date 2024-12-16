import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import json
from model import Model  # Base Model 클래스
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

class SensorModel(Model):
    def __init__(self):
        super().__init__()  # Base Model 클래스 초기화
        self._Model__modelName = "LSTM Sensor Model"  # 부모 클래스의 private 속성 접근
        self.preprocessor = Sensor_Info_Preprocessor()
        self.lstm_model = build_model()

    def predict(self, sensor):
        """
        주어진 센서를 통해 데이터를 전처리하고, 모델 예측을 실행합니다.
        """
        print(f"[SensorModel] Preparing data for prediction (Sensor: {sensor.sensorInfo})...")

        # 데이터 추출 및 전처리
        formatted_data = self.preprocessor.getFormattedBioData(sensor)
        # 모델 예측 준비
        print("[SensorModel] Predicting using LSTM model...")
        data_dict = json.loads(formatted_data)
        data = np.array(data_dict["data"])  # JSON에서 데이터 추출

        # 데이터 크기 맞추기 (100 타임스텝, 1 특성)
        if len(data) < 100:
            print("[SensorModel] Warning: Not enough data points. Padding with zeros.")
            data = np.pad(data, (0, 100 - len(data)), 'constant')
        data = data[:100].reshape(1, 100, 1)

        # 모델 예측
        prediction = self.lstm_model.predict(data)
        print("[SensorModel] Prediction result:", prediction)

        # 결과 해석 (0.5 기준으로 정상/위험 판단)
        if prediction[0][0] > 0.5:
            print("[SensorModel] Status: 위험")
            # self.notifyState()  # 상태 변경 알림
            return True
        else:
            print("[SensorModel] Status: 정상")
            return False
