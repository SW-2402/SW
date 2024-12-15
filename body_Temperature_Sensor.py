
from sensor_interface import SensorInterface
from sensor_data_generator import generate_temperature_data

class Body_Temperature_Sensor(SensorInterface):


    def __init__(self):
        self.sensorInfo = "Body Temperature Sensor"
        self.data = None

    def getBioInfo(self):
        print("[Body Temperature Sensor] Returning sensor information...")
        return self.data

    def extractBioInfo(self):
        print("[Blood Pressure Sensor] Extracting blood pressure data...")
        self.data = generate_temperature_data(samples=1000)

    # def __init__(self):
    #     self.sensorInfo = "Body Temperature Sensor"
    #     self.data = generate_temperature_data(samples=1000)
    #
    # def extractBioInfo(self):
    #     """체온 데이터 반환"""
    #     print("[Body Temperature Sensor] Extracting temperature data...")
    #     return self.data
    #
    # def getBioInfo(self):
    #     print("[Body Temperature Sensor] Returning sensor information...")
    #     return self.sensorInfo