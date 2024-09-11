"""
Bài 4 (2 điểm) 
Nâng cấp lớp SanPham, bổ sung hàm khởi tạo gồm 3 tham số là tên, giá và giảm 
giá. Viết chương trình nhập vào thông tin của 2 sản phẩm, sử dụng hàm khởi tạo 
để gán giá trị cho các thuộc tính của sản phẩm. Xuất thông tin của các sản phẩm 
ra màn hình, sử dụng hàm xuat() có trong bài 1.
"""
class SanPham:
    def __init__(self, ten, gia, giam_gia):
        self.__ten = ten
        self.__gia = gia
        self.__giam_gia = giam_gia
    
    

    def tinh_thue_nhap_khau(self):
        return self.__gia * 0.1
    
    def xuat_thong_tin(self):
        print(f"Tên sản phẩm: {self.get_ten()}")
        print(f"Đơn giá: {self.get_gia()} VND")
        print(f"Giảm giá: {self.get_giam_gia()} VND")
        print(f"Thuế nhập khẩu: {self.tinh_thue_nhap_khau()} VND")
        
        
ten_sp1 = input("Nhập tên sản phẩm 1: ")
gia_sp1 = float(input("Nhập giá sản phẩm 1: "))
giam_gia_sp1 = float(input("Nhập giảm giá sản phẩm 1: "))

sp1 = SanPham(ten_sp1, gia_sp1, giam_gia_sp1)

ten_sp2 = input("Nhập tên sản phẩm 2: ")
gia_sp2 = float(input("Nhập giá sản phẩm 2: "))
giam_gia_sp2 = float(input("Nhập giảm giá sản phẩm 2: "))

sp2 = SanPham(ten_sp2, gia_sp2, giam_gia_sp2)

print("\nThông tin sản phẩm 1:")
sp1.xuat_thong_tin()

print("\nThông tin sản phẩm 2:")
sp2.xuat_thong_tin()

