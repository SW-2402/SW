from hospitalAPI import HospitalAPI
from gPSInfo import GPSInfo

class HospitalNumber:
    def __init__(self):
        self.phoneNumber = None
        self.hospitalAPI = HospitalAPI()
        self.GPS = GPSInfo()
        
        
    def __sendNumber(self, ):
        longitude, latitude = self.GPS.getInfo()
        _, self.phoneNumber = self.hospitalAPI.getInfo(longitude,latitude)
        pass

    def getInfo(self, ):
        self.__sendNumber()
        return self.phoneNumber
    
