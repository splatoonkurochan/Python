import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("chap3/test.csv")

# 1列のデータを表示
print("C子のデータ\n",df.loc[2])

# 複数の列のデータを表示
print("C子とD郎のデータ\n",df.loc[[2,3]])

# 指定した行の指定した列のデータを表示
print("C子の国語データ\n", df.loc[2]["国語"])
      

      
