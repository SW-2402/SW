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

# TensorFlow 로그 레벨 설정
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.get_logger().setLevel('ERROR')

# Keras 경고 숨기기
warnings.filterwarnings("ignore", category=UserWarning, module="keras")


def main():
    print("[Main] Starting the biometric data processing...")

    # 센서 초기화
    sensors = {
        "temperature": Wearable_Device_Sensor(Body_Temperature_Sensor()),
        "blood_pressure": Wearable_Device_Sensor(Blood_Pressure_Sensor()),
        "ecg": Wearable_Device_Sensor(ESG_Sensor())
    }

    model = Model()
    for sensor_type, sensor in sensors.items():
        print(f"\n[Main] Requesting prediction for {sensor_type} sensor...")
        raw_data = sensor.extractBioInfo()
        result = model.predict(raw_data, sensor_type)
        print(f"[Main] Prediction for {sensor_type} sensor: {result}")
    print("[Main] Biometric data processing completed.")



    # # 데이터 전처리 및 결과 처리
    # preprocessor = Sensor_Info_Preprocessor()
    # for sensor_type, sensor in sensors.items():
    #     print(f"\n[Main] Requesting data processing for {sensor_type} sensor...")
    #     result = preprocessor.process_sensor_data(sensor, sensor_type)
    #     print(f"[Main] Result for {sensor_type} sensor: {result}")
    #print("[Main] Biometric data processing completed.")


# def main1():
#     # Sensor instances
#     sensors = {
#         "temperature": Wearable_Device_Sensor(Body_Temperature_Sensor()),
#         "blood_pressure": Wearable_Device_Sensor(Blood_Pressure_Sensor()),
#         "ecg": Wearable_Device_Sensor(ESG_Sensor())
#     }
#
#     # Preprocessor and Model
#     preprocessor = Sensor_Info_Preprocessor()
#     model = Model()
#
#     # Process data from each sensor
#     for sensor_type, sensor_instance in sensors.items():
#         print(f"\n[Main] Processing data from {sensor_type} sensor...")
#
#         # Step 1: Extract raw data from sensor
#         raw_data = sensor_instance.extractBioInfo()
#         if raw_data is None or not isinstance(raw_data, (list, np.ndarray)) or len(raw_data) == 0:
#             print(f"[Error] No valid data extracted from {sensor_type} sensor.")
#             continue
#
#         # Step 2: Get sensor info
#         sensor_info = sensor_instance.getBioInfo()
#         if not sensor_info:
#             print(f"[Error] No sensor info available for {sensor_type} sensor.")
#             continue
#
#         # Step 3: Format data using preprocessor
#         formatted_data = preprocessor.getFormattedBioData(raw_data, sensor_info)
#
#         # Step 4: Send data to the model
#         print("[Main] Sending formatted data to model...")
#         prediction = model.predict(formatted_data)
#
#         # Step 5: Print prediction result
#         print(f"[Main] Prediction for {sensor_type}: {prediction}")


if __name__ == "__main__":
    main()
