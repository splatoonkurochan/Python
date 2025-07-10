import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# CSVファイルを読み込む
df = pd.read_csv("chap3/test.csv", index_col=0)

# 棒グラフを作って表示する
colorlist = ["skyblue","steelblue","tomato","cadetblue","orange","sienna"]
df.T.plot.bar(color = colorlist)
plt.legend(loc="lower right")
plt.savefig("bargraph.png")


