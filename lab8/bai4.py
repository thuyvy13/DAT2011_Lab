"""
Bài 4 (2 điểm) 
Đọc file dữ liệu được tạo trong bài 3. Sử dụng thư viện statistics để tính các giá trị 
sau: 
✓ Trung bình của bộ dữ liệu (mean hay average) 
✓ Tính toán độ lệch chuẩn (standard deviation) 
YÊU CẦU NÂNG CAO (KHÔNG BẮT BUỘC) 
✓ Sử dụng iterator để làm việc với số lớn
"""

import statistics

file = open('random_numbers.txt', 'r')
data = (int(num) for num in file.read().split())

mean_value = statistics.mean(data)

file = open('random_numbers.txt', 'r') #đọc lại iterator vì iterator chỉ duyệt 1 lần
data = (int(num) for num in file.read().split())

std_dev_value = statistics.stdev(data)

print(f"Trng bình của bộ dữ liệu: {mean_value}")
print(f"Độ lệch chuẩn của bộ dữ liệu: {std_dev_value}")