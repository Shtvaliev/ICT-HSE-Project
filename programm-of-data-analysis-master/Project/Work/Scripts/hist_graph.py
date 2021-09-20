# данный скрипт строит гистограмму
# распределения полётов
# по классам

import matplotlib.pyplot as plt
from data_import import graphs


def plotting (data):
    plt.title("Гистограмма распределения полётов по классам")

    plt.hist(data["класс"])

    s = graphs + "Histogram.png"
    plt.savefig(s)
    plt.clf()