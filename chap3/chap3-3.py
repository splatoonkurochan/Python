import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("chap3/test.csv")

# 1列のデータを表示
print("国語の列データ\n",df["国語"])

# 複数の列のデータを表示
print("国語と数学の列データ\n",df[["国語","数学"]])

      
