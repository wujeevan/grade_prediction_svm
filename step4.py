from process import *


pre_grade_filename = '../成绩预测/2017级（2018-2019-02）预测数据/0535专业/0535专业2016级数据.xls.xls'
follow_grade_filename = '../成绩预测/2017级（2018-2019-02）预测数据/0535专业/0535专业2017级数据.xls'
prediction_filename = '../成绩预测结果/2017级预测结果/0535专业.xls'
pre_grade = read_excel(pre_grade_filename)
follow_grade = read_excel(follow_grade_filename)
x_train, y_train, x_test = get_table(pre_grade, follow_grade)
# get_prediction(filename1, filename2, filename3)



