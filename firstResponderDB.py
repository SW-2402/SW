#!/usr/bin/python
# -*- coding: utf-8 -*-

class FirstResponderDB:
    def __init__(self):
        self.firstResponderInfo = {}

    def getInfo(self, ):
        return self.firstResponderInfo

    def deleteInfo(self, name):
        if name in self.firstResponderInfo:
            del self.firstResponderInfo[name]
            print(f"{name} 정보를 삭제했습니다.")
        else:
            print(f"{name} 정보를 찾을 수 없습니다.")
        pass

    def addInfo(self, name, phone):
        if name in self.firstResponderInfo:
            print(f"{name} 정보가 이미 존재합니다. 업데이트합니다.")
        self.firstResponderInfo[name] = phone
        pass
