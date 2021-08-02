from Class.Travel import Travel
from Class.FileManager import FileManager

class Device:
    def __init__(self,id,name,lat,lng):
        self.id=int(id)
        self.name=name
        self.lat=lat
        self.lng=lng
        self.travel=Travel()
    def getDict(self):
        return self.__dict__

    def addPoints(self):
        fileManager=FileManager("files/pointsDevice.txt")
        access=fileManager.readFile()
        if access:
            for line in access:
                id,lat,lng=line.split(",")
                lng=lng.replace("\n","")
                if int(id)==self.id:
                    self.travel.addPoint(lat,lng)

    def printDevicePoint(self):
        print(self.name)
        for point in self.travel.getPoints():
            print(point)