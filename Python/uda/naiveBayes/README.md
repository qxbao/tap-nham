# Naive Bayes (Bayes ngây thơ)

## Định lý Bayes

Cái định lý này rất khô khan, nhàm chán và thực sự cũng không cần thiết để hiểu rõ nhưng mình vẫn sẽ nêu ở đây. Nếu bạn đọc tới lần thứ 3 và vẫn chưa hiểu, tốt nhất là nên bỏ qua.

**Định nghĩa:**
- P(A) = Tỉ lệ xảy ra A
- P(B) = TỈ lệ xảy ra B
- P(A|B) = Tỉ lệ xảy ra A khi biết B đã xảy ra

Lấy ví dụ như này nhé, tỉ lệ nhiễm Covid là 1 người/100 người, tỉ lệ kit test nhanh đưa ra kết quả sai là 10%, như vậy:

**P(Covid) = 1%** Tỉ lệ nhiễm Covid

**P(noCovid) = 100% - P(Covid) = 99%** Tỉ lệ không nhiễm Covid

**P(Pos) = P(Pos|Covid) + P(Pos|noCovid) = (1% \* 90%) + (99% \* 10%) = 10.8%** Tỉ lệ kit test đưa ra kết quả âm tính

Như vậy, ta đã biết được 3 tỉ lệ trên. Ta sẽ xét xem nếu bạn nhận được kết quả dương tính, vậy tỉ lệ nhiễm Covid của bạn sẽ tăng lên bao nhiêu nhé. Vẫn là 1% hay là 50%, 100% đây nhỉ?

**P(Covid|Pos) = P(Pos|Covid) / P(Pos) = 90% / 10.8% = 8.333%** Tỉ lệ nhiễm Covid khi biết kết quả dương tính với Covid

Hay công thức đầy đủ là:

**P(Covid|Pos) = [P(Pos|Covid) \* P(Covid)] / P(Pos)**

**<=> P(A|B) = [P(B|A) \* P(A)] / P(B)**

Như vậy test ra dương tính cũng không phải buồn nhe, bạn mới chỉ tăng thêm 7.3% khả năng nhiễm Covid thoai :smile:

Đó là cách định lý Bayes đưa ra dự đoán từ dữ liệu đầu vào. Bạn cho biết tỉ lệ nhiễm Covid và độ chính xác của kit test, bạn biết được tỉ lệ nhiễm Covid khi test ra kết quả dương tính và nhiều giá trị khác như **P(noCovid|Pos), P(Covid|Neg), P(noCovid|Neg)**

## Naive Bayes (Bayes ngây thơ)
