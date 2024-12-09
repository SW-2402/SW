from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class SensorInterface(ABC):
    @abstractmethod
    def extractBioInfo(self):
        """
        센서로부터 원시 생체 데이터를 추출하는 메서드.
        """
        pass

    @abstractmethod
    def getBioInfo(self):
        """
        센서의 정보를 반환하는 메서드 (예: 센서 타입).
        """
        pass