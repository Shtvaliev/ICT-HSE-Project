# данный скрипт выводит зависимость
# количества рейсов в каждом городе от дня или месяца вылета
import csv
import matplotlib.pyplot as plt
from main import FLIGHTS
from data_import import graphs


def plotting(file, title, width, height, sizee):
    fig, ax = plt.subplots(1, 1)

    x = file.keys()
    y = file.values()

    ax.bar(x, y)

    ax.tick_params(axis='x', labelrotation=90)

    fig.set_figwidth(width)  # ширина
    fig.set_figheight(height)  # высота
    plt.title(title, size=sizee)
    s = graphs + 'bar_flights.png'
    plt.savefig(s)
    plt.clf()


def coppy_of_str(inputt, start, stopp):
    outputt = ''
    for i in range(start, stopp):
        outputt += inputt[i]
    # print('output=',outputt)
    return int(outputt)


def date_inc(i):
    # print(i,'before')
    # print(i % 100)
    i += 1
    if i % 100 > 31:
        i = i - 1 - 30 + 100
    if i % 10000 > 1231:
        i = i - 1 - 1200 + 10000
    # print(i,'after\n')
    return i


def import_first(database, dictionary):
    count = 1
    for i in range(0, database.shape[0]):
        if count > 0:
            s = database["дата"][i]
            s = s.replace("/", "")
            num = int(coppy_of_str(s, 4, 8) * 10000 + coppy_of_str(s, 2, 4) + coppy_of_str(s, 0, 2) * 100)
            if num in dictionary.keys():
                dictionary[num] += 1
            else:
                dictionary[num] = 1
            count += 1
        else:
            count += 1
    del dictionary['']
    return dictionary


def compressor_of_first(dictionary):
    min_date = min(dictionary.keys())
    max_date = max(dictionary.keys())

    i = min_date
    while i < max_date:
        j = i + 1
        while j <= max_date + 1:
            if i in dictionary.keys() and j in dictionary.keys():
                if int(i / 100) == int(j / 100):
                    dictionary[i] += dictionary[j]
                    del dictionary[j]
                    j -= 1
            j = date_inc(j)
        if i in dictionary.keys():
            dictionary[int(i / 100)] = dictionary[i]
            del dictionary[i]
        i = date_inc(i)
    return dictionary


def trans_to_str(dictionary, answer):
    keys = []
    for line in dictionary.keys():
        keys.append(line)
    for line in keys:
        if answer == 'Да' or answer == 'Yes' or answer == '1' or answer == 'yes':
            s = line
            s = str(s % 100) + '.' + str(int(s / 100) % 100) + '.' + str(int(s / 10000))
        else:
            s = str(line)
            s = s[4:] + '.' + s[:4]
        dictionary[s] = dictionary[line]
        del dictionary[line]
    return dictionary


def flights():
    flights_of_date = {
        '': ''
    }

    # print('Строить график по дням? (Yes/No)')
    # answer = input()
    # if answer == 'Да' or answer == 'Yes' or answer == '1' or answer == 'yes':
    #     print('Хорошо, будем строить по дням, но он будет очень большой!\n (Это займёт какое-то время)')
    # else:
    #     print('Ладно, тогда строим по месяцам')

    flights_of_date = import_first(FLIGHTS, flights_of_date)
    answer = 0
    if not (answer == 'Да' or answer == 'Yes' or answer == '1' or answer == 'yes'):
        flights_of_date = compressor_of_first(flights_of_date)
    flights_of_date = trans_to_str(flights_of_date, answer)
    # print(flights_of_date.keys())
    # print(len(flights_of_date.keys()))

    if answer == 'Да' or answer == 'Yes' or answer == '1' or answer == 'yes':
        plotting(flights_of_date, 'Количество рейсов в каждом дне', 160, 15, 50)
    else:
        plotting(flights_of_date, 'Количество рейсов в каждом месяце', 50, 10, 50)


flights()