import os
from ast import literal_eval
class Migration:
    def __init__(self,path="migrate"):
       self.path=path
       self.listFile=[]
    def getPath(self):
        return self.path 
    def getListPath(self):
        for file in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path,file)) and file.endswith(".py"):
                self.listFile.append(file)
        return self.listFile

    def makeMigration(self):
        for file in self.listFile:
            #print(self.path+"\\"+file)
            with open(self.path+"\\"+file) as currentFile:
                currentData=currentFile.read()
                query="create table "
                table=file.replace(".py","")
                query=query+table+" ("
                currentData=currentData.replace(table+"=","")
                #print(type(currentData))
                currentDict=literal_eval(currentData)
                #print(currentDict)
                #print(type(currentDict))
                #print(currentDict.keys())
                for key in currentDict.keys():
                    #print(key,currentDict[key])
                    query=query+"\n"+key
                    value=currentDict[key]
                    for currentKey in value.keys():
                        query=query+" "+value[currentKey]
                    query=query+","
                query=query[0:-1]
                query=query+")"
                print(query)    


