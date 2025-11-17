import pandas
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams.update({'font.size': 16})


data = pandas.read_csv('O2/to2.csv')
# sns.set(style="ticks", rc={"lines.linewidth":2.5})
# Plot the responses for different events and regions

line = sns.lineplot(x='timepoint', y='value', hue='treatment',
             style="treatment", markers=True, data=data, linewidth = 2.5)
# 提取线条
lines = line.get_lines()
# 设置每条线的marker大小
marker_size = 8  # 你想要设置的marker大小
for line in lines:
    line.set_markersize(marker_size)


plt.xlabel('时间（d）')
plt.ylabel('氧气累计消耗量（g）')
plt.show()
