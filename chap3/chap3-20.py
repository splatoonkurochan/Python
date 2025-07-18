import pandas as pd
import openpyxl

# CSVファイルを読み込む
df = pd.read_csv("chap3/test.csv")

# ソート（国語の点数が高いもの順）
kokugo = df.sort_values("国語",ascending=False)

# Excelファイルに出力する
kokugo.to_excel("csv_to_excel1.xlsx")
