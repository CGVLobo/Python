from flask import Flask,request,jsonify
from Class.dao.ClientDao import ClientDao
from Class.model.Client import Client
app=Flask(__name__)


@app.route("/client",methods=["GET"])
def clientList():
    dao=ClientDao()
    try:
        return {
            "statusCode":200,
            "data":dao.findAll()
        }
    except:
        return{
            "statusCode":200,
            "msg":"Problemas en la consulta"
        }
@app.route("/client",methods=["POST"])
def insert():
    dao=ClientDao()
    data=request.get_json()
    print(data)
    dao.insert(Client(data["name"],data["age"]).toDict())
    return{
        "msg":"Se ha ingresado correxctamente",
        "statusCode":200
    }

@app.route("/client/<id>",methods=["DELETE"])
def deleteClient(id):
    dao=ClientDao()
    dao.delete(id)
    return{
        "msg":"Se ha eliminado correxctamente",
        "statusCode":200
    }

@app.route("/client/<id>",methods=["PUT"])
def updateClient(id):
    data=request.get_json()
    currentClient=Client(data["name"],data["age"])
    currentClient.setId(id)
    dao=ClientDao()
    dao.update(currentClient.toDict())
    return{
        "statusCode":200
    }

if(__name__=='__main__'):
    app.run(debug=True,port=4500)