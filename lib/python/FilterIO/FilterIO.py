import pickle


class FilterIO:
    def __init__(self):
        self.__backgroundImg = None
        self.__blockXMLData = None
        self.__filterData = None

    def loadFilterData(self, path):
        with open(path, "rb") as f:
            tmp_dict = pickle.load(f)
        self.__dict__.update(tmp_dict)

    def saveFilterData(self, path):
        with open(path, "wb") as f:
            pickle.dump(self.__dict__, f, pickle.HIGHEST_PROTOCOL)

    def getBlockXMLData(self):
        return self.__blockXMLData

    def getBackgroundImg(self):
        return self.__backgroundImg

    def getFilterData(self):
        return self.__filterData

    def setBlockXMLData(self, data):
        self.__blockXMLData = data

    def setBackgroundImg(self, data):
        self.__backgroundImg = data

    def setFilterData(self, data):
        self.__filterData = data
