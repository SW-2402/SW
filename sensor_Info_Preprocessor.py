import json

from sensor_interface import SensorInterface
from wearable_Device_Sensor import Wearable_Device_Sensor


class Sensor_Info_Preprocessor:
    def __init__(self):
        # self.supported_sensors = ["temperature", "blood_pressure", "ecg"]
        self.sensor_info_history = []
        self.supported_sensors = {
            "Body Temperature Sensor": "temperature",
            "Blood Pressure Sensor": "blood_pressure",
            "ECG Sensor": "ecg"
        }

    def extractAndStoreData(self, sensor: SensorInterface):
        """
        센서의 데이터를 추출(extractBioInfo)한 후 내부적으로 저장합니다.
        """
        wearable_sensor = Wearable_Device_Sensor(sensor)
        wearable_sensor.extractBioInfo()  # 데이터 추출
        print(f"[Preprocessor] Data extracted for {sensor.sensorInfo}.")

    def getFormattedBioData(self, sensor: SensorInterface):
        """
        센서 데이터를 JSON 형식으로 변환하여 반환합니다.
        """
        sensor_info = sensor.getBioInfo()  # 추출된 데이터 가져오기
        sensor_type = sensor.sensorInfo

        if sensor_type not in self.supported_sensors:
            raise ValueError(f"Unsupported sensor type: {sensor_type}")

        # JSON 포맷팅
        formatted_data = {
            "sensor_type": sensor_type,
            "data_type": self.supported_sensors[sensor_type],
            "data": sensor_info.tolist() if hasattr(sensor_info, "tolist") else sensor_info
        }

        # 히스토리에 추가
        self.sensor_info_history.append(formatted_data)
        print(f"[Preprocessor] Data successfully formatted for {sensor_type}.")
        return json.dumps(formatted_data)
