import requests
from requests.api import post
#request
#response

url="http://localhost:4500/client"

data={
    "name":"Julia",
    "age":26
}
#response=requests.post(url,json=data)
#print(response)
#print(response.json())

#response=requests.get(url)
#print(response)
#print(response.json())

loginData={
    "username":"test",
    "passwd":"test"    
}
response=requests.post("http://localhost:4500/login",json=loginData)
print(response)
print(response.json()["access_token"])
token=response.json()["access_token"]
headers={'Authorization':'Bearer {}'.format(token)}

response=requests.get(url,headers=headers)
print(response)
print(response.json())

response=post(url,json=data,headers=headers)
print(response)
print(response.json())