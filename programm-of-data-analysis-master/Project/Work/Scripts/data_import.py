# данный скрипт импортирует данные

import csv
import pandas as pd

def import_database(base, file):
    with open(file) as data:
        database = csv.reader(data)
        count = 0
        for line in database:
            if count > 0:
                base_add = pd.Series([int(line[0]), int(line[1]), line[2],
                                      line[3], line[4], float(line[5]),
                                      float(line[6]), float(line[7]), line[8],
                                      line[9]],
                                     index=["код путешествия",
                                            "код пользователя",
                                            "город вылета", "город прилёта",
                                            "класс", "цена", "время в пути",
                                            "дистанция", "авиакомпания",
                                            "дата"])
                base = base.append(base_add, ignore_index=True)
            else:
                count += 1
    return base

FLIGHTS = pd.DataFrame({"код путешествия": [],
                        "код пользователя": [],
                        "город вылета": [],
                        "город прилёта": [],
                        "класс": [],
                        "цена": [],
                        "время в пути": [],
                        "дистанция": [],
                        "авиакомпания": [],
                        "дата": []})
FLIGHTS = FLIGHTS.astype({"код путешествия": int,
                          "код пользователя": int,
                          "город вылета": str,
                          "город прилёта": str,
                          "класс": str,
                          "цена": float,
                          "время в пути": float,
                          "дистанция": float,
                          "авиакомпания": str,
                          "дата": str})


# FILE = "/Users/shqwerty/git/programm-of-data-analysis/Project/Data/flights2.csv"
with open("Presets.txt") as f:
    FILE = f.readline()
    graphs = f.readline()
    tables = f.readline()

FILE = FILE.replace('Р Р°СЃРїРѕР»РѕР¶РµРЅРёРµ Р°РЅР°Р»РёР·РёСЂСѓРµРјРѕРіРѕ С„Р°Р№Р»Р°: ', '')
FILE = FILE.replace('\n', '')
print(FILE)
graphs = graphs.replace('РџР°РїРєР° РґР»СЏ СЃРѕС…СЂР°РЅРµРЅРёСЏ РіСЂР°С„РёРєРѕРІ: ', '')
graphs = graphs.replace('\n', '')
graphs = graphs + '/'
print(graphs)
tables = tables.replace('РџР°РїРєР° РґР»СЏ СЃРѕС…СЂР°РЅРµРЅРёСЏ С‚Р°Р±Р»РёС†: ', '')
tables = tables.replace('\n', '')
tables = tables + '/'
print(tables)

print("Импорт базы данных...")
FLIGHTS = import_database(FLIGHTS, FILE)
# print(FLIGHTS["дата"])
