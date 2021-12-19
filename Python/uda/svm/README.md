# SVM (Support Vector Machine)

**Lưu ý**: Bạn nên tìm hiểu *"Bayes ngây thơ"* trước khi chuyển tới phần này để biết rõ được sự khác biệt và lựa chọn thuật toán phù hợp.

## Khác biệt

Chắc bạn còn nhớ lí do tại sao thuật toán Bayes ngây thơ lại "ngây thơ" nhỉ? Dù sao thì mình cũng sẽ nhắc lại. Thuật toán Naive Bayes giả định các dữ kiện đầu vào tồn tại độc lập, không tồn tại liên hệ với nhau. SVM không như vậy, thuật toán này đưa ra dự đoán dựa vào sự liên kết giữa các dữ liệu trong một mức độ nhất định. Tuy nhiên, điều này không đồng nghĩa với việc SVM tốt hơn Naive Bayes, nên nhớ rằng:

> Không có thuật toán nào tốt hơn thuật toán nào, chỉ có thuật toán nào phù hợp hơn mà thôi
\- [No free lunch theorem](https://en.wikipedia.org/wiki/No_free_lunch_theorem)

*Nếu có phần nào không hiểu, hãy tự tin liên hệ mình để được hỗ trợ nhé. Mình chắc chắn không phải chuyên gia về lĩnh vực này, nhưng mình sẽ giúp đỡ bạn trong khả năng có thể ^^*

## SVC (Support Vector Classification)

Để sử dụng hàm SVC(), ta khai báo như sau:

```sh
from sklearn import svm
clf = svm.SVC()
```

Khi khai báo, ta có thể truyền vào các tham số thay vì sử dụng tham số mặc định:

```sh
sklearn.svm.SVC(*, C=1.0, kernel='rbf', degree=3, gamma='scale', coef0=0.0,
shrinking=True, probability=False, tol=0.001, cache_size=200, class_weight=None,
verbose=False, max_iter=- 1, decision_function_shape='ovr', break_ties=False, random_state=None)
```

Mình sẽ nói về một vài tham số quan trọng thôi nhé, mà cụ thể ở đây là **kernel**, **gamma** và **C**

### Kernel:

Kernel (nhân xử lý) như trái tim của một thuật toán. Việc bạn chọn một kernel sẽ quyết định kết quả bạn nhận được. Xem ví dụ sau đây:

![kernel](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_svc_001.png)

Chúng ta có một số lựa chọn sau cho tham số kernel:
- *linear*
- *poly*
- *rbf*
- *sigmoid*
- *precomputed*
với giá trị mặc định là **rbf**

### C:

**Lưu ý**: *C phải là giá trị dương*

Độ lớn C thể hiện mong muốn tránh việc phân loại sót data của người dùng. Ừm...nói sao cho dễ hiểu nhỉ.

Như này đi. Trong một dataset, thường tồn tại giá trị nhiễu khác rất nhiều với giá trị trung bình.

**Ví dụ:** Dataset chiều cao - cân nặng xuất hiện trường hợp 190cm - 45kg hay 1m44 - 80kg, khác biệt lớn so với giá trị trung bình 170cm - 63kg

Với C = 1.0, đa số các giá trị nhiễu sẽ bị bỏ qua nhằm giữ margin lớn nhất, qua đó tối ưu kết quả. Nhưng với C = 1000.0, thuật toán sẽ cố gắng phân loại chính xác cả những giá trị nhiễu. Để quan sát được sự thay đổi một cách rõ ràng, bạn nên thử nghiệm với kernel rbf.

![c](https://i.stack.imgur.com/jfJ9G.png)

Xin hãy nhớ rằng, việc C càng lớn không đồng nghĩa với tính chính xác của thuật toán càng tăng.

### Gamma:

Độ lớn gamma tỉ lệ nghịch với tầm ảnh hưởng của từng điểm dữ liệu. Càng cố giải thích sẽ càng rối và khó hiểu, hãy nhìn ảnh và đọc lại câu đầu tiên.

![gamma](https://prwatech.in/blog/wp-content/uploads/2020/02/SVM15.png)

Như bạn thấy, đường phân chia với gamma lớn sẽ không xét tới những điểm nằm ngoài một phạm vi nhất định (tỉ lệ thuận với gamma) và ngược lại.

### Overfitting:

Overfitting là tình trạng mô hình quá khớp với dữ liệu training. Điều này có gì không tốt sao? Ừ thì, nó khớp với dữ liệu training là một chuyện, nhưng có khớp với dữ liệu test và các data ngoài hay không lại là một chuyện khác. Dù sao thì, chúng ta cần tránh overfitting hoặc kết quả dự đoán sẽ có sai lệch.

![overfitting](https://labs.flinters.vn/wp-content/uploads/2016/12/Screen-Shot-2016-12-05-at-5.06.47-PM.png)

Vậy phải làm sao để tránh việc dính over/underfitting? Điều này phụ thuộc vào việc bạn khai báo 3 tham số C, kernel và gamma bên trên ra sao để mọi thứ đi đúng quỹ đạo của nó.
