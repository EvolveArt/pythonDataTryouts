# Imports 
import matplotlib.pyplot as plt
import csv
import numpy as np
import urllib
import matplotlib.dates as mdates

# Proportion Chart
"""
days = [i for i in range(1,6)]

sleeping = [7,8,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,7,2,2]
playing=[8,5,7,8,13]

plt.plot([], [], color='m', label='Sleeping', linewidth=5)
plt.plot([], [], color='c', label='Eating', linewidth=5)
plt.plot([], [], color='r', label='Working', linewidth=5)
plt.plot([], [], color='k', label='Playing', linewidth=5)

plt.stackplot(days, sleeping,eating,working,playing, colors=['m', 'c', 'r', 'k'])
"""
# End Proportion Chart

# Pie Chart
"""
slices = [7,2,2,13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0.1,0.1,0.1,0.1),
        autopct='%1.0f%%')
"""
# End Pie Chart

# File Datas (no numpy)
"""
x = []
y = []

with open('example_data.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, label='Loaded from file!')
"""

# With numpy :
"""
x,y = np.loadtxt('example_data.txt', delimiter=',', unpack=True)
plt.plot(x,y, label='Loaded from one file!')
"""
# End File Datas

# Internet Datas
"""
def bytespdate2num(fmt, encoding='utf-8'):
    # Converts bytes to a number 
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

def graph_data(stock):
    # Get the datas from an url and arrange it to make a graph
    # No more yahoo API
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))

    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'

    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                                    delimiter=',',
                                                                    unpack=True,
                                                                    # %Y = full year (2015)
                                                                    # %y partial year (15)
                                                                    # %m number month
                                                                    # %d number day
                                                                    # %H hours
                                                                    # %M minutes
                                                                    # %s seconds
                                                                    # 12-06-2014
                                                                    # %m-%d-%Y
                                                                    converters={0: bytespdate2num('%Y-%m-%d')})

    ax1.plot_date(date, closep, '-', label='Price')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(40)
    ax1.grid(True)#, color='g', linestyle='-', linewidth=5)

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.title('Graph tryouts')
    plt.subplots_adjust(left=0.09, bottom=0.15, right=0.94, top=0.90, wspace=0.5, hspace=0)
    plt.show()
"""
# End Internet Datas

# 3D Plot Surface
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.abs(np.sin(R))

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
"""
# End 3D Plot Surface

# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.title('Graph tryouts')
# plt.show()

# raph_data('TSLA')
