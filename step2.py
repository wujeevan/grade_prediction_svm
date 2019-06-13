import numpy as np
import pandas as pd
from process import *


train = readxl('train.xls')
test = readxl('test.xls')

s1 = set(train.columns)
s2 = set(test.columns)
x_col = list(s1 & s2)
y_col = list(s1 - (s1 & s2))
x_train = train[x_col]
y_train = train[y_col]
x_test = test[x_col]

