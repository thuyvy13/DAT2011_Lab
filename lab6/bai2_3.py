"""
Bài 2 (2 điểm) 
Tạo lớp SinhVienPoly gồm 2 thuộc tính họ tên và ngành cùng với phương thức 
trừu tượng là get_diem(). Thêm phương thức get_hoc_luc() để xếp loại học lực. 
Lớp cũng bao gồm một phương thức xuat() để xuất họ tên, ngành, điểm và học 
lực ra màn hình. 
"""

from abc import ABC, abstractmethod

class SinhVienPoly(ABC):
    def __init__(self, ho_ten, nganh):
        self.ho_ten = ho_ten
        self.nganh = nganh
        
    def get_diem(self):
        pass

    def get_hoc_luc(self):
        diem = self.get_diem()
        if diem < 5:
            return "Yếu"
        elif 5 <= diem <= 7:
            return "Trung bình"
        elif 7 <= diem <= 8:
            return "Khá"
        elif 8 <= diem < 9:
            return "Giỏi"
        else:
            return "Xuất sắc"
        
    def xuat(self):
        print(f'Họ tên: {self.ho_ten()}')
        print(f'Ngành: {self.ngành()}')
        print(f'Điểm: {self.diem()}')
        print(f'Học lực: {self.get_hoc_luc()}')
    
    
"""
Bài 3 (2 điểm) 
Tạo lớp SinhVienIT và SinhVienBiz kế thừa từ lớp SinhVienPoly. 
✓ SinhVienIT gồm các thuộc tính điểm java, html, css. Ghi đè phương thức 
get_diem() để tính điểm cho sinh viên IT theo công thức  (2 * java + html + 
css) / 4 
✓ SinhVienBiz gồm các thuộc tính điểm marketing, sales. Ghi đè phương thức 
get_diem() để tính điểm cho sinh viên Biz theo công thức  (2 * marketing + 
sales) / 3 
"""

class SinhVienIT(SinhVienPoly):
    def __init__(self, ho_ten, nganh, diem_java, diem_html, diem_css):
        super().__init__(ho_ten, nganh)
        self.diem_java = diem_java
        self.diem_html = diem_html
        self.diem_css = diem_css
        
    def get_diem(self):
        return (2 * self.diem_java + self.diem_html + self.diem_css) / 4
    
# sv = SinhVienIT("Đỗ Thuỳ Vy", "Xử lý dữ liệu", 10, 10, 10)
# sv.xuat()

class SinhVienBiz(SinhVienPoly):
    def __init__(self, ho_ten, nganh, diem_marketing, diem_sales):
        super().__init__(ho_ten, nganh)
        self.diem_marketing = diem_marketing
        self.diem_sales = diem_sales
        
    def get_diem(self):
        return (2 * self.diem_marketing + self.diem_sales)