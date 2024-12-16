import csv
from firstResponderDB import FirstResponderDB
from dotenv import load_dotenv
import os

load_dotenv()

class FirstResponder:
    def __init__(self):
        self.name = {}
        self.phoneNumber = {}
        self.db = FirstResponderDB()
        self.__loadFromCSV(os.path.join(os.getenv("DATA_PATH"), os.getenv("FIRST_RESPONDER_FILE")))
        
    def __loadFromCSV(self, file_path):
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader) 

                for row in reader:
                    if len(row) >= 2:
                        name, phone_number = row[0], row[1]
                        self.db.addInfo(name, phone_number)
        except FileNotFoundError:
            print(f"Error: 파일 '{file_path}'을(를) 찾을 수 없습니다.")
        except Exception as e:
            print(f"Error: CSV 파일 읽기 중 오류 발생 - {e}")
    
    def __sendNumber(self, ):
        FirstResponderinfo = self.db.getInfo()
        self.name = list(FirstResponderinfo.keys())
        self.phoneNumber = list(FirstResponderinfo.values())
        pass

    def getInfo(self, ):
        self.__sendNumber()
        return self.name, self.phoneNumber
