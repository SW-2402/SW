
# Model Interface
class Model:
    def __init__(self):
        self.__modelName = None
        self.__observer_list = []
        self.__preprocessor = None

    def predict(self, sensor):
      pass
    
    def notifyState(self, ):
        for observer in self.observer_list:
            observer.notifyAlert()

    def subObserver(self, observer):
        self.observer_list.append(observer)

    def unsubObserver(self, observer):
        self.observer_list.remove(observer)
