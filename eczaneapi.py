import http.client
import json

IL_INPUT=input("İl giriniz:")
ILCE_INPUT=input("İlçe giriniz:")

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 5Ll7g1Jps6oyT4gku7BoTa:6tswAKZcSHcxKTVypgSaEN"
    }

STR=("/health/dutyPharmacy?ilce=%s&il=%s" %(ILCE_INPUT,IL_INPUT))

conn.request("GET", STR, headers=headers)

res = conn.getresponse()
data = res.read()
data=data.decode("utf-8")

data=json.loads(data)

if data["success"]:
  F_NAME=data["result"][0]["name"]
  F_ADD=data["result"][0]["address"]
  print(F_ADD,F_NAME)
else:
  print("Herhangi bir kayıt bulunumadı")