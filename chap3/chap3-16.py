import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# CSVファイルを読み込む（名前の列をインデックスで）
df = pd.read_csv("chap3/test.csv", index_col=0)

# 国語の棒グラフを作って表示する
df["国語"].plot.barh()
plt.legend(loc="lower right")
plt.show()

# 国語と数学の棒グラフを作って表示する
df[["国語","数学"]].plot.barh()
plt.legend(loc="lower right")
plt.show()

# C子の棒グラフを作って表示する
df.loc["C子"].plot.barh()
plt.legend(loc="lower right")
plt.show()

# C子の円グラフを作って表示する
df.loc["C子"].plot.pie(labeldistance=0.6)
plt.legend(loc="lower right")
plt.show()
