import numpy as np
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt

x = np.array([[-2,-1],[-1,-2],[1,2],[2,1],[1,1],[-1,-1]])
y = np.array([1,1,2,2,2,1])
# Ta sẽ cho một tập hợp X được dán nhãn theo giá trị (X < 0 <=> Y = 1) và ngược lại. Bạn có thể tùy biến miễn
# vẫn tuân theo một quy tắc nhất định. Đừng cho data quá phức tạp và khó phân loại vào, vì nó ngây thơ lắm...

ptr = GaussianNB()
# Khởi tạo hàm Gaussian

ptr.fit(x,y)
# Đưa biến x và y vào để máy tự tìm điểm chung và phân loại (Training)

plt.scatter(x.T[0],x.T[1])
# plt.show()
# ^^^^^----- Uncomment dòng này để mở đồ thị giúp bạn dễ hiểu hơn về dữ liệu X đầu vào.
# Hàm Gausian sẽ dán nhãn cho các dữ liệu và vẽ một đường phân chia giữa 2 tập hợp dữ liệu
accu = ptr.score(x,y)
# biến accu thể hiện độ chính xác của thuật toán bằng cách thử từng biến Y xem bao nhiêu % trường hợp sẽ xử lý => biến Y
# print(accu) để biết thêm chi tiết (Sẽ xuất kết quả = 1.0, bạn nên thử thêm vài giá trị gây nhiễu để xem sự thay đổi)

print(ptr.predict([[-2,-2]]))
# In kết quả dự đoán với X = [-2,-2] hay bất cứ giá trị nào bạn muốn
