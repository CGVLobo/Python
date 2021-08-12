class Client:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def setId(self,id):
        self.id=id
    def toDict(self):
        return self.__dict__
    def toString(self):
        return "name="+self.name+" age="+str(self.age)+" id="+str(self.id)