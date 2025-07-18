import requests
from pathlib import Path

# 保存用フォルダを作る
out_folder = Path("dawnload")
out_folder.mkdir(exist_ok=True)

# 画像ファイルを取得する
image_url = "https://ymori.com/books/python2nen/sample1.png"
imgdata = requests.get(image_url)

# URLから最後のファイル名を取り出して、保存フォルダ名とつなげる
filename = image_url.split("/")[-1]
out_path = out_folder.joinpath(filename)

# 画像データを、ファイルに書き出す
with open(out_path, mode="wb") as f:
    f.write(imgdata.content)
    