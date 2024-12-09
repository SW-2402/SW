from Wearable_Device_Sensor import wearable_device_sensor
from body_temperature_sensor import Body_Temperature_Sensor
from sensor_info_preprocessor import Sensor_Info_Preprocessor

from wearable_Device_Sensor import wearble_device_sensor

# Step 1: 센서 객체 생성
body_temp_sensor = Body_Temperature_Sensor()
decorated_sensor = Wearable_Device_Sensor(body_temp_sensor)

# Step 2: 센서를 통해 생체 데이터 추출
raw_data = decorated_sensor.extractBioInfo()
sensor_type = decorated_sensor.getBioInfo()

# Step 3: 데이터를 규격화하고 LSTM 모듈에 전달
preprocessor = Sensor_Info_Preprocessor()
formatted_data = preprocessor.formatBioData(raw_data, sensor_type)
preprocessor.sendToLSTM(formatted_data)
