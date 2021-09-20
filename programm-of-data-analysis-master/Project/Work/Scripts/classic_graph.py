# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 10:25:06 2021

@author: Иван
"""

# данный скрипт показывает зависимость
# стоимости полёта от его дальности и
# стоимости полёта от его времени

from collections import OrderedDict
import matplotlib.pyplot as plt

from main import FLIGHTS
from data_import import graphs
# Data_Path = "flights.csv"


def price_from_distance(sx, sy, title):
    pridis = {'': ''}
    del pridis['']
    for i in range(0, FLIGHTS.shape[0]):
        if FLIGHTS[sx][i] not in pridis.keys():
            pridis[float(FLIGHTS[sx][i])] = [float(FLIGHTS[sy][i])]
        else:
            pridis[float(FLIGHTS[sx][i])].append(float(FLIGHTS[sy][i]))
    for row in pridis.keys():
        cnt = 0
        for i in pridis[row]:
            cnt += i
        pridis[row] = cnt / len(pridis[row])

    pridis = OrderedDict(sorted(pridis.items()))
    # print(pridis.keys())
    # print(pridis.values())

    # fig, ax = plt.subplots()
    x = pridis.keys()
    y = pridis.values()

    plt.plot(x, y)
    plt.title(title)
    s = graphs + title + '.png'
    plt.savefig(s)
    plt.clf()


price_from_distance("дистанция", "цена", "Зависимость стоимости от дальности")
price_from_distance("дистанция", "время в пути", "Зависимость стоимости от времени")
