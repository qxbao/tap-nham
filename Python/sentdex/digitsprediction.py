# Import một số thư viện cần thiết
# Phần này mình chỉ note một lần duy nhất ở file đầu tiên thôi :) Mọi người có thể tự tìm hiểu thêm nhé
import matplotlib.pyplot as plt # Hiển thị đồ thị
from sklearn import svm # SVM hỗ trợ phân loại dữ liệu (classification)
from sklearn import datasets # Datasets cung cấp các bộ data nổi tiếng có sẵn phục vụ test thuật toán
import numpy as np # Không biết tới thư viện này thì lên W3s học trước đã rồi quay lại sau (QUAN TRỌNG)

dig = datasets.load_digits() # Sử dụng bộ dữ liệu số (có sẵn)

clf = svm.SVC(gamma=0.0001)
# SVC() là hàm giải SVM với gamma là bước nhảy trong kiểm thử đồ thị (khó nói ngắn gọn)[gamma thuộc R+]

x,y = dig.data, dig.target
# Data, target giống như x,y trong phương trình y = f(x). Ở đây, ta tạo hai biến
# và truyền dữ liệu có sẵn từ datasets vào để chuẩn bị giúp máy tìm phương trình chính xác
# để có thể tìm y từ x tùy biến.

clf.fit(x[:],y[:])
# Truyền hai giá trị trên vào hàm SVC, tìm ra phương trình chính xác nhất có thể

# Nhập số ngẫu nhiên để chọn số thứ tự phần tử thử nghiệm
query = int(input("Nhập giá trị từ 1 đến "+str(len(dig.images))+": "))-1

# Hàm clf.predict giúp tìm Y từ X theo phương trình đạt được qua quá trình training
print('Số này có thể là: ',clf.predict([dig.data[query]]))
plt.imshow(dig.images[query]) # Dòng này và dòng dưới chỉ để hiển thị ảnh
plt.show()

# NẾU KHÔNG THỂ CHẠY FILE, VUI LÒNG ĐỌC KỸ FILE README.MD
