import matplotlib.pyplot as plt
import numpy as np
import pymongo
import pprint as pp
from scipy import stats
import pandas as pd

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb = myclient["MachineLearning"]
mycol = mydb["data"]
colfind = mycol.find_one({'tag':'info'})

# Khai báo tập hợp số đo chiều cao, cân nặng, lọc các giá trị gây nhiễu

height=colfind['height']
weight=colfind['weight']

# Hiển thị các cặp dữ liệu

print(pd.DataFrame({'Cao':height, 'Nặng':weight}))

# Xác lập biến đại số tuyến tính

lin = stats.linregress(height,weight)

# Phương trình đại số tuyến tính sẽ có dạng
# f(x)= ax+b với a, b là các hằng số để tạo nên một đồ thị thẳng
# Theo hàm stats.linregress() bên trên, các phần tử được tạo ra trong
# dictionary có {slope} = {a}, {intercept}={b}
# Vậy nên, ta xây dựng hàm trả lại kết quả phương trình dựa vào x khi có sẵn a,b

getY = np.poly1d([lin.slope, lin.intercept])

# Kiểm tra tính tin cậy của phương trình

print("Độ chính xác kết quả dựa theo dữ liệu đầu vào: {}% ".format(abs(lin.rvalue)*100))
if abs(lin.rvalue)*100 < 60:
    print("==> Có thể đã xuất hiện phần tử đột biến gây nhiễu hoặc dữ liệu đầu vào quá ít")
    print("====> Sai số rất lớn. Đại số tuyến tính không còn phù hợp")

query = int(input("Nhập chiều cao để ước lượng: "))
kqua = getY(query)

print("Cân nặng ước tính: %.2f kg." % kqua)
graf = input("Nhập false nếu bạn không muốn hiển thị đồ thị: ")

if graf != "false":
    # Xây dựng biểu đồ với matplotlib
    cl = np.random.randint(100,size=(len(height)))
    plt.scatter(height,weight,c=cl)
    plt.xlabel("Chiều cao (cm)")
    plt.ylabel("Cân nặng (kg)")
    plt.grid()
    # Xây dựng đường thẳng đại diện phương trình đại số tuyến tính đã lập bên trên
    plt.plot(height,list(map(getY, height)))
    plt.show()
else:
    exit()
