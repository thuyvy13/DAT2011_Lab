"""
Bài 3
Nâng cấp lớp SanPham bằng cách khai báo các trường dữ liệu với đặc tả truy xuất 
là private để hạn chế truy xuất trực tiếp đến các trường này sau đó bổ sung các 
phương thức getter và setter để đọc ghi dữ liệu các trường.
"""

class SanPham:
    def __init__(self, ten=None, gia=None, giam_gia=None):
        self.__ten = ten
        self.__gia = gia
        self.__giam_gia = giam_gia
    
    def get_ten(self):
        return self.__ten
    
    def set_ten(self, ten):
        self.__ten = ten
    
    def get_gia(self):
        return self.__gia
    
    def set_gia(self, gia):
        if gia > 0:
            self.__gia = gia
        else:
            raise ValueError("Giá phải lớn hơn 0.")
    
    def get_giam_gia(self):
        return self.__giam_gia
    
    def set_giam_gia(self, giam_gia):
        if giam_gia >= 0:
            self.__giam_gia = giam_gia
        else:
            raise ValueError("Giảm giá không được nhỏ hơn 0.")
    
    def tinh_thue_nhap_khau(self):
        return self.__gia * 0.1
    
    def xuat_thong_tin(self):
        print(f"Tên sản phẩm: {self.get_ten()}")
        print(f"Đơn giá: {self.get_gia()} VND")
        print(f"Giảm giá: {self.get_giam_gia()} VND")
        print(f"Thuế nhập khẩu: {self.tinh_thue_nhap_khau()} VND")


