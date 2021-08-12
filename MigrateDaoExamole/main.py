from Class.dao.ClientDao import ClientDao
from Class.model.Client import Client

currentClient=Client("Carlos Gonzalez Valenzuela",38)
currentClient.setId(4)
clientDao=ClientDao()
#clientDao.insert(currentClient.toDict())
#clientDao.delete(1)
#clientDao.update(currentClient.toDict())
#print(clientDao.findAll())
for currentClient in clientDao.findAll():
    print(currentClient.toString())

print(clientDao.findOne(4).toString())