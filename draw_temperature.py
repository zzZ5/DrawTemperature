import pandas
import numpy as np
import datetime
import seaborn
import matplotlib.dates as mdates
from matplotlib import pyplot as plt
import matplotlib
from matplotlib.pyplot import MultipleLocator

plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

path_pre = 'data'
data1 = pandas.read_csv(path_pre + '/' + '1' + '.csv')
data2 = pandas.read_csv(path_pre + '/' + '2' + '.csv')
data3 = pandas.read_csv(path_pre + '/' + 't' + '.csv')

data1['newindex'] = np.arange(len(data1)-1, -1, -1)
data1.sort_values('newindex', inplace=True)
data1.drop('newindex', axis=1, inplace=True)
data1['Std'] = data1.std(axis=1)
data1['Average'] = (data1['Value1'] + data1['Value2'] + data1['Value3'])/3
data1['Time'] = data1['Time'].astype('datetime64[ns]')

data2['newindex'] = np.arange(len(data2)-1, -1, -1)
data2.sort_values('newindex', inplace=True)
data2.drop('newindex', axis=1, inplace=True)
data2['Std'] = data2.std(axis=1)
data2['Average'] = (data2['Value1'] + data2['Value2'] + data2['Value3'])/3
data2['Time'] = data2['Time'].astype(
    'datetime64[ns]') + datetime.timedelta(days=6, hours=23)


data3['newindex'] = np.arange(len(data3)-1, -1, -1)
data3.sort_values('newindex', inplace=True)
data3.drop('newindex', axis=1, inplace=True)
data3['Std'] = data3.std(axis=1)
data3['Average'] = (data3['Value1'] + data3['Value2'] + data3['Value3'])/3
data3['Time'] = data3['Time'].astype('datetime64[ns]')


matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'


def format_func(value, tick_number):
    print(value)
    return tick_number


# def format_func(x, pos=None):
#     x = matplotlib.dates.num2date(x)
#     if pos == 0:
#         fmt = '%D %H:%M:%S.%f'
#     else:
#         fmt = '%H:%M:%S.%f'
#     label = x.strftime(fmt)
#     label = label.rstrip("0")
#     label = label.rstrip(".")
#     return label
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(data1['Time'][::], data1['Average'][::], label='堆肥温度1')
ax.plot(data2['Time'][::], data2['Average'][::], label='堆肥温度2')
ax.plot(data3['Time'][::], data3['Average'][::], label='室温')

# l1 = ax.errorbar(data1['Time'][::], data1['Average'][::],
#                  yerr=data1['Std'][::],  label='温度')
# handle1, label1 = ax.get_legend_handles_labels()
ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
ax.xaxis.set_major_locator(mdates.HourLocator(byhour=11))
# ax.set_xticks([0, 1, 2, 3, 4])
ax.set_ylim((0, 80))
ax.set_ylabel('温度(℃)')

ax.set_xlabel('时间(d)')
plt.xlim((18879.4581, 18909))
# if path_pre == 'data1':
#     # plt.xlim((19290.91, 19298.11))
#     # plt.xlim((19290.91, 19297.68))
#     plt.xlim((19290.91, 19297.08))
# if path_pre == 'data2':
#     # plt.xlim((19309.5, 19316.7))
#     plt.xlim((19309.5, 19315.66))
# if path_pre == 'data3':
#     plt.xlim((19317.913, 19324.97))
# lns = l1+l2
# labs = [l.get_label() for l in lns]
# ax.legend(lns, labs, loc='upper left')
# ax1.legend(loc='upper left')
fig.legend(loc="upper right", bbox_to_anchor=(
    1, 1), bbox_transform=ax.transAxes)
plt.show()
# plt.savefig(path_pre + '/+' + str(i) + '.png')
