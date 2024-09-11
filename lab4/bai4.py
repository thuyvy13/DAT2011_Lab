import sys
sys.path.insert(0, 'E:\FALL 2024\DAT201\DAT109_Exercise\src')
from lab.lab4.bai1 import tinh_tien_nuoc_sinh_hoat
from lab.lab4.bai2 import tinh_nguyen_lieu

def menu():
    while True:
        print("+------------------------------+")
        print("| 1. Tính tiền nước sinh hoạt  |")
        print("| 2. Tính nguyên liệu làm bánh |")
        print("| 3. Kết thúc                  |")
        print("+------------------------------+")
        
        try:
            choice = int(input("Chọn chức năng: "))
            print(f"Bạn đã chọn: {choice}")
        except ValueError:
            print("Vui lòng nhập một số từ 1 đến 3")
            continue
    
        if choice == 1:
            san_luong = int(input("Nhập số nước m3 sử dụng: "))
            tien_nuoc = tinh_tien_nuoc_sinh_hoat(san_luong)
            print(f"Tiền nước cho {san_luong} m3 là {tien_nuoc} VNĐ")
            break
        elif choice == 2:
            banh_dau_xanh = int(input("Nhập số lượng bánh đậu xanh: "))
            banh_thap_cam = int(input("Nhập số lượng bánh thập cẩm: "))
            banh_deo = int(input("Nhập số lượng bánh dẻo: "))
            nguyen_lieu = tinh_nguyen_lieu(banh_dau_xanh, banh_thap_cam, banh_deo)
            print(f"Nguyên liệu cần có {nguyen_lieu}")
            break
        elif choice == 3:
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn số từ 1 đến 3.")
            break
if __name__ == "__main__":
    menu()
            