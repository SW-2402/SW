#!/usr/bin/python
# -*- coding: utf-8 -*-

class Model:
    def __init__(self):
        self.modelName = None
        self.observer_list = []

    def predict(self, ):
        pass

    def notifyState(self, ):
        for observer in self.observer_list:
            observer.notifyAlert()

    def subObserver(self, observer):
        self.observer_list.append(observer)

    def unsubObserver(self, observer):
        self.observer_list.remove(observer)
