class Travel:
    def __init__(self):
        self.points=[]
    def addPoint(self,lat,lng):
        self.points.append((lat,lng))
    def getPoints(self):
        return self.points