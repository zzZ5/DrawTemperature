import pandas
import seaborn as sns
import matplotlib.pyplot as plt

data = pandas.read_csv('data1/pH.csv')

ax = sns.lineplot(x="Time/d", y='pH', hue='Group', style='Group',
                  markers=True, data=data)

plt.show()