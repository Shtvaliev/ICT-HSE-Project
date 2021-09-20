# этот скрипт считает, сколько отправлений и
# посадок было совершено в каждом городе
import csv
from collections import OrderedDict
import matplotlib.pyplot as plt
from main import FLIGHTS
from data_import import graphs


def plotting(file, title, width, height, sizee):
    fig, ax = plt.subplots(1, 1)

    file = OrderedDict(sorted(file.items()))

    x = file.keys()
    y = file.values()

    ax.bar(x, y)

    fig.set_figwidth(width)  # ширина
    fig.set_figheight(height)  # высота
    plt.title(title, size=sizee)
    s = graphs + "bar_cityes.png"
    plt.savefig(s)
    plt.clf()


def import_second(database, column):
    dictionary = {'': ''}
    del dictionary['']
    count = 0
    for line in database:
        if count != 0:
            if line[column] in dictionary.keys():
                dictionary[line[column]] += 1
            else:
                dictionary[line[column]] = 1
        count += 1
    return dictionary

def cityes():
    city_departure = {'': ''}
    city_arrivals = {'': ''}

    city_departure = import_second(FLIGHTS, 2)
    city_arrivals = import_second(FLIGHTS, 3)

    plotting(city_departure, 'Количество отправлений в каждом городе', 20, 10, 25)
    plotting(city_arrivals, 'Количество прибытий в каждом году', 20, 10, 25)


cityes()
