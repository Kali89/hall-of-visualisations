#!/usr/bin/python
import datetime
import matplotlib.pyplot as plt
import numpy as np
import calendar
from scipy import stats

def group(lst, n):
    """
    Group data into the specified number of groups
    """
    return zip(*[lst[i::n] for i in range(n)])


datey_dictionary = {}
months = iter(calendar.month_name)
## Blank first month
months.next()

with open('price_summary_by_month.txt', 'rb') as f:
    for line in f.readlines():
        datey, price = line.split('\t')
        datey = datetime.datetime.strptime(datey, '%Y-%m')
	price = float(price.strip('\n'))
	try:
	    datey_dictionary[datey.year].append(price)
	except:
	    datey_dictionary[datey.year] = [price]

pricey_dictionary = {}
for entry in datey_dictionary.keys():
    for index in range(len(datey_dictionary[entry])):
	if entry == 2014:
	    continue
	try:
	    pricey_dictionary[index].append(datey_dictionary[entry][index]/sum(datey_dictionary[entry]))
	except:
	    pricey_dictionary[index] = [datey_dictionary[entry][index]/sum(datey_dictionary[entry])]


for entry in group(pricey_dictionary.keys(),3):
    legend_list = []
    for enter in entry:
	density = stats.kde.gaussian_kde(pricey_dictionary[pricey_dictionary.keys()[enter]])
	x = np.arange(0.065, 0.095, 0.0005)
	plt.plot(x, density(x))
	legend_list.append(months.next())
    plt.xlabel("% of year's total value")
    plt.ylabel("Density")
    plt.legend(legend_list, loc=2)
    plt.show()
