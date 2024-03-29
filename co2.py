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
plt.rcParams['font.size'] = 15
path_pre = 'data3'





fig, ax1 = plt.subplots(figsize=(10, 5))

for i in range(1, 6):
    data = pandas.read_csv(path_pre + '/' + 'mr' + str(i) + '.csv')
    co2 = pandas.read_csv(path_pre + '/' + 'CO2-' + str(i) + '.csv')
    data['newindex'] = np.arange(len(data)-1, -1, -1)
    data.sort_values('newindex', inplace=True)
    data.drop('newindex', axis=1, inplace=True)
    data['Std'] = data.std(axis=1)
    data['Average'] = (data['Value1'] + data['Value2'] + data['Value3'])/3

    data['Time'] = data['Time'].astype('datetime64[ns]')

    co2['Time'] = co2['Time'].astype('datetime64[ns]')
    if path_pre == 'data3':
        co2['Consum'] = (co2['Value'] - 400) * 0.03 * 1.429 / 1000
    else:
        co2['Consum'] = (co2['Value'] - 400) * (i *0.2 - 0.1) * 1.429 / 1000

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

   
    # ax.plot(data['Time'][::60], data['Value1'][::60])
    # l1 = ax.errorbar(data['Time'][::], data['Average'][::],
    #                  yerr=data['Std'][::],  label='温度')
    # handle1, label1 = ax.get_legend_handles_labels()
    ax1.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
    if path_pre == 'data2':
        ax1.xaxis.set_major_locator(mdates.HourLocator(byhour=12))
    else:
        ax1.xaxis.set_major_locator(mdates.HourLocator(byhour=22))
    # # ax.set_xticks([0, 1, 2, 3, 4])
    # ax.set_ylim((0, 80))
    # ax.set_ylabel('温度(℃)')

    # ax1 = ax.twinx()
    if i == 1:
        name = 'CK'
    if i == 2:
        name = 'T11'
    if i == 3:
        name = 'T23'
    if i == 4:
        name = 'T36'
    if i == 5:
        name = 'H1'

    ax1.plot(co2['Time'][::], co2['Consum']
                  [::], label= name )

handle2, label2 = ax1.get_legend_handles_labels()
    # ax1.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
    # ax1.xaxis.set_major_locator(mdates.HourLocator(interval=24))


ax1.set_ylabel("氧气消耗速率(μg/min)")
ax1.set_ylim((0, 2.6))


ax1.set_xlabel('时间(d)')

if path_pre == 'data1':
    # plt.xlim((19290.91, 19298.11))
    # plt.xlim((19290.91, 19297.68))
    plt.xlim((19290.915, 19297.08))
if path_pre == 'data2':
    # plt.xlim((19309.5, 19316.7))
    plt.xlim((19309.5, 19315.66))
if path_pre == 'data3':
    plt.xlim((19317.913, 19324.97))
    # lns = l1+l2
    # labs = [l.get_label() for l in lns]
    # ax.legend(lns, labs, loc='upper left')
    # ax1.legend(loc='upper left')

fig.legend(loc="upper right", bbox_to_anchor=(
        1, 1), bbox_transform=ax1.transAxes)
    # plt.show()
plt.savefig(path_pre + '/O2-' + '.png')
