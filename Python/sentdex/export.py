# File này hướng dẫn các bạn cách scrape data từ các file HTML, sau này có thể áp dụng để nhận data từ những nguồn khác. Nên nhớ, machine learning đưa ra kết quả như nào phụ thuộc hầu hết vào data đầu vào

import pandas as pd
import numpy as np
import os
import time
from matplotlib import style
import matplotlib.pyplot as plt
from datetime import datetime
import re

style.use("dark_background")

# Config đường dẫn tới tài liệu chứa dữ liệu
# Có thể mình sẽ up luôn folder data lên (Hên xui) bởi vì nó tương đối nặng. Nếu
# tải về các bạn nhớ chỉnh lại path nhe.
path = "../inputData/intraQuarter"

def statsFinder(keyword="Total Debt/Equity (mrq):",bonus='</td><td class="yfnc_tabledata1">'):
    statsPath = path + "/_KeyStats"
    pf = pd.DataFrame(columns=['Thời gian','UNIX','Code','Nợ/vốn',"Giá","Stockchange","SP500","SP500change","Diff"])

    sp = pd.read_csv('../../csv/fedSP500.csv')
    # Có thể mình sẽ up file này lên (đã qua xử lý) để mọi người đỡ một bước đi kiếm data
    # rồi lại ngồi reformat rất cực.

    # Hàm os.walk() trả về một tuple mang ba giá trị (root, dir, file) trong đường dẫn tham số
    # Bạn có thể print bên dưới để xem kết quả root trả về sẽ nhìn ra sao (trông rối cm)
    statsList = [x[0] for x in os.walk(statsPath)]

    code_list=[]

    # Không lấy phần tử đầu tiên vì đấy là folder gốc, không dùng tới
    for dir in statsList[1:]:
        allFile = os.listdir(dir) # Hiển thị tất cả file chứa trong thư mục i
        print(dir)
        # Giá trị khởi đầu
        gtkd = False
        gtkd_SP500 = False

        code = dir.split('\\')[1]
        # .split(x) sẽ chia một chuỗi thành một list gồm các phần tử được chia cách bằng dấu space (nếu không truyền x) hoặc x.
        code_list.append(code)

        if len(allFile) > 0: # Lọc những folder không có cái quái gì bên trong
            for file in allFile:
                processed_time = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                # Hàm datetime.strptime() hỗ trợ chuyển đổi từ string sang Time Object. Rất tiện
                # Tìm hiểu thêm tại đây: https://www.programiz.com/python-programming/datetime/strptime

                unix_time = time.mktime(processed_time.timetuple())
                # Thời gian UNIX được tính từ 1/1/1970, số thời gian trôi qua sẽ quy đổi sang giây. Hàm này nhận tham số dạng (Year, month, date,...)
                # Hàm timetuple() nhận một Time Object và trả về tuple dạng (Year, month, date,...) phù hợp làm tham số cho time.mktime()

                filePath = dir + '/' + file # Tạo đường dẫn tới từng file trong vòng lặp

                sourceCode = open(filePath,'r').read()
                # open() là hàm mở file xem nội dung, tham số 'r' chỉ yêu cầu 'read' (Nếu không hiểu thì chịu đấy)
                # Vì sourcecode HTML bung ra rất loằng ngoằng nên mình khuyến khích nếu bạn muốn print có thể thêm hàm
                # time.sleep(60) đằng sau để tạm ngừng 60 giây giữa mỗi lần print thay vì print hết sạch (cho dễ quan sát)

                try:
                    value = -444
                    try:
                        value = float(sourceCode.split(keyword+bonus)[1].split('</td>')[0])
                    except Exception as e:
                        value = float(sourceCode.split(keyword+'</td>\n<td class="yfnc_tabledata1">')[1].split('</td>')[0])
                    # Ép biến value sang float để lưu trữ
                    # Việc split sourcecode liên tục để có thể chọn được giá trị cần thiết

                    sp500_time = datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')
                    # Lấy thời gian từ folder data -> Đem so sánh và tìm ra cột tương ứng trong file CSV SP500
                    row = sp[(sp['Ngày'] == sp500_time)]

                    try:
                        sp500_value = float(row["Lần cuối"])
                        # Thử ép biến {giá trị cổ phiếu cuối phiên}. Nếu biến rỗng <=> Ngày {sp500_time} không
                        # tồn tại trong file CSV 500P, lùi 3 ngày (Tránh những ngày nghỉ lễ, thứ bảy chủ nhật ctct)
                    except:
                        sp500_time = datetime.fromtimestamp(unix_time-259200).strftime('%Y-%m-%d')
                        # Lùi thời gian đi 3 ngày (259200 là số giây của 3 ngày trong hệ UNIXtime)
                        row = sp[(sp['Ngày'] == sp500_time)]
                        sp500_value = float(row["Lần cuối"])
                    stock_price = False
                    try:
                        stock_price = float(sourceCode.split("</small><big><b>")[1].split('</b></big>')[0])
                        # Tìm kiếm giá trị cổ phiếu tương ứng trong từng file
                    except:
                        try:
                            stock_price = (sourceCode.split("</small><big><b>")[1].split('</b></big>')[0])
                            stock_price = float(re.search(r'(\d{1,8}\.\d{1,8})',stock_price).group(1))
                            # Regex

                        except:
                            try:
                                stock_price = sourceCode.split('<p> <span class="time_rtq_ticker">')[1].split('</span>')[0]
                                stock_price = float(re.search(r'(\d{1,8}\.\d{1,8})',stock_price).group(1))
                            except:
                                pass
                    if not gtkd:
                        gtkd = stock_price
                    if not gtkd_SP500:
                        gtkd_SP500 = sp500_value
                    # Nếu biến giá trị khởi đầu chưa được khởi tạo => gán price vào

                    # Hiển thị số phần trăm tăng/giảm so với phiên trước
                    # print(file)
                    if stock_price and value != -44:
                        stock_change = (stock_price - gtkd)/gtkd*100
                        sp500change = (sp500_value-gtkd_SP500)/gtkd_SP500*100
                        # Thêm một row vào data
                        pf = pf.append({'Thời gian':processed_time,
                                'UNIX':unix_time,
                                'Code':code,
                                'Nợ/vốn':value,
                                'Stockchange':stock_change,
                                'Giá':stock_price,
                                'SP500change': sp500change,
                                'SP500':sp500_value,
                                'Diff':stock_change - sp500change
                                }, ignore_index=True)
                    else:
                        pass
                    # Thêm giá trị vào DataFrame
                    # Mình bị một lỗi rất ngớ ngẩn ở đây là quên viết "pf = pf.append()" mà chỉ viết "pf.append" thôi
                    # nên đến cuối cùng cái file CSV trống trơn :v Nhớ nhé, hàm .append() này return lại một bản copy
                    # thôi nên phải khai báo giá trị cho nó.

                except Exception as e:
                    pass
                # Try...except... này các bạn nên tự tìm hiểu thêm. Đại khái là nếu cụm Try xảy ra lỗi thì chạy cụm Except.
                # Còn nếu thành công thì chạy tiếp cụm else hoặc chạy tiếp nếu k có else
    print("DONE!")
    # for ticker in code_list:
    #     try:
    #         print('Check')
    #         code_row = pf[(pf['Code']==ticker)].set_index(["Thời gian"])
    #         code_row['Diff'].plot(label=ticker)
    #         plt.legend()
    #     except Exception as e:
    #         print(str(e))
    #         pass
    # print('Done 2')
    # plt.show()

    saveName = keyword;
    for key in [' ',':','(',')','/']:
        saveName = saveName.replace(key,'')
    saveName = saveName + '.csv'
    # Tạo tên savefile từ tham số keyword. Hàm .replace(x,y) chỉ đơn giản thay x bằng y thôi.
    # Nếu có thể nhớ tìm hiểu RegEx nha. Không chỉ tiện mà còn siêu tiện luôn đó

    pf.to_csv('../../csv/'+saveName)
    # Lưu thông tin về file CSV (Tùy chỉnh path). Chạy code sẽ khá lâu đó (i5 ~ 7p, i7 ~ 1p) nên đừng tắt giữa chừng nha

# statsFinder()
#   ^^^^^^^----------- Mình ẩn cái hàm này đi vì nó chỉ cần thiết cho lần lưu trữ đầu tiên thôi. Lưu xong file rồi mà lỡ
#                      chạy thì nó ngốn CPU lắm :p Các bạn cứ uncomment rồi chạy nếu muốn xuất file CSV nhé.
