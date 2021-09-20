import pandas as pd
import numpy as np

from data_import import tables


def stringg(base, name):
    base1 = pd.DataFrame({name: [],
                          "частота появления": [],
                          "процент от общего количества": [],})
    base1 = base1.astype({name: str,
                          "частота появления": int,
                          "процент от общего количества": str})

    # base1 = base1.append(base[name].value_counts(), ignore_index=True)
    base_add = base[name].value_counts()
    for line in base_add.index:
        base_add2 = pd.Series([line, base_add[line]], index=[name, "частота появления"])
        base1 = base1.append(base_add2, ignore_index=True)

    for i in range(0, base1.shape[0]):
        k = base1["частота появления"][i] / base1["частота появления"].sum() * 100
        round(k, 2)
        base1["процент от общего количества"][i] = str(k) + ' %'
    s = tables + name + "_standart.xlsx"
    base1.to_excel(s)
