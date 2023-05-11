import pandas
import seaborn as sns
import matplotlib.pyplot as plt


def myerrorbar(data, x, y, err, color, label=None, **kws):

    # 函数必须要接受data,color,label
    # data其实是待绘制的数据子集sub_data
    # color和label与在matplotlib中的含义一样，因而可以直接用在errorbar里
    # errorbar函数需要x和y的数列，以及标识errorbar的半宽度的数列
    # 如情景描述所说，这些都在我们的data里有，因而此处的sub_data也是有这些数据的，我们只需要按列名将它们提取出来就行
    # 我们使用x,y,err三个str分别指出errorbar需要的三个数列在sub_data中的列名
    # 当没有指定hue参数时，label是不起效的，因此我们默认label为None，这样传参时就不需要指出label了

    if label is None:  # 首先对label的状态进行判断，若无label则无需传给errorbar
        plt.errorbar(x=data[x], y=data[y], yerr=data[err], color=color,
                     ecolor=color, capsize=5, alpha=0.8, marker='.')
    else:
        plt.errorbar(x=data[x], y=data[y], yerr=data[err], color=color,
                     ecolor=color, label=label, capsize=3, alpha=0.8, marker='.')
        # 用data[列名]将需要的数列取出来，与其他参数一道直接传给errorbar
        # 样式直接在函数内部进行设置了，这样比较简单，如果想编写一个通用函数也可以用**kws来传值

# 误差线是会重叠的，这里考虑了两种解决重叠的办法
# 一是alpha=0.8 设置透明度 0为完全透明 1完全不透明
# 二是设置capsize 即误差线的小横线的尺寸，默认为0


data = pandas.read_csv('data1/pH.csv')

sns.set(style="ticks", font_scale=1.5, rc={"lines.linewidth":2.5})
# ax = sns.FacetGrid(data, row="row", col="col",hue="Treatment")
g = sns.lineplot(
    data=data, x="Time/d", y='pH', hue='Treatment', err_style="bars", errorbar='ci',style='Treatment', markers=True, err_kws={'capsize':5}
)
# g.set_xticklabels(['0','1','3','5','7'])
# ax = sns.lineplot(x="Time/d", y='pH', hue='Treatment', style='Treatment',
#                   markers=True, data=data)
# ax.map_dataframe(myerrorbar, x="Time/d", y="pH", err='err')
# ax.map(sns.lineplot, x="Time/d", y='pH', hue='Treatment', style='Treatment', markers=True, data=data)
# ax.set_titles(col_template="{col_name}", row_template="{row_name}")
# ax.add_legend()
plt.show()
