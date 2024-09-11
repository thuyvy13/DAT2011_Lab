"""
Bài 1
Tạo lớp SanPham gồm 3 thuộc tính là tên, giá và giảm giá. Lớp cũng gồm 2 
phương thức là tính thuế nhập khẩu (10% giá sản phẩm) và xuất thông tin ra màn 
hình. Thông tin xuất ra màn hình gồm: 
✓ Tên sản phẩm 
✓ Đơn giá 
✓ Giảm giá 
✓ Thuế nhập khẩu 
"""
import copy

class SanPham:
    def __init__(self, ten = None, gia = None, giam_gia = None):
        self.ten = ten
        self.gia = gia
        self.giam_gia = giam_gia
        
    def nhap(self):
        self.ten = input("Nhập tên sản phẩm: ")
        self.gia = float(input("Nhập giá sản phẩm: "))
        self.giam_gia = float(input("Nhập giảm giá: "))
    
    def tinh_thue_nhap_khau(self):
        return self.gia * 0.1
    
    def xuat_thong_tin(self):
        print(f"Tên sản phẩm: {self.ten}")
        print(f"Đơn giá: {self.gia} VND")
        print(f"Giảm giá: {self.giam_gia} VND")
        print(f"Thuế nhập khẩu: {self.tinh_thue_nhap_khau()} VND")
            
sanpham = SanPham("Laptop", 24000000, 500000)
# sanpham.xuat_thong_tiN
sanpham1= sanpham.copy(SanPham("abc"))
ten = sanpham.ten
gia = sanpham.gia
print(sanpham1)
print(gia)

