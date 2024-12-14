from wearable_Device_Sensor import Wearable_Device_Sensor
from body_Temperature_Sensor import Body_Temperature_Sensor
from blood_Pressure_Sensor import Blood_Pressure_Sensor
from ecg_Sensor import ESG_Sensor
from sensor_Info_Preprocessor import Sensor_Info_Preprocessor
from model import Model
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

    # 센서 목록 초기화
    sensor_classes = {
        "Body Temperature Sensor": Body_Temperature_Sensor,
        "Blood Pressure Sensor": Blood_Pressure_Sensor,
        "ECG Sensor": ESG_Sensor
    }

    # 모델 초기화
    model = Model()

    # 위험 상태 플래그
    any_risk_detected = False

    # 모든 센서에 대해 예측 수행
    for sensor_type, sensor_class in sensor_classes.items():
        print(f"\n[Main] Processing {sensor_type}...")
        sensor = Wearable_Device_Sensor(sensor_class())
        raw_data = sensor.extractBioInfo()
        result = model.predict(raw_data, sensor_type)
        print(f"[Main] Prediction for {sensor_type}: {'위험' if result else '정상'}")

        # 위험일 경우 그래프 시각화
        if result:
            any_risk_detected = True
            plot_data(sensor_type, raw_data)

    print("[Main] Biometric data processing completed.")

    # 위험 상태 반환
    return any_risk_detected

if __name__ == "__main__":
    main()
