import pandas as pd
import numpy as np
import os
import time
from datetime import datetime

# Config đường dẫn tới tài liệu chứa dữ liệu
# Có thể mình sẽ up luôn folder data lên (Hên xui) bởi vì nó tương đối nặng. Nếu
# tải về các bạn nhớ chỉnh lại path nhe.
path = "../inputData/intraQuarter"

def statsFinder(keyword="Total Debt/Equity (mrq)"):
    statsPath = path + "/_KeyStats"
    # Hàm os.walk() trả về một tuple mang ba giá trị (root, dir, file) trong đường dẫn tham số
    # Bạn có thể print bên dưới để xem kết quả root trả về sẽ nhìn ra sao (trông rối cm)
    statsList = [x[0] for x in os.walk(statsPath)]

    # Không lấy phần tử đầu tiên vì đấy là folder gốc, không dùng tới
    for i in statsList[1:]:
        allFile = os.listdir(i) # Hiển thị tất cả file chứa trong thư mục i
        if len(allFile) > 0: # Lọc những folder không có cái quái gì bên trong
            for file in allFile:
                processed_time = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                # Hàm datetime.strptime hỗ trợ chuyển đổi từ string sang Time Object. Rất tiện
                # Tìm hiểu thêm tại đây: https://www.programiz.com/python-programming/datetime/strptime
                unix_time = time.mktime(processed_time.timetuple())
                # Thời gian UNIX được tính từ 1/1/1970, số thời gian trôi qua sẽ quy đổi sang giây. Hàm này nhận tham số dạng (Year, month, date,...)
                # Hàm timetuple() nhận một Time Object và trả về tuple dạng (Year, month, date,...) phù hợp làm tham só cho time.mktime()

statsFinder()
