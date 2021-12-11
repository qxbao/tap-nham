# Naive Bayes (Bayes ngây thơ)

## Định lý Bayes
Để mình đưa ra ví dụ cho dễ hiểu:

Một bộ kit hỗ trợ test Covid-19 cho bệnh nhân (gọi là bộ K). Tỉ lệ người nhiễm Covid là 1/100 người (tương đương 1%), tỉ lệ bệnh nhân mắc Covid nhưng K báo âm tính là 10%, tỉ lệ bệnh nhân âm tính nhưng K báo dương tính là 10%. Vậy, nếu bạn sử dụng bộ K và được kết quả dương tính, tỉ lệ mắc Covid của bạn bây giờ là bao nhiêu?

> Thật ra không lớn lắm đâu. Chỉ 8,3% thôi

Tại sao lại như vậy? Đọc kỹ các số liệu trên, ta có thể thấy tỉ lệ K đưa ra kết quả dương tính là 1% [thật sự nhiễm Covid] + 9.9% [âm tính nhưng K báo sai] - 0.1% [dương tính nhưng K báo âm tính] = 10.8%. Như vậy, dù đạt được kết quả âm tính, bạn vẫn chỉ có:

> (1 - 0.1)/(10.8) = 0.08333 = ~8.3% tỉ lệ thực sự mắc Covid mà thôi

P\(C\) = 0.1%

<sup><sub>[Tỉ lệ nhiễm Covid] = 1%</sub></sup>

P(C|Dt) = P\(C\) * P\(Dt|C\)

<sup><sub>[Tỉ lệ nhiễm Covid cho ra kết quả dương tính] = [Tỉ lệ nhiễm Covid] * [Tỉ lệ kết quả dương tính nhưng thực sự nhiễm Covid]</sub></sup>
