"""-*- coding: utf-8 -*-"""
# данный скрипт строит
# сводную таблицу по параметрам
# город вылета | самая популярная авиакомпания | количество полётов этой компании

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
    base1 = pd.DataFrame({"город вылета": [],
                          "самая популярная авиакомпания": [],
                          "количесвое полётов самой популярной авиакомпании": []})
    base1 = base1.astype({"город вылета": str,
                          "самая популярная авиакомпания": str,
                          "количесвое полётов самой популярной авиакомпании": int})
    counter_of_flights = {'': ''}
    del counter_of_flights['']

    for city in base["город вылета"]:

        # print(city)
        if not a_in_b(city, base1["город вылета"]):
            counter_of_flights = {'': int(0)}
            del counter_of_flights['']
            maxi = '0'
            i = 0
            for agency in base["авиакомпания"]:
                # print(BASE["город вылета"][i], "==", city)
                if base["город вылета"][i] == city:
                    if agency in counter_of_flights.keys():
                        counter_of_flights[agency] += 1
                    else:
                        counter_of_flights[agency] = int(1)
                        # print(agency)
                    # print(counter_of_flights)
                    if maxi == '0':
                        maxi = agency
                    # print(maxi)
                    if counter_of_flights[agency] > counter_of_flights[maxi]:
                        maxi = agency
                        # print(maxi)
                i += 1
            base_add = pd.Series([city, maxi, counter_of_flights[maxi]],
                                 index=["город вылета", "самая популярная авиакомпания",
                                        "количесвое полётов самой популярной авиакомпании"])
            base1 = base1.append(base_add, ignore_index=True)

    return base1


def create_third_base(base):
    """Functuon Docstring"""
    dictionary = {'': 0}
    del dictionary['']
    i = 0
    for agency in base["самая популярная авиакомпания"]:
        if agency in dictionary.keys():
            dictionary[agency] += base["количесвое полётов самой популярной авиакомпании"][i]
        else:
            dictionary[agency] = base["количесвое полётов самой популярной авиакомпании"][i]
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

    s = graphs + 'plot_Shamil.png'
    plt.savefig(s)
    plt.clf()


def shamil():
    print("Создание таблицы...")
    FLIGT = create_second_base(FLIGHTS)
    s = tables + "Shamil's_table.xlsx"
    FLIGT.to_excel(s)

    print("Постоение графика...")
    graph_plot(create_third_base(FLIGT))


shamil()
