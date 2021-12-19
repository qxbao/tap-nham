# Naive Bayes (Bayes ngây thơ)

## Định lý Bayes

Cái định lý này rất khô khan, nhàm chán và thực sự cũng không cần thiết để hiểu rõ nhưng mình vẫn sẽ nêu ở đây. Nếu bạn đọc tới lần thứ 3 và vẫn chưa hiểu, tốt nhất là nên bỏ qua.

**Định nghĩa:**
- P(A) = Tỉ lệ xảy ra A
- P(B) = TỈ lệ xảy ra B
- P(A|B) = Tỉ lệ xảy ra A khi biết B đã xảy ra

Lấy ví dụ như này nhé, tỉ lệ nhiễm Covid là 1 người/100 người, tỉ lệ kit test nhanh đưa ra kết quả sai là 10%, như vậy:

**P(Covid) = 1%** << Tỉ lệ nhiễm Covid

**P(noCovid) = 100% - P(Covid) = 99%** << Tỉ lệ không nhiễm Covid

**P(Pos) = P(Pos|Covid) + P(Pos|noCovid) = (1% \* 90%) + (99% \* 10%) = 10.8%** << Tỉ lệ kit test đưa ra kết quả dương tính (Positive)

Như vậy, ta đã biết được 3 tỉ lệ trên. Ta sẽ xét xem nếu bạn nhận được kết quả dương tính, vậy tỉ lệ nhiễm Covid của bạn sẽ tăng lên bao nhiêu nhé. Vẫn là 1% hay là 50%, 100% đây nhỉ?

**P(Covid|Pos) = P(Pos|Covid) / P(Pos) = 90% / 10.8% = 8.333%** << Tỉ lệ nhiễm Covid khi biết kết quả dương tính với Covid

Hay công thức đầy đủ là:

**P(Covid|Pos) = [P(Pos|Covid) \* P(Covid)] / P(Pos)**

**<=> P(A|B) = [P(B|A) \* P(A)] / P(B)**

> Như vậy test ra dương tính cũng không phải buồn nhe, bạn mới chỉ tăng thêm 7.3% khả năng nhiễm Covid thoai :smile:

Đó là cách định lý Bayes đưa ra dự đoán từ dữ liệu đầu vào. Bạn cho biết tỉ lệ nhiễm Covid và độ chính xác của kit test, bạn biết được tỉ lệ nhiễm Covid khi test ra kết quả dương tính và nhiều giá trị khác như **P(noCovid|Pos), P(Covid|Neg), P(noCovid|Neg)**

## Bayes ngây thơ

Vậy Bayes ngây thơ và Bayes không phải là một à? Ừ thì, Thomas Bayes là nhân vật có thật và mình không nghĩ ông ấy "ngây thơ" cho lắm... Naive Bayes là một thuật toán dựa trên định lý Bayes, thứ ngây thơ ở đây là thuật toán xử lý dữ liệu và đưa ra dự đoán. Tại sao lại thế hả? Cùng tìm hiểu nào!

Vì mình khá ghét việc chỉ ghi công thức suông nên sẽ có một ví dụ như sau cho mọi người:

- Linh là một học sinh nghiêm túc, 70% từ ngữ bạn sử dụng liên quan tới chuyện học hành, 20% liên quan tới phim ảnh và 10% để nói tục

- Đức thì không được ngoan cho lắm, 10% từ ngữ bạn sử dụng liên quan tới học tập, 30% phim ảnh và 60% nói bậy.

Truyền hai tham số trên vào thuật toán Naive Bayes và đặt ra câu hỏi:

**Với một câu nói chỉ gồm các từ ngữ liên quan tới vấn đề học tập VÀ phim ảnh, ai là người có khả năng nói ra nó hơn?**

Cùng xét các xác suất nhé. Vì ở đây có 2 người nên tỉ lệ mỗi người nói sẽ nhân thêm với 50%.

1. Xác suất nói ra câu nói ấy của Linh là 70% * 10% * 50% = 3.5% (Công thức xác suất cơ bản)

2. Xác suất nói ra câu tương tự của Đức là 10% * 30% * 50% = 1.5%

Khả năng của Linh nói ra như vậy trong 2 bạn là 3.5 / (1.5 + 3.5) = 70%

Vậy khả năng Linh nói lớn hơn Đức, đó cũng là kết quả thuật toán Naive Bayes sẽ trả lại.

Hiểu được cách nó hoạt động rồi, hãy cùng tìm hiểu lí do tại sao thuật toán "ngây thơ" nào.

Khi bạn đưa cho thuật toán một chuỗi các giá trị đầu vào, nó sẽ kiểm tra các giá trị và tần suất xuất hiện. Thế nhưng lại bỏ qua một điều khá quan trọng. Cùng đoán xem nó là gì nhỉ? Điều này xảy ra bởi cách NB dự đoán xác suất với giả định các dữ kiện độc lập với nhau.

Nói sao cho dễ hiểu nhỉ? Giống như ở ví dụ trên, các từ ngữ được sử dụng không hề tồn tại độc lập. Cũng như từng chữ trong những câu nói của ta hằng ngày, chúng luôn ảnh hưởng đến nhau. Nếu các từ ngữ tồn tại độc lập với nhau như giả định của NB và sắp xếp ngẫu nhiên loạn lên, không tuân theo một trật tự nhất định thì câu nói sẽ chẳng có ý nghĩa gì cả.

**Ví dụ**: Cậu học được gì từ bộ phim Titanic?
=> Titanic cậu được bộ gì học phim từ

 Như vậy, có thể thấy ở một số trường hợp Bayes ngây thơ không phải sự lựa chọn tốt, nhưng cũng có nhiều trường hợp NB lại là một thuật toán vô cùng mạnh mẽ và đơn giản, tiện lợi.
