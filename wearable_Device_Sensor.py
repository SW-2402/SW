
from sensor_interface import SensorInterface


class Wearable_Device_Sensor(SensorInterface):
    def __init__(self, sensor: SensorInterface):
        self.sensor = sensor

    def extractBioInfo(self):
        print("[Decorator] Pre-processing in Wearable_Device_Sensor")
        data = self.sensor.extractBioInfo()
        print("[Decorator] Post-processing in Wearable_Device_Sensor")
        return data

    def getBioInfo(self):
        print("[Decorator] Logging bio info request")
        return self.sensor.getBioInfo()

