import json

#
# #이 코드 사용되지 않고 있음
# def sendToModel(self, formatted_data, model):
#     print("[Preprocessor] Sending formatted data to model...")
#     result = model.predict(formatted_data)
#     print(f"[Preprocessor] Model prediction result: {result}")
#     return result

class Sensor_Info_Preprocessor:
    def __init__(self):
        self.supported_sensors = ["temperature", "blood_pressure", "ecg"]
        self.sensorInfoHistory = []  # Can be used to store sensor information history
        # self.model = Model()  #main 간소화1
        # pass

    def getFormattedBioData(self, bio_data, sensor_type):
        """
        생체 데이터를 JSON 형식으로 규격화.
        """
        if sensor_type == "Body Temperature Sensor":
            data_type = "temperature"
        elif sensor_type == "Blood Pressure Sensor":
            data_type = "blood_pressure"
        elif sensor_type == "ECG Sensor":
            data_type = "ecg"
        else:
            raise ValueError(f"Unknown data_type: {sensor_type}")

        # JSON 포맷팅
        formatted_data = {
            "sensor_type": sensor_type,
            "data_type": data_type,
            "data": bio_data.tolist() if hasattr(bio_data, "tolist") else bio_data
        }
        #main 간소화1 self.sensorInfoHistory.append(formatted_data)

        print(f"[Preprocessor] Data successfully formatted for {data_type}.")
        return json.dumps(formatted_data)


