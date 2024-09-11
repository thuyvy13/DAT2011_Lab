"""
Bài 4 (2 điểm) 
Viết chương trình quản lý sinh viên: 
1. Nhập danh sách sinh viên 
2. Xuất thông tin danh sách sinh viên 
3. Xuất danh sách sinh viên có học lực giỏi 
4. Sắp xếp danh sách sinh viên theo điểm 
5. Kết thúc 
"""

import sys
sys.path.insert(0, 'E:\FALL2024\DAT201\DAT109_Exercise\src')
from lab.lab6.bai2_3 import SinhVienIT, SinhVienBiz

def nhap_danh_sach_sinh_vien():
    danh_sach = []
    while True:
        loai_sv = input("Nhập loại sinh viên (1: IT, 2: Biz, 0: Dừng): ")
        
        if loai_sv == '0':
            break
        
        ho_ten = input("Nhập tên: ")
        nganh = input("Nhập ngành: ")
        if loai_sv == '1':
            diem_java = float(input("Nhập điểm Java: "))
            diem_html = float(input("Nhập điểm html: "))
            diem_css = float(input("Nhập điểm css: "))
            sv = SinhVienIT(ho_ten, nganh, diem_java, diem_html, diem_css)
        
        elif loai_sv == '2':
            diem_marketing = float(input("Nhập điểm Marketing: "))
            diem_sales = float(input("Nhập điểm Sales: "))
            sv = SinhVienBiz(ho_ten, nganh, diem_marketing, diem_sales)
            
        danh_sach.append(sv)
    return danh_sach

def xuat_danh_sach_sinh_vien(danh_sach):
    for sv in danh_sach:
        sv.xuat()
        print()
        
def xuat_sinh_vien_gioi(danh_sach):
    print("Danh sách sinh viên giỏi: ")
    for sv in danh_sach:
        if sv.get_hoc_luc() == 'Giỏi':
            sv.xuat()
            print()
            
def sap_xep_sinh_vien_theo_diem(danh_sach):
    danh_sach.sort(key=lambda sv: sv.get_diem(), reverse = True)
    print("Danh sách sinh viên sau khu sắp xếp theo điểm: ")
    xuat_danh_sach_sinh_vien(danh_sach)
    
def main():
    danh_sach = []
    while True:
        print("1. Nhập danh sách sinh viên")
        print("2. Xuất danh sách sinh viên")
        print("3. Xuất danh sách sinh viên có học lực giỏi")
        print("4. Sắp xếp danh sách sinh viên theo điểm")
        print("5. Kết thúc")
        choice = input("Chọn chức năng: ")
        
        if choice == '1':
            danh_sach = nhap_danh_sach_sinh_vien()
        elif choice == '2':
            xuat_danh_sach_sinh_vien(danh_sach)
        elif choice == '3':
            xuat_sinh_vien_gioi(danh_sach)
        elif choice == '4':
            sap_xep_sinh_vien_theo_diem(danh_sach)
        elif choice == '5':
            print("Kết thúc")
            break
        else:
            print("Chức năng không hợp lệ, vui lòng chọn lại")

if __name__ == "__main__":
    main()