from abc import ABC, abstractmethod

class SensorInterface(ABC):
    @abstractmethod
    def extractBioInfo(self):
        pass

    @abstractmethod
    def getBioInfo(self):
        pass
