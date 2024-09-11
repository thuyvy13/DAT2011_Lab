"""
Bài 2 (3 điểm) 
Nhập thông tin của một sinh viên, bao gồm họ tên, email, số điện thoại, chứng 
minh nhân dân. Kiểm tra và thông báo lỗi nếu nhập không đúng định dạng email, 
số điện thoại và CMND. 
HƯỚNG DẪN: 
✓ Có thể sử dụng kiểu dữ liệu dictionary để lưu thông tin của 1 sinh viên. 
✓ Kiểm soát dữ liệu nhập vào bằng cách sử dụng biểu thức chính qui (tham 
khảo slide bài giảng) để kiểm tra và thông báo lỗi 
o Email 
o Số điện thoại
o CMND 
"""
import re

def validate_email(email):
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
    if re.match(email_pattern, email): #match kiểm tra 1 chuỗi có khớp với 1 pattern regex không
        return True
    else:
        return False
    
def validate_phone(phone):
    phone_pattern = r'^\d{10}$'
    if re.match(phone_pattern, phone):
        return True
    else:
        return False
    
def validate_cmnd(cmnd):
    cmnd_pattern = r'^\d{9}$'
    if re.match(cmnd_pattern, cmnd):
        return True
    else:
        return False
    
def nhap_thong_tin_sinh_vien():
    sinh_vien = {}
    
    sinh_vien['ho_ten'] = input("Nhập họ tên sinh viên: ")
    
    while True:
        email = input("Nhập email sinh viên: ")
        if validate_email(email):
            sinh_vien['email'] = email
            break
        else: 
            print("Email không hợp lệ, vui lòng nhập lại")
            
    while True:
        phone = input("Nhập số điện thoại (10 số): ")
        if validate_phone(phone):
            sinh_vien['so_dien_thoai'] = phone
            break
        else:
            print("Số điện thoại không hợp lệ, vui lòng nhập lại")
            
    while True:
        cmnd = input("Nhập số CMND (9 số): ")
        if validate_cmnd(cmnd):
            sinh_vien['cmnd'] = cmnd
            break
        else:
            print("Số CMND không hợp lệ, vui lòng nhập lại")
    
    return sinh_vien

sinh_vien = nhap_thong_tin_sinh_vien()
print("Thông tin sinh viên đã nhập: ")
for key, value in sinh_vien.items(): #lặpqua các cặp khoá giá trị trong 1 dic   
    #print(f"{key} : {value}")
    print(f"{key.capitalize()}: {value}") #capitalize: định dạng khoá của dic(vd: ho_ten -> Ho_ten)