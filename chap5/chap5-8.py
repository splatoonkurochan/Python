import requests
import json
from pprint import pprint

# ５日間（３時間ごと）の天気を取得する：広島
url = "http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=metric"
url = url.format(city="Hiroshima,JP", key="86c9b401e0f4df9a5824817e26cf856c")

jsondata = requests.get(url).json()
pprint(jsondata)
