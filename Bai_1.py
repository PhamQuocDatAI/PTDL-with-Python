# Câu 1: Hãy tạo 1 đối tượng kiểu Series có tối thiểu 10 phần tử (kiểu số) với giá trị tùy ý thích của bạn.
# In giá trị của Series đó ra màn hình

import pandas as pd
import random 

n = int(input("Nhập giá trị của n: "))
test = []
for item in range(n):
    a = random.randint(-1000, 1000)
    test.append(a)

print(test)
print(pd.Series(test))
print("-" * 100)

# Câu 2: Hãy tạo 1 đối tượng kiểu Series với giá trị khởi tạo hình thành từ dữ liệu kiểu Dictionary. 
# In kết quả ra màn hình

import pandas as pd


dic = {"Trung": 1, "Nam": 2, "Hai": 3, "Thanh": 4, "Ngan": 5, 
       "Mai": 6, "Tam": 7, "Thien":8, "Jack": 9, "Lucifer": 10}

ser = pd.Series(dic)
print(ser)
print("-" * 100)

# Câu 3: Sử dụng series ở câu 1, hãy thay đổi giá trị của cột index 
# từ kiểu số theo kiểu ký tự với giá trị do bạn tự xác định.

series = pd.Series((test), 
                   index = ["A11", "B22", "C33",
                            "D33", "E22", "F11", 
                            "GG22", "Hkdg11", "I77",
                            "J12311", "11", "22", 
                            "33", "77", "1177"]
                  )
print(series)
print("-" * 100)


# Câu 4: Sử dụng series ở câu 2, hãy truy cập đến phần tử thứ 5 và in ra màn hình

print(ser[4])
print("-" * 100)

# Câu 5: Sử dụng series ở câu 3, hãy truy cập đến 1 phần tử dựa theo 
# chỉ số kiểu ký tự do bạn lựa chọn và in ra màn 

print(series["A11"], series["C33"], series["F11"])    
print("-" * 100)

# Câu 6: Sử dụng series ở câu 3, hãy tìm ra tính chất đặc thù trong các chỉ số kiểu kí tự, 
# thực hiện vòng lặp for duyệt trên các chỉ mục kiểu kí tự này để lọc ra 
# những phần tử thỏa mãn điều kiện và in ra màn hình

print(series[[name.endswith("77") or name.startswith("G") for name in series.index]])
print("-" * 100)

# Câu 7: Sử dụng series ở câu 1, hãy đổi tên cột index thành 'STT' 
# và đặt tên cho series là 'Gia_tri'. In kết quả ra màn hình

series.index.name = "STT"
series.name = "Gia_tri"
print(series)
print("-" * 100)

# Câu 8: Hãy áp dụng hàm logarith của gói numpy với series ở câu 1 và in kết quả ra màn hình

import numpy as np


np.log(series)
print("-" * 100)


# Câu 9: Lọc các giá trị của series 1 > 15 và in ra màn hình
print(series[1:15])

