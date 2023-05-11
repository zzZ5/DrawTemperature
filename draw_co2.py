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

path_pre = 'data3'
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
        co2['Consum'] = (co2['Value'] - 400) * 300
    else:
        co2['Consum'] = (co2['Value'] - 400) * (i * 200 - 100)

    matplotlib.rcParams['xtick.direction'] = 'in'
    matplotlib.rcParams['ytick.direction'] = 'in'

    def format_func(value, tick_number):
        print(value)
        return tick_number

    fig, ax = plt.subplots(figsize=(10, 5))
    handle1, label1 = ax.get_legend_handles_labels()
    ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
    ax.xaxis.set_major_locator(mdates.HourLocator(byhour=22))
    l2 = ax.plot(co2['Time'][::], co2['Value']
                 [::], color='teal', label='CO2浓度')
    handle2, label2 = ax.get_legend_handles_labels()
    # ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
    # ax.xaxis.set_major_locator(mdates.HourLocator(interval=24))
    ax.set_ylabel("CO2浓度(ppm)")
    # ax.set_ylim((0, 12000000))
    # y_major_locator = MultipleLocator(1000000)
    ax.set_ylim((0, 60000))
    # ax.yaxis.set_major_locator(y_major_locator)

    ax.set_xlabel('时间(d)')

    if path_pre == 'data1':
        # plt.xlim((19290.91, 19298.11))
        # plt.xlim((19290.91, 19297.68))
        plt.xlim((19290.91, 19297.08))

    if path_pre == 'data2':
        # plt.xlim((19309.5, 19316.7))
        plt.xlim((19309.5, 19315.66))

    if path_pre == 'data3':
        plt.xlim((19317.913, 19324.97))
    # lns = l1+l2
    # labs = [l.get_label() for l in lns]
    # ax.legend(lns, labs, loc='upper left')
    # ax.legend(loc='upper left')

    fig.legend(loc="upper right", bbox_to_anchor=(
        1, 1), bbox_transform=ax.transAxes)
    # plt.show()
    plt.savefig(path_pre + '/CO2+' + str(i) + '.png')
