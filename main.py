from wearable_Device_Sensor import Wearable_Device_Sensor
from body_Temperature_Sensor import Body_Temperature_Sensor
from sensor_Info_Preprocessor import Sensor_Info_Preprocessor
from model import Model
# Step 1: 센서 객체 생성
body_temp_sensor = Body_Temperature_Sensor()
decorated_sensor = Wearable_Device_Sensor(body_temp_sensor)

# Step 2: 센서를 통해 생체 데이터 추출
raw_data = decorated_sensor.extractBioInfo()
sensor_type = decorated_sensor.getBioInfo()

# Step 3: 데이터를 규격화하고 LSTM 모듈에 전달
preprocessor = Sensor_Info_Preprocessor()

lstm_model = Model()

formatted_data = preprocessor.getFormattedBioData(raw_data, sensor_type)
# preprocessor.sendToLSTM(formatted_data, lstm_model)

# 데이터를 모델에 전달 및 예측
prediction = lstm_model.predict(formatted_data)

# 상태 확인
state = lstm_model.notifyState(prediction)
print("Current State:", state)