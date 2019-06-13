import numpy as np
import pandas as pd
import xlrd

colnames = ('NO_', 'COURE_NAME', 'ZHSCORE')
filename = 'train.xls'
book = xlrd.open_workbook(filename, 'r')
sheet = book.sheet_by_index(0)
result = dict()
for i in range(sheet.ncols):
    if sheet.cell_value(0,i) in colnames:
        result[sheet.cell_value(0,i)] = sheet.col_values(i,1)
result = pd.DataFrame(result)
result = result.replace('', np.nan)
result = result.dropna()
result = result.pivot_table(index=colnames[0], columns=colnames[1], values=colnames[2], fill_value=0)
t = result[result > 0].count()
idx = t[t < len(result)/2].index
result = result.drop(idx, 1)
result[result > 100] = result - 60