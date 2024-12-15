from firstResponderDB import FirstResponderDB

class FirstResponder:
    def __init__(self):
        self.name = {}
        self.phoneNumber = {}
        self.db = FirstResponderDB()
        
    def __sendNumber(self, ):
        self.db.addInfo("건구수", "010-1234-5678")
        self.db.addInfo("김건국", "010-1111-2222")
        FirstResponderinfo = self.db.getInfo()
        self.name = list(FirstResponderinfo.keys())
        self.phoneNumber = list(FirstResponderinfo.values())
        pass

    def getInfo(self, ):
        self.__sendNumber()
        return self.name, self.phoneNumber