import pandas as pd

# データフレームを読み込む
df = pd.read_csv("chap4/898.csv")

print(len(df))
print(df.columns.values)
