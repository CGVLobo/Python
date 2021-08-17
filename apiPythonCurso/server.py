from flask import Flask,request

app=Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    return '<h1> hola mundo</h1>'
@app.route("/account",methods=["GET"])
def account():
    person={
        "name":request.args.get('name'),
        "age":request.args.get('age')
    }
    return {
        "statudCode":200,
        "msg":"lka conexion es exitosa",
        "data":person
        }
@app.route("/account",methods=["POST"])
def accountPost():
    data=request.get_json()
    print(type(data))
    print(data)
    return {
        "getData":{
            "name":request.args.get('name'),
            "age":request.args.get('age')
        },
        "postData":data
    }       

@app.route("/account",methods=["PUT"])
def accountPut():
    data=request.get_json()
    print(type(data))
    print(data)
    return {
        "getData":{
            "name":request.args.get('name'),
            "age":request.args.get('age')
        },
        "postData":data
    }

if(__name__=='__main__'):
    app.run(debug=True,port=18999)