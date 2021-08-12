from Class.ConnectionHandler import ConnectionHandler
from Class.model.Client import Client
class ClientDao:
    
    def __init__(self):
        self.handler=ConnectionHandler("LAPTOP-IU8SOAQU\SQLEXPRESS","pythonBD","loboCGV","detonador")

    def insert(self,client):
        query="insert into client values ('"+client["name"]+"',"+str(client["age"])+")"
        self.handler.executeQuery(query)
    def delete(self,clientId):
        query="delete from client where id="+str(clientId)
        self.handler.executeQuery(query)
    def update(self,client):
        query="update client set name='"+client["name"]+"', age="+str(client["age"])+" where id="+str(client["id"])
        self.handler.executeQuery(query)
    def findAll(self):
        query="select * from client"
        result=self.handler.executeSelect(query)
        clientList=[]
        for currentClient in result:
            newClient=Client(currentClient[1],currentClient[2])
            newClient.setId(currentClient[0])
            clientList.append(newClient)
        return clientList
        
    def findOne(self,clientId):
        query="select * from client where id="+str(clientId)
        result=self.handler.executeSelect(query)
        newClient=None
        for currentClient in result:
            newClient=Client(currentClient[1],currentClient[2])
            newClient.setId(currentClient[0])
        return newClient
