import requests
import xml.etree.ElementTree as ET

class HospitalAPI:
    def __init__(self):
        self.hospitalLocation = []
        self.hospitalNumber = []

    def getInfo(self, latitude, longitude):
        self.searchInfo(latitude, longitude)
        return self.hospitalLocation, self.hospitalNumber
    
    def findHos(self, xml_data):
        root = ET.fromstring(xml_data)
        
        # Extracting header information
        result_code = root.find(".//resultCode").text
        result_msg = root.find(".//resultMsg").text
        print(f"Result Code: {result_code}, Result Message: {result_msg}\n")

        # Extracting body information
        items = root.findall(".//item")
        if not items:
            print("No hospital data found.")
            return

        for item in items:
            duty_name = item.find("dutyName").text if item.find("dutyName") is not None else "N/A"
            duty_addr = item.find("dutyAddr").text if item.find("dutyAddr") is not None else "N/A"
            duty_tel = item.find("dutyTel1").text if item.find("dutyTel1") is not None else "N/A"
            duty_div_name = item.find("dutyDivName").text if item.find("dutyDivName") is not None else "N/A"
            latitude = item.find("latitude").text if item.find("latitude") is not None else "N/A"
            longitude = item.find("longitude").text if item.find("longitude") is not None else "N/A"
            start_time = item.find("startTime").text if item.find("startTime") is not None else "N/A"
            end_time = item.find("endTime").text if item.find("endTime") is not None else "N/A"

            self.hospitalLocation.append(duty_addr)
            self.hospitalNumber.append(duty_tel)
            '''
            print(f"Hospital Name: {duty_name}")
            print(f"Address: {duty_addr}")
            print(f"Phone: {duty_tel}")
            print(f"Category: {duty_div_name}")
            print(f"Latitude: {latitude}, Longitude: {longitude}")
            print(f"Operating Hours: {start_time} - {end_time}")
            print("-" * 40)
            '''
            
            
    def searchInfo(self, latitude, longitude):
        url = 'http://apis.data.go.kr/B552657/HsptlAsembySearchService/getHsptlMdcncLcinfoInqire'
        params ={
            'serviceKey' : 'xeHjoT3CYwwoJcAOini6dIUeT9HggH6jUZDyFs8ni1yxSiJvQOfU8HUGN6BEg29Vl6MdWdGvQrXAyH7SIQDoEA==', 
            'WGS84_LON' : '127.085156592737', 
            'WGS84_LAT' : '37.4881325624879', 
            'pageNo' : 1, 
            'numOfRows' : 5
        }

        response = requests.get(url, params=params)
        self.findHos(response.content)
        pass

