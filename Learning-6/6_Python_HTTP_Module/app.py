import http.client
import json

conn = http.client.HTTPSConnection('dummyjson.com')
conn.request("GET", "/products")

response = conn.getresponse()

print(response.status)
print(response.headers)

data = response.read()
pyObj = json.loads(data)
# jsonData = json.dumps(pyObj, indent=4)
print(pyObj)



