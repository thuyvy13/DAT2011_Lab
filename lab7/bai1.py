""" 
Bài 1 (2 điểm) 
Mở file DAT201 - Lab 7 – Resource.txt. 
✓ Đọc toàn bộ nội dung của file và xuất ra màn hình 
✓ Đọc và xuất ra màn hình tên bài thơ (9 ký tự đầu tiên) 
✓ Đọc và xuất ra màn hình tên tác giả (dòng thứ hai) 
"""

file = open("DAT201 - Lab 7 - Resource.txt", "r", encoding= "utf-8")
print(file.read())
print(file.read(9))
print(file.readline.strip())

file.close
