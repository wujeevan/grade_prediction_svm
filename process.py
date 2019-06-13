import numpy as np
import pandas as pd
from sklearn.svm import SVR
import xlrd
import os
import sys


def read_excel(filename, col_names = ('NO_', 'COURE_NAME', 'ZHSCORE')):
    book = xlrd.open_workbook(filename, 'r')
    sheet = book.sheet_by_index(0)
    result = dict()
    for i in range(sheet.ncols):
        if sheet.cell_value(0,i) in col_names:
            result[sheet.cell_value(0,i)] = sheet.col_values(i,1)
    result = pd.DataFrame(result)
    result = result.replace('', np.nan)
    result = result.dropna()
    try:
        result = result.pivot_table(index=col_names[0], columns=col_names[1], values=col_names[2], fill_value=0)
    except Exception:
        print(filename + '文件内容为空')
    t = result[result > 0].count()
    idx = t[t < len(result) / 2].index
    result = result.drop(idx, 1)
    result[result > 100] = result - 60
    return result


def get_table(pre_grade, follow_grade):
    s1 = set(pre_grade.columns)
    s2 = set(follow_grade.columns)
    x_col = list(s1 & s2)
    y_col = list(s1 - (s1 & s2))
    x_train = pre_grade[x_col]
    y_train = pre_grade[y_col]
    x_test = follow_grade[x_col]
    return x_train, y_train, x_test


def predict(x_train, y_train, x_test):
    y_test = pd.DataFrame(index=x_test.index)
    for i in range(len(y_train.columns)):
        linear_svr = SVR(C=0.7, kernel='linear')
        linear_svr.fit(x_train.values, y_train.values[:, i])
        y_predict = linear_svr.predict(x_test.values)
        y_test[y_train.columns[i]] = y_predict
    y_test = y_test.astype(int)
    y_test[y_test > 100] = 99
    y_test[y_test < 0] = 0
    return y_test


def get_prediction(pre_grade_filename, follow_grade_filename, prediction_filename):
    try:
        pre_grade = read_excel(pre_grade_filename)
        follow_grade = read_excel(follow_grade_filename)
        x_train, y_train, x_test = get_table(pre_grade, follow_grade)
        y_prediction = predict(x_train, y_train, x_test)
        y_prediction.to_excel(prediction_filename)
    except Exception:
        print('课程完全重合，无预测科目')


def process_grade(grade_dir, result_dir):
    major = os.listdir(grade_dir)
    for cur_major in major:
        cur_dir = grade_dir + '/' + cur_major
        files = os.listdir(cur_dir)
        filepath = []
        for cur_files in files:
            filepath.append(cur_dir + '/' + cur_files)
        print(cur_major + ':')
        get_prediction(filepath[0], filepath[1], result_dir + '/' + cur_major + '.xls')

if __name__ == '__main__':
    gradedir = '../成绩预测/2018级（2018-2019-02）预测数据'
    resultdir = '../成绩预测结果/2018级（2018-2019-02）预测结果'
    process_grade(gradedir, resultdir)





