
import json

class Sensor_Info_Preprocessor:
    def __init__(self):
        self.sensorInfoHistory = []  # Can be used to store sensor information history
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
            "data_type" : data_type,
            "data": bio_data.tolist() if hasattr(bio_data, "tolist") else bio_data
        }
        self.sensorInfoHistory.append(formatted_data)
        print(f"[Preprocessor] Data formatted for {data_type}")
        return json.dumps(formatted_data)

    def sendToModel(self, formatted_data, model):
        # def sendToLSTM(self, formatted_data, model):
        print("[Preprocessor] Sending formatted data to LSTM model.")
        model.predict(formatted_data)
