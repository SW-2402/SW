from wearable_Device_Sensor import Wearable_Device_Sensor
from body_Temperature_Sensor import Body_Temperature_Sensor
from blood_Pressure_Sensor import Blood_Pressure_Sensor
from ecg_Sensor import ECG_Sensor
from sensor_Info_Preprocessor import Sensor_Info_Preprocessor
from model import Model
from sensor_Model import SensorModel
import numpy as np
import os
import tensorflow as tf
import warnings
import matplotlib.pyplot as plt
from datetime import datetime
# from dotenv import load_dotenv

# 환경 변수 로드
# load_dotenv()

# TensorFlow 로그 레벨 설정
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.get_logger().setLevel('ERROR')
api_key = os.getenv("API_KEY")

# Keras 경고 숨기기
warnings.filterwarnings("ignore", category=UserWarning, module="keras")

def main():
    is_any_risk = predict_all_sensors()
    if is_any_risk:
        print("[Main] Risk detected in at least one sensor!")
    else:
        print("[Main] All sensors indicate normal status.")

def plot_data(sensor_type, raw_data):
    """
    위험 상태의 데이터를 그래프로 시각화하는 함수.
    """
    # 현재 스크립트가 위치한 디렉토리에서 sensor_history 폴더로 경로 설정
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sensor_history')

    # 디렉토리가 없으면 생성
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 현재 시각을 파일명에 덧붙일 수 있는 형식으로 가져오기
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

    print(f"[Main] Plotting data for {sensor_type}...")
    plt.figure(figsize=(10, 6))
    plt.plot(raw_data, label=sensor_type, color="red")
    plt.title(f"{sensor_type} Data Visualization (Risk Detected)")
    plt.xlabel("Time Steps")
    plt.ylabel("Sensor Values")
    plt.legend()
    plt.grid(True)

    # 파일명에 현재 시각 추가
    file_name = f"{sensor_type}_{current_time}.png"
    # 파일 저장 (디렉토리 경로 포함)
    file_path = os.path.join(directory, file_name)
    plt.savefig(file_path)
    print(f"Graph saved to {file_path}")

    # 그래프 화면에 표시
    plt.show()

def predict_all_sensors():
    """
    센서 데이터를 처리하고 모든 센서에 대해 예측을 수행하는 함수.
    """
    print("[Main] Starting the biometric data processing...")

    # 모델 초기화
    model = SensorModel()

    # 위험 상태 플래그
    any_risk_detected = False

    sensors = [
        Wearable_Device_Sensor(Body_Temperature_Sensor()),
        Wearable_Device_Sensor(Blood_Pressure_Sensor()),
        Wearable_Device_Sensor(ECG_Sensor())
    ]

    for sensor in sensors:
        print(f"\n[Main] Processing data for {sensor.sensor.sensorInfo}...")
        sensor.extractBioInfo()  # 센서 데이터 추출
        result = model.predict(sensor.sensor)  # 원래 센서를 모델에 전달
        print(f"Prediction Result for {sensor.sensor.sensorInfo}:", "위험" if result else "정상")
        if result:
            any_risk_detected = True
            plot_data(sensor.sensor.sensorInfo, sensor.getBioInfo())  # 결과 시각화

    return any_risk_detected


if __name__ == "__main__":
    main()

