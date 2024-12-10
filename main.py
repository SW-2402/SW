# main.py

from wearable_Device_Sensor import Wearable_Device_Sensor
from body_Temperature_Sensor import Body_Temperature_Sensor
from blood_Pressure_Sensor import Blood_Pressure_Sensor
from eSG_Sensor import ESG_Sensor
from sensor_Info_Preprocessor import Sensor_Info_Preprocessor
from model import Model
import json
import numpy as np

import matplotlib.pyplot as plt

def plot_sensor_data(sensor_data):
    """
    센서 데이터를 시각화하는 함수.
    :param sensor_data: 각 센서 데이터를 포함한 딕셔너리 (temperature, blood_pressure, ecg)
    """
    time_steps = range(len(next(iter(sensor_data.values()))))  # 데이터 길이에 따른 x축 설정

    plt.figure(figsize=(15, 5))

    # 체온 데이터
    plt.subplot(1, 3, 1)
    plt.plot(time_steps, sensor_data["temperature"], label="Temperature (°C)", color="orange")
    plt.xlabel("Time Step")
    plt.ylabel("Temperature (°C)")
    plt.title("Body Temperature")
    plt.grid(True)
    plt.legend()

    # 혈압 데이터
    plt.subplot(1, 3, 2)
    plt.plot(time_steps, sensor_data["blood_pressure"], label="Blood Pressure", color="blue")
    plt.xlabel("Time Step")
    plt.ylabel("Pressure (mmHg)")
    plt.title("Blood Pressure")
    plt.grid(True)
    plt.legend()

    # 심전도 데이터
    plt.subplot(1, 3, 3)
    plt.plot(time_steps, sensor_data["ecg"], label="ECG Signal", color="green")
    plt.xlabel("Time Step")
    plt.ylabel("ECG Amplitude")
    plt.title("ECG Signal")
    plt.grid(True)
    plt.legend()

    # 그래프 출력
    plt.tight_layout()
    plt.show()


# Sensor instances
sensors = {
    "temperature": Wearable_Device_Sensor(Body_Temperature_Sensor()),
    "blood_pressure": Wearable_Device_Sensor(Blood_Pressure_Sensor()),
    "ecg": Wearable_Device_Sensor(ESG_Sensor())
}

# Preprocessor and Model
preprocessor = Sensor_Info_Preprocessor()
model = Model()

# Collect and process data from all sensors
sensor_data = {}

for sensor_type, sensor_instance in sensors.items():
    print(f"\n[Main] Processing data from {sensor_type} sensor...")

    # Raw data from sensor
    raw_data = sensor_instance.extractBioInfo()
    sensor_info = sensor_instance.getBioInfo()

    # Format the data
    formatted_data = preprocessor.getFormattedBioData(raw_data, sensor_info)

    # Store formatted data for model input
    sensor_data[sensor_type] = np.array(formatted_data)

# Ensure all sensor data have the same length (e.g., 100 timesteps)
min_timesteps = min(len(data) for data in sensor_data.values())
for key in sensor_data:
    sensor_data[key] = sensor_data[key][:min_timesteps]

# Combine data into a single input for the model
combined_data = np.stack(
    [sensor_data["temperature"], sensor_data["blood_pressure"], sensor_data["ecg"]], axis=1
)
combined_data = combined_data.reshape(1, min_timesteps, 3)  # Reshape for model input

# Convert combined data to JSON format for the model
formatted_data = json.dumps({
    "temperature": sensor_data["temperature"].tolist(),
    "blood_pressure": sensor_data["blood_pressure"].tolist(),
    "ecg": sensor_data["ecg"].tolist()
})

# Send data to model and get predictions
print("[Main] Sending formatted data to model...")
result = model.predict(formatted_data)


# 센서 데이터 그래프 출력
print("[Main] Visualizing sensor data...")
# plot_sensor_data(sensor_data)


# Final status
if result == "위험":
    print("[Main] ALERT: Combined sensor data indicates a potential risk!")
else:
    print("[Main] All sensor data are within the safe range.")
