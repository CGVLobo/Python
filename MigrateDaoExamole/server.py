from flask import Flask,request,jsonify
from Class.dao.ClientDao import ClientDao
from Class.model.Client import Client
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app=Flask(__name__)
app.config["JWT_SECRET_KEY"]="qwerty"
jwt=JWTManager(app)

@app.route("/login",methods=["POST"])
def login():
    username=request.json.get("username",None)
    passwd=request.json.get("passwd",None)
    #print(hash(passwd))
    #validar usuario
    if username!="test" or passwd!="test":
        return jsonify({"msg":"no existe usuario"}),401
    
    access_token=create_access_token(identity=username)
    return jsonify(access_token=access_token)


@app.route("/client",methods=["GET"])
@jwt_required()
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
@jwt_required()
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