#!/usr/bin/python
# -*- coding: utf-8 -*-

class Model_Observer:
    def __init__(self):
        self.__alert = None

    def setAlert(self, alert):
        self.__alert = alert

    def notifyAlert(self, ):
        print('Model_Observer notifyAlert')
        self.__alert.startEmergency()
