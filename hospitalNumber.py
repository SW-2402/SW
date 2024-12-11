from hospitalAPI import HospitalAPI
class HospitalNumber:
    def __init__(self):
        self.phoneNumber = None
        self.hospitalAPI = HospitalAPI()
    def sendNumber(self, ):
        _, self.phoneNumber = self.hospitalAPI.getInfo('127.085156592737','37.5606691709596')
        pass

    def getInfo(self, ):
        self.sendNumber()
        return self.phoneNumber
    
