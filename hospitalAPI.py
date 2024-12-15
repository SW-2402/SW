import requests
import xml.etree.ElementTree as ET
import os
from dotenv import load_dotenv

class HospitalAPI:
    def __init__(self):
        load_dotenv()
        self.hospitalLocation = []
        self.hospitalNumber = []
        self.serviceKey = os.getenv("serviceKey")
        
    def getInfo(self, latitude, longitude):
        self.__searchInfo(latitude, longitude)
        return self.hospitalLocation, self.hospitalNumber
    
    def __findHos(self, xml_data):
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
            
            
    def __searchInfo(self, latitude, longitude):
        url = 'http://apis.data.go.kr/B552657/HsptlAsembySearchService/getHsptlMdcncLcinfoInqire'
        params ={
            'serviceKey' : self.serviceKey, 
            'WGS84_LON' : latitude, 
            'WGS84_LAT' : longitude, 
            'pageNo' : 1, 
            'numOfRows' : 5
        }

        response = requests.get(url, params=params)
        self.__findHos(response.content)
        pass

