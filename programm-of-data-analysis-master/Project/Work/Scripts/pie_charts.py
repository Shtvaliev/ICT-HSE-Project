# -*- coding: utf-8 -*-
# этот скрипт счиатет распределение полётов по авиакомпаниям
# и цен по классам

import csv

import matplotlib.pyplot as plt
# import numpy as np
from main import FLIGHTS
from data_import import graphs


# Data_Path="D:/spyder/анализ данных/flights.csv/flights.csv"

def flights_from_agency():
    agencies = []
    number_of_flights = []
    for i in range(0, FLIGHTS.shape[0]):
        if FLIGHTS["авиакомпания"][i] in agencies:
            number_of_flights[agencies.index(FLIGHTS["авиакомпания"][i])] += 1
        else:
            agencies.append(FLIGHTS["авиакомпания"][i])
            number_of_flights.append(1)
    # print(agencies)
    # print(number_of_flights)

    """sum=0
    for i in number_of_flights:
        sum +=i"""

    fig, ax = plt.subplots()
    ax.pie(number_of_flights, labels=agencies, autopct='%1.1f%%',
           colors={'#FF0000', '#FF8C00', '#00FF00', '#ADFF2F', '#00FFFF', '#9400D3', '#0000FF', 'm'})
    ax.axis("equal")

    plt.title('Количесво полётов авиакомпании')
    s = graphs + 'pie_charts1.png'
    plt.savefig(s)
    plt.clf()


def avarage_price_from_class():
    type_of_flight = []
    price_of_type = []
    number_of_flights = []
    for i in range(0, FLIGHTS.shape[0]):
        if FLIGHTS["класс"][i] in type_of_flight:
            price_of_type[type_of_flight.index(FLIGHTS["класс"][i])] += float(FLIGHTS["цена"][i])
            number_of_flights[type_of_flight.index(FLIGHTS["класс"][i])] += 1
        else:
            type_of_flight.append(FLIGHTS["класс"][i])
            price_of_type.append(float(FLIGHTS["цена"][i]))
            number_of_flights.append(1)

    average = []
    for i in range(len(type_of_flight)):
        average.append(round((price_of_type[i] / number_of_flights[i]), 2))

    # print(type_of_flight, "1")
    # print(average, "@")

    fig, ax = plt.subplots()
    ax.pie(average, labels=type_of_flight, autopct='%1.1f%%',
           colors={'c', 'm', '#DC143C', '#FF69B4', '#9400D3', '#00FF00', '#000080'})
    ax.axis("equal")
    plt.title('Зредняя цена за класс')

    s = graphs + 'pie_charts2.png'
    plt.savefig(s)
    plt.clf()


def pie():
    flights_from_agency()
    avarage_price_from_class()


pie()
