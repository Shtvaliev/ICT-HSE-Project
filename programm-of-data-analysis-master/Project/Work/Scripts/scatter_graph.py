# данный скрипт строит
# категоризированную диаграмму рассеивания
# зависимости цены от времени полёта

import matplotlib.pyplot as plt
from data_import import graphs

def plotting (data):
    fig, ax = plt.subplots()

    x = data["время в пути"]
    y = data["цена"]

    ax.scatter(x, y)

    fig.set_figwidth(30)  # ширина
    fig.set_figheight(30)  # высота

    plt.tick_params(labelsize=40)
    plt.title("Зависимость цены от времени полёта", size=50)

    s = graphs + 'Scatter.png'
    plt.savefig(s)
    plt.clf()
