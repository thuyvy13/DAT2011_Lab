"""
Bài 3 (2 điểm) 
Viết chương trình để tạo ra 1 triệu số nguyên ngẫu nhiên có giá trị trong khoảng 
từ 0 đến 100. Ghi kết quả ra file. 
HƯỚNG DẪN: 
✓ Sử dụng thư viện random để tạo ra các số ngẫu nhiên. 
✓ Mỗi số được cách nhau bởi dấu trống. 
"""

import random

num_count = 1000000
random_number = [str(random.randint(0, 100)) for _ in range(num_count)] # _ : khi không cần dùng đến giá trị của biến vòng lặp
num_string = ' '.join(random_number) #join: kết hợp các phần tử của iterable(randon_number) -> 1 chuỗi & cách nhau bởi dấu cách

file = open('random_numbers.txt', 'w' )
file.write(num_string)