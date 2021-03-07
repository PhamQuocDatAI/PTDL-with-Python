# Cho bảng tính đính kèm, hãy:
# 1) Lưu lại thành định dạng csv
# 2) Dùng pandas đọc file csv trên vào bộ nhớ
# 3) Hãy chọn ra ngẫu nhiên 7 sinh viên trong danh sách
# Kết quả lưu vào 1 file csv khác. Code và file csv đẩy lên github và gửi link vào phần trả lời bài tập.

import pandas as pd

data = pd.read_csv("C:\\Users\\PC\\Desktop\\demo.csv", 'rt')
print(data)
print("-" * 50)
data2 = data.sample(7)
print(data2)
data2.to_csv('file.csv')