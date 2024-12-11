from firstResponder import FirstResponder
from hospitalNumber import HospitalNumber

class facade:
    def __init__(self):
        self.firstResponder = FirstResponder()
        self.hospitalNumber = HospitalNumber()
        self.emergencyCall = []

    def getAllNumber(self, ):
        self.sendAllNumber()
        return self.emergencyCall

    def sendAllNumber(self, ):
        _, firstResponderNumber = self.firstResponder.getInfo()
        hospitalNumber = self.hospitalNumber.getInfo()
        self.emergencyCall.extend(firstResponderNumber)
        self.emergencyCall.extend(hospitalNumber)
        print(self.emergencyCall)
        
if __name__ == "__main__":
    facade = facade()
    facade.sendAllNumber()
