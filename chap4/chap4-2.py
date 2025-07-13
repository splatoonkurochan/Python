import pandas as pd

# データフレームを読み込む
df = pd.read_csv("chap4/13TOKYO.CSV", header=None, encoding="shift_jis")

# 「２」の列が「１６００００６」の住所を抽出して表示
results = df[df[2] == 1600006]
print(results[[2,6,7,8]])
