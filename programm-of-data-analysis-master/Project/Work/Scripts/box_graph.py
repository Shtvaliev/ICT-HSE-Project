# данный скрипт строит
# категоризированную диаграмму Бокса-Вискера
# (он же ящик с усами)
# для цены, времени в пути и дистанции полёта

import matplotlib.pyplot as plt
import numpy as np
from data_import import graphs

def ploatting(data):
    fig, ax = plt.subplots()

    plt.boxplot([data["цена"], data["время в пути"], data["дистанция"]], labels=["цена", "время в пути", "дистанция"])

    plt.tick_params(labelsize=40)
    plt.title("Соотношения порядков цены, времени в пути и дистанции", size=50)
    plt.yticks(np.linspace(0, max(data["цена"]), int((max(data["цена"]))/10)))

    fig.set_figwidth(30)  # ширина
    fig.set_figheight(200)  # высота

    s = graphs + 'box_graph.png'
    plt.savefig(s)
    plt.clf()