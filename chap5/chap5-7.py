import requests
import json

# 現在の天気を取得する：郵便番号160-0006
url = "http://api.openweathermap.org/data/2.5/weather?zip={zipcode}&appid={key}&lang=ja&units=metric"
url = url.format(zipcode="160-0006,JP", key="86c9b401e0f4df9a5824817e26cf856c")

jsondata = requests.get(url).json()
print("都市名  = ",jsondata["name"])
print("気温    = ",jsondata["main"]["temp"])
print("天気    = ",jsondata["weather"][0]["main"])
print("天気詳細 = ",jsondata["weather"][0]["description"])

