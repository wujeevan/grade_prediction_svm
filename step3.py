from process import *
from sklearn.svm import SVR
import matplotlib.pyplot as plt


preGrade = readxl('train.xls')
followGrade = readxl('test.xls')
x_train, y_train, x_test = getData(preGrade, followGrade)

# 选择线性回归
# linear_svr = SVR(C=0.8, kernel='linear')
# linear_svr.fit(x_train.values, y_train.values[:,0])
# linear_svr_y_predict = linear_svr.predict(x_test.values)
# plt.figure()
# plt.plot(linear_svr_y_predict)

y_test = pd.DataFrame(index=x_test.index)
for i in range(len(y_train.columns)):
    linear_svr = SVR(C=0.7, kernel='linear')
    linear_svr.fit(x_train.values, y_train.values[:,i])
    y_predict = linear_svr.predict(x_test.values)
    y_test[y_train.columns[i]] = y_predict

y_test = y_test.astype(int)
y_test[y_test > 100] = 99
y_test[y_test < 0] = 0

y_test.to_csv('y_prediction.csv', encoding='gbk')

# poly_svr = SVR(C=0.8, kernel='poly')
# poly_svr.fit(x_train.values, y_train.values[:,1])
# poly_svr_y_predict = poly_svr.predict(x_test.values)
# plt.figure()
# plt.plot(poly_svr_y_predict)
#
# rbf_svr = SVR(C=0.8, kernel='rbf')
# rbf_svr.fit(x_train.values, y_train.values[:,1])
# rbf_svr_y_predict = rbf_svr.predict(x_test.values)
# plt.figure()
# plt.plot(rbf_svr_y_predict)
