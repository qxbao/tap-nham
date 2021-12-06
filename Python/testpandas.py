import pandas as pd
import pymongo
import pprint as pp
import numpy as np
import math
from sklearn import linear_model

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb = myclient["MachineLearning"]
mycol = mydb["data"]
dbquery = pd.Series(mycol.find_one({'tag':'cccn12'},{'_id':0}))

def checkGender2(x,sx):s
    tmp = np.empty((0,2),int)
    for i in range(len(x)):
        if x[i][2]==sx:
            tmp = np.append(tmp,np.array([[x[i][0],x[i][1]]]),axis=0)
    return tmp;
def checkGender1(x,sx):
    tmp = np.array([])
    for i in range(len(x)):
        if dbquery['sex'][i]==sx:
            tmp = np.append(tmp,x[i])
    return tmp;

name=np.array(dbquery['name'])
dob=np.array(dbquery['dob'])
sex=np.array(dbquery['sex'])
height=np.array(dbquery['height'])
weight=np.array(dbquery['weight'])

print("DỰ ĐOÁN NGÀY THÁNG SINH VỚI CHIỀU CAO & CÂN NẶNG (2004):")
print(pd.DataFrame({'Tên':name,'Ngày sinh': dob, 'Giới tính': sex,'Chiều cao':height,'Cân nặng':weight}))
gendercheck = input("\nBạn muốn kiểm tra giới tính nào? (F/M): ")
if gendercheck == 'F':
    print("Giới tính kiểm tra: Nữ")
    sexinp = 0;
elif gendercheck == 'M':
    print("Giới tính kiểm tra: Nam")
    sexinp = 1;
else:
    print("Giá trị nhập vô nghĩa. Tự kết thúc chương trình")
    exit()

inp = np.array([height,weight]).T
aftercheck = checkGender2(np.array([height,weight,sex]).T,sexinp)
aftersex  = checkGender1(dob,sexinp)

regr = linear_model.LinearRegression()
regr.fit(aftercheck,aftersex)

print("CHÚ Ý: Tránh nhập các dữ liệu gây nhiễu như cân nặng, chiều cao quá khác biệt so với giá trị trung bình")
preh = int(input("Nhập chiều cao: "))
prew = int(input("Nhập cân nặng: "))

kqua = regr.predict([[preh,prew]])
date = math.floor(kqua%30)
month = math.floor((kqua-date)/30)
year = 2004;
if month <= 0 or month >12:
    print("Có sự cố trong dự đoán. Chương trình tự động kết thúc")
    exit()
print('Bạn có thể sinh vào ngày {0} tháng {1} năm {2}'.format(date,month,year))
