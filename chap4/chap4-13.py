import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# データフレームを読み込む
df1 = pd.read_csv("chap4/Sample_20190619102739.csv", index_col="時点")

# 平均気温で折れ線グラフを表示
df1["年平均気温【℃】"].plot()
plt.ylim(-10,40)
plt.show()

