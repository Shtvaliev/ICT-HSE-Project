"""-*- coding: utf-8 -*-"""
# данный скрипт строит
# сводную таблицу по параметрам
# авиакомпания | дальности её рейсов | количество совершённых рейсов

import matplotlib.pyplot as plt
import pandas as pd
from data_import import FILE
from data_import import graphs
from data_import import tables

# file="D:/spyder/анализ данных/flights.csv/flights.csv"
def anna():
    """Functuon Docstring"""
    with open(FILE, 'r', encoding="utf-8"):
        bs = pd.read_csv(FILE, sep=",")
        bs1 = bs.pivot_table(index=['agency', 'distance'],
                             values=['travelCode'], aggfunc='count')
        bs1 = bs1.rename(columns={'travelCode': 'number of flights'})
        # print(bs1)
        # xlsx_plot(bs1)
        s = tables + "Anna's_table.xlsx"
        bs1.to_excel(s)

        bs1.plot.bar(grid=True, figsize=(25, 12))
        plt.xticks(rotation=65, ha='right', fontsize=8)
        s = graphs + 'plot_Anna.png'
        plt.savefig(s)

        # plt.show()


# anna()
