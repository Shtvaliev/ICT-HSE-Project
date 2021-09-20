import pandas as pd

from data_import import tables


def digit(base, name):
    base1 = pd.DataFrame({name: [],
                          "максимум": [],
                          "минимум": [],
                          "среднее арифметическое": [],
                          "выборочная дисперсия": [],
                          "стандартное отклонение": []})
    base1 = base1.astype({name: float,
                          "максимум": float,
                          "минимум": float,
                          "среднее арифметическое": float,
                          "выборочная дисперсия": float,
                          "стандартное отклонение": float})

    maxi = base[name].max()
    mini = base[name].min()
    meani = base[name].mean()
    vari = base[name].var()
    stdi = base[name].std()

    count = 0
    for i in range(0, base.shape[0]):
        if count > 0:
            base_add = pd.Series([base[name][i]],
                                 index=[name])
            base1 = base1.append(base_add, ignore_index=True)
        else:
            count += 1
            base_add = pd.Series([base[name][i],
                                  maxi, mini, meani, vari, stdi],
                                 index=[name,
                                        "максимум",
                                        "минимум",
                                        "среднее арифметическое",
                                        "выборочная дисперсия",
                                        "стандартное отклонение"])
            base1 = base1.append(base_add, ignore_index=True)

    s = tables + name + "_standart.xlsx"
    base1.to_excel(s)