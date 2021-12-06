import matplotlib.pyplot as plt
import numpy as np
import pymongo
import pprint as pp
from scipy import stats
from sklearn.metrics import r2_score
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

# Xác lập biến hồi quy đa thức
# Hàm numpy.polyfit(x,y,z) => Với các tập hợp {x,y} xuất các biến a,b,c,...tạo ra phương trình bậc {z}

gen = np.polyfit(height,weight,3)

# Giải thích: Với {height} = {x} và {weight}={y} và bậc phương trình {z}={3}, xuất các biến a,b,c,d thay thế
# phương trình bậc 3 y = ax^3+bx^2+cx+d tạo nên đồ thị hồi quy đa thức dự đoán các kết quả sau đó
# >> [a b c d]

ptr = np.poly1d(gen)

# Hàm numpy.poly1d() giúp tạo nên phương trình dựa theo kết quả polyfit trả lại
# EX: từ [a b c d] thành ax^3+bx^2+cx+d
# Đã có phương trình, chúng ta cần đưa nghiệm vào để vẽ được đồ thị
# Hàm numpy.linspace(x,y,z) hỗ trợ việc này. Khi ta đưa vào các tham số, hàm sẽ thử từ
# giá trị {x} đến giá trị {y} với {z} số cách đều nhau (Trường hợp không truyền {z} thì {z} mặc định = 5)
# Thêm Endpoint = False để thử tiếp tục thử các giá trị sau {y} chứ k dừng lại

lins = np.linspace(np.amin(height),np.amax(height),100)

trustpoint = r2_score(weight,ptr(height))
print("Độ chính xác của phương trình:{}%".format(trustpoint*100))
if trustpoint*100 < 55:
    print("==> Độ chính xác không cao.")
    print("====> Sẽ xuất hiện sai số.")

# Hàm r2_score(x,y) sẽ trả lại độ chuẩn xác của phương trình hồi quy gồm tập hợp 2 giá trị {x} và {y}

query = int(input("Nhập chiều cao để ước tính cân nặng:"))
kqua = ptr(query)
print("Cân nặng ước tính: %.2fkg " %kqua)

plt.scatter(height,weight)

#         v {x} là các tham số được truyền
#                  v {y} là giá trị phương trình sau khi truyền tham số

plt.plot(lins, ptr(lins))

plt.show()
