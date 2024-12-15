from twilio.rest import Client
from facade import facade
import os
from dotenv import load_dotenv

class Twilio:
    def __init__(self):
        load_dotenv()
        self.ACCOUNT_SID = os.getenv("ACCOUNT_SID")
        self.AUTH_TOKEN = os.getenv("AUTH_TOKEN")
        self.TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
        self.VERIFIED_NUMBER = os.getenv("VERIFIED_NUMBER")
        self.facade = facade()
        
        self.client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN)
    def sendMessage(self, ):
        allNumber = self.__getNumber()
        try:
            emergency_contacts = allNumber[:-5] if len(allNumber) > 5 else []
            hospital_contacts = allNumber[-5:] 

            body_message = "응급 상황입니다.\n"
            if emergency_contacts:
                body_message += f"비상 연락망: {', '.join(emergency_contacts)}\n"
            if hospital_contacts:
                body_message += f"병원 연락처: {', '.join(hospital_contacts)}"

            message_data = self.client.messages.create(
                from_=self.TWILIO_NUMBER,
                body=body_message,
                to=self.VERIFIED_NUMBER
            )
            print(f"Message sent successfully! SID: {message_data.sid}")
            return message_data.sid
        except Exception as e:
            print(f"Failed to send message: {e}")
            raise

    def __getNumber(self, ):
        return self.facade.getAllNumber()

