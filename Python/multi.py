import pandas as pd
import pymongo
import pprint as pp
import numpy as np
from sklearn import linear_model

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb = myclient["MachineLearning"]
mycol = mydb["data"]
dbquery = pd.Series(mycol.find_one({'tag':'info'},{'_id':0}))

print(dbquery)
# Lấy danh sách từ cơ sở dữ liệu

name=np.array(dbquery['name'])
dob=np.array(dbquery['dob'])
sex=np.array(dbquery['sex'])
height=np.array(dbquery['height'])
weight=np.array(dbquery['weight'])

regr = linear_model.LinearRegression()
regr.fit([height,weight],sex)

print(pd.DataFrame({'Tên':name,'Ngày sinh': dob, 'Giới tính': sex,'Chiều cao':height,'Cân nặng':weight}))
