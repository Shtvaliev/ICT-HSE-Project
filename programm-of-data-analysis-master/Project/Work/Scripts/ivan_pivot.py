"""-*- coding: utf-8 -*-"""
# данный скрипт строит
# сводную таблицу по параметрам
# авиакомпания | самый непопулярный город | количество полётов в самом непопулярном городе

import csv

import matplotlib.pyplot as plt
import pandas as pd

from main import FLIGHTS
from data_import import graphs
from data_import import tables


def a_in_b(objectt, base):
    """Functuon Docstring"""
    for look in base:
        if objectt == look:
            return True
    return False


def create_second_base(base):
    """Functuon Docstring"""
    base1 = pd.DataFrame({"авиакомпания": [],
                          "самый непопулярный город": [],
                          "количество полетов в самом непопулярном городе": []})
    base1 = base1.astype({"авиакомпания": str,
                          "самый непопулярный город": str,
                          "количество полетов в самом непопулярном городе": int})
    counter_of_flights = {'': ''}
    del counter_of_flights['']

    for city in base["авиакомпания"]:
        if not a_in_b(city, base1["авиакомпания"]):
            counter_of_flights = {'': int(0)}
            del counter_of_flights['']
            maxi = '0'
            i = 0
            for agency in base["город вылета"]:
                if base["авиакомпания"][i] == city:
                    if agency in counter_of_flights.keys():
                        counter_of_flights[agency] += 1
                    else:
                        counter_of_flights[agency] = int(1)
                    if maxi == '0':
                        maxi = agency
                    if counter_of_flights[agency] < counter_of_flights[maxi]:
                        maxi = agency
                i += 1
            base_add = pd.Series([city, maxi, counter_of_flights[maxi]],
                                 index=["авиакомпания",
                                        "самый непопулярный город",
                                        "количество полетов в самом непопулярном городе"])
            base1 = base1.append(base_add, ignore_index=True)
    return base1


def create_third_base(base):
    """Functuon Docstring"""
    dictionary = {'': 0}
    del dictionary['']
    i = 0
    for agency in base["самый непопулярный город"]:
        if agency in dictionary.keys():
            dictionary[agency] += base["количество полетов в самом непопулярном городе"][i]
        else:
            dictionary[agency] = base["количество полетов в самом непопулярном городе"][i]
        i += 1

    return dictionary


def graph_plot(base):
    """Functuon Docstring"""
    fig, ax = plt.subplots(1, 1)

    x = base.keys()
    y = base.values()

    ax.bar(x, y)

    # fig.set_figwidth(10)  # ширина
    # fig.set_figheight(50)  # высота

    s = graphs + 'plot_Ivan.png'
    plt.savefig(s)
    plt.clf()

def ivan():
    print("Создание таблицы...")
    FLIGT = create_second_base(FLIGHTS)
    s = tables + "Ivan's_table.xlsx"
    FLIGT.to_excel(s)

    print("Постоение графика...")
    graph_plot(create_third_base(FLIGT))


ivan()
