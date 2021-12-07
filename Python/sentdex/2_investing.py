import pandas as pd
import numpy as np
import os
import time
from datetime import datetime

# Config đường dẫn tới tài liệu chứa dữ liệu
# Có thể mình sẽ up luôn folder data lên (Hên xui) bởi vì nó tương đối nặng. Nếu
# tải về các bạn nhớ chỉnh lại path nhe.
path = "../inputData/intraQuarter"

def statsFinder(keyword="Total Debt/Equity (mrq):",bonus='</td><td class=\"yfnc_tabledata1\">'):
    statsPath = path + "/_KeyStats"
    pf = pd.DataFrame(columns=['Thời gian','UNIX','Code','Nợ/vốn'])
    # Hàm os.walk() trả về một tuple mang ba giá trị (root, dir, file) trong đường dẫn tham số
    # Bạn có thể print bên dưới để xem kết quả root trả về sẽ nhìn ra sao (trông rối cm)
    statsList = [x[0] for x in os.walk(statsPath)]

    # Không lấy phần tử đầu tiên vì đấy là folder gốc, không dùng tới
    for dir in statsList[1:]:
        allFile = os.listdir(dir) # Hiển thị tất cả file chứa trong thư mục i
        code = dir.split('\\')[1]
        # .split(x) sẽ chia một chuỗi thành một list gồm các phần tử được chia cách bằng dấu space (nếu không truyền x) hoặc x.


        if len(allFile) > 0: # Lọc những folder không có cái quái gì bên trong
            for file in allFile:
                processed_time = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                # Hàm datetime.strptime() hỗ trợ chuyển đổi từ string sang Time Object. Rất tiện
                # Tìm hiểu thêm tại đây: https://www.programiz.com/python-programming/datetime/strptime

                unix_time = time.mktime(processed_time.timetuple())
                # Thời gian UNIX được tính từ 1/1/1970, số thời gian trôi qua sẽ quy đổi sang giây. Hàm này nhận tham số dạng (Year, month, date,...)
                # Hàm timetuple() nhận một Time Object và trả về tuple dạng (Year, month, date,...) phù hợp làm tham só cho time.mktime()

                filePath = dir + '/' + file # Tạo đường dẫn tới từng file trong vòng lặp

                sourceCode = open(filePath,'r').read()
                # open() là hàm mở file xem nội dung, tham số 'r' chỉ yêu cầu 'read' (Nếu không hiểu thì chịu đấy)
                # Vì sourcecode HTML bung ra rất loằng ngoằng nên mình khuyến khích nếu bạn muốn print có thể thêm hàm
                # time.sleep(60) đằng sau để tạm ngừng 60 giây giữa mỗi lần print thay vì print hết sạch (cho dễ quan sát)

                try:
                    value = float(sourceCode.split(keyword+bonus)[1].split('</td>')[0])
                    # Ép biến value sang float để lưu trữ
                    # Việc split sourcecode liên tục để có thể chọn được giá trị cần thiết

                    pf = pf.append({'Thời gian':processed_time,'UNIX':unix_time,'Code':code,'Nợ/vốn':value}, ignore_index=True)
                    # Thêm giá trị vào DataFrame
                    # Mình bị một lỗi rất ngớ ngẩn ở đây là quên viết "pf = pf.append()" mà chỉ viết "pf.append" thôi
                    # nên đến cuối cùng cái file CSV trống trơn :v Nhớ nhé, hàm .append() này return lại một bản copy
                    # thôi nên phải khai báo giá trị cho nó.

                except Exception as e:
                    print(e)
                    pass
                # Try...except... này các bạn nên tự tìm hiểu thêm. Đại khái là nếu cụm Try xảy ra lỗi thì chạy cụm Except.

    saveName = keyword;
    for key in [' ',':','(',')','/']:
        saveName = saveName.replace(key,'')
    saveName = saveName + '.csv'
    # Tạo tên savefile từ tham số keyword. Hàm .replace(x,y) chỉ đơn giản thay x bằng y thôi.
    # À nhân tiện nếu có thể nhớ tìm hiểu RegEx nha. Không chỉ tiện mà còn siêu tiện luôn đó

    pf.to_csv(saveName)
    # Lưu thông tin về file CSV. Chạy code sẽ khá lâu đó (i5 ~ 7p, i7 ~ 1p) nên đừng tắt giữa chừng nha

# statsFinder()
#   ^^^^^^^----------- Mình ẩn cái hàm này đi vì nó chỉ cần thiết cho lần lưu trữ đầu tiên thôi. Lưu xong file rồi mà lỡ
#                      chạy thì nó ngốn CPU lắm :p Các bạn cứ uncomment rồi chạy nếu muốn xuất file CSV nhé.
