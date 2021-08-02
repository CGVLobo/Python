from Class.Device import Device
from Class.FileManager import FileManager

devices=[]
addeds=[]
fileManager=FileManager("files/devices.txt")
access=fileManager.readFile()
if access:
    for line in access:
        id,name,lat,lng=line.split(",")
        lng=lng.replace("\n","")
        if id not in addeds:
            addeds.append(id)
            currentDevice=Device(id,name,lat,lng)
            devices.append(currentDevice)    

    #for device in devices:
     #   if(device["id"]==2):
      #      print(device)
    try:
        currentDevice=list(element for element in devices if element["id"]==2)[0]
        print(currentDevice)
    except:
        print("no esta el elemento")

else:
    print("hay algun problema")

for device in devices:
    device.addPoints()

for device in devices:
    print(device.printDevicePoint())
