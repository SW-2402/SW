
from sensor_interface import SensorInterface

from sensor_data_generator import generate_temperature_data

class Body_Temperature_Sensor(SensorInterface):
    def __init__(self):
        self.sensorInfo = "Body Temperature Sensor"
        self.data = generate_temperature_data(samples=1000)

    def extractBioInfo(self):
        """체온 데이터 반환"""
        print("[Body Temperature Sensor] Data extracted.")
        return self.data

    def getBioInfo(self):
        return self.sensorInfo