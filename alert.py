from twilio_Service import Twilio

class Alert:
    def __init__(self):
        self.isEmergency = None
        self.twilio = Twilio()

    def startEmergency(self, ):
        self.twilio.sendMessage()
        pass

    def stopEmergency(self, ):
        pass

    def alertEmergency(self, ):
        pass
    
if __name__ == "__main__":
    Alert().startEmergency()
