import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# CSVファイルを読み込む（名前の列をインデックスで）
df = pd.read_csv("chap3/test.csv", index_col=0)

# 棒グラフを作って表示する
df.plot.bar()
plt.legend(loc="lower right")
plt.show()

# 棒グラフ（水平）を作って表示する
df.plot.barh()
plt.legend(loc="lower right")
plt.show()

# 積み上げ棒グラフを作って表示する
df.plot.bar(stacked=True)
plt.legend(loc="lower right")

# 箱ひげグラフを作って表示する
df.plot.box()
plt.show()

# 面グラフを作って表示する
df.plot.area()
plt.legend(loc="lower right")
plt.show()
