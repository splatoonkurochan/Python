import pandas as pd

# データフレームを読み込む
df = pd.read_csv("chap4/200.csv",encoding="shift-jis")

print(len(df))
print(df.columns.values)
