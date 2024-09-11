import sys
sys.path.insert(0, 'E:\FALL2024\DAT201\DAT109_Exercise\src')
from manager.utils.util import Utils as U
"""
Bài 2 (2 điểm)
Viết chương trình nhập dữ liệu của một sinh viên. Thông tin của sinh viên bao 
gồm: họ tên và điểm.
✓ Xuất dữ liệu đã nhập, bổ sung thêm thông tin về xếp loại
o Yếu: điểm < 5
o Trung bình: 5 <= điểm < 7
o Khá: 7 <= điểm < 8
o Giỏi: 8 <= điểm < 9
o Xuất sắc: điểm >= 9
HƯỚNG DẪN
✓ Sử dụng dữ liệu kiểu dictionary (từ điển) để lưu thông tin của sinh viên
✓ Sử dụng lệnh if để xét học lực sau đó xuất thông tin của sinh viên
o Họ tên:
o Điểm:
o Xếp loại:
"""


information_student = {} #tạo từ điểm rỗng lưu trữ thông tin sinh viên
#nhập dữ liệu sinh viên
information_student['Họ tên'] = input("Nhập họ tên của sinh viên: ")
information_student['Điểm'] = U.check_number("Nhập điểm của sinh viên: ")
#xếp loại theo điểm của sinh viên
if information_student['Điểm'] < 5:
    information_student['Xếp loại'] = 'Yếu'
elif 5 <= information_student['Điểm'] < 7:
    information_student['Xếp loại'] = 'Trung bình'
elif 7 <= information_student['Điểm'] < 8:
    information_student['Xếp loại'] = 'Khá'
elif 8 <= information_student['Điểm'] < 9:
    information_student['Xếp loại'] = 'Giỏi'
else:
    information_student['Xếp loại'] = 'Xuất sắc'
#output
print("\nThông tin sinh viên:")
print("Họ tên:", information_student['Họ tên'])
print("Điểm:", information_student['Điểm'])
print("Xếp loại:", information_student['Xếp loại'])



"""
CÁC YÊU CẦU NÂNG CAO (KHÔNG BẮT BUỘC)
✓ Sử dụng kiểu list để lưu danh sách sinh viên
✓ Nhập vào thông tin của một vài sinh viên
✓ Xuất thông tin của sinh viên ra màn hình, có thêm thông tin xếp loại
"""
student = [] #tạo list rỗng lưu trữ thông tin sinh viên
#số lượng sinh viên nhập vào
num_students = int(input("Nhập số lượng sinh viên: "))

for i in range(num_students):
    #nhập dữ liệu sinh viên
    print(f"\nNhập thông tin của sinh viên thứ {i + 1}: ")
    information_student = {}
    information_student['Họ tên'] = input("Nhập họ tên của sinh viên: ")
    information_student['Điểm'] = U.check_number("Nhập điểm của sinh viên: ")
    #xếp loại theo điểm của sinh viên
    if information_student['Điểm'] < 5:
        information_student['Xếp loại'] = 'Yếu'
    elif 5 <= information_student['Điểm'] < 7:
        information_student['Xếp loại'] = 'Trung bình'
    elif 7 <= information_student['Điểm'] < 8:
        information_student['Xếp loại'] = 'Khá'
    elif 8 <= information_student['Điểm'] < 9:
        information_student['Xếp loại'] = 'Giỏi'
    else:
        information_student['Xếp loại'] = 'Xuất sắc'
    
    student.append(information_student)
    
# Output
print("\nThông tin sinh viên:")
for index, information_student in enumerate(student, start=1): #enumerate trả về một tuple gồm hai giá trị: chỉ số hiện tại (index) và phần tử từ danh sách (information_student).
    print(f"\nThông tin sinh viên thứ {index}:")
    print("Họ tên:", information_student['Họ tên'])
    print("Điểm:", information_student['Điểm'])
    print("Xếp loại:", information_student['Xếp loại'])
