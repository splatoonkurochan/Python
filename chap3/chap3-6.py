import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("chap3/test.csv")

# 「名前」の列を削除
print("「名前」の列を削除\n", df.drop("名前",axis=1))

# インデックス２の行を削除
print("インデックス２の行を削除\n", df.drop(2,axis=0))
