"""
Bài 1 (2 điểm) 
Xây dựng lớp ChuNhat gồm 2 thuộc tính là rong và dai và các phương thức 
get_chu_vi() và get_dien_tich() để tính chu vi và diện tích. Phương thức xuat() sẽ 
xuất ra màn hình chiều rộng, chiều dài, diện tích và chu vi.  
Xây dựng lớp Vuong kế thừa từ lớp ChuNhat và ghi đè phương thức xuat() để xuất 
thông tin cạnh, diện tích và chu vi. 
Viết chương trình nhập 2 hình chữ nhật và một hình vuông sau đó xuất ra màn 
hình. 
"""
import sys
sys.path.insert(0, 'E:\FALL2024\DAT201\DAT109_Exercise\src')
from manager.utils.util import Utils as U

class ChuNhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
    
    def get_chu_vi(self):
        return 2 * (self.dai + self.rong)
        
    def get_dien_tich(self):
        return self.dai * self.rong
        
    def xuat(self):
        print(f'Chiều dài: {self.dai}, Chiều rộng: {self.rong}')
        print(f'Chu vi: {self.get_chu_vi()}, Diện tích: {self.get_dien_tich()}')
            
class Vuong(ChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)
        
    def xuat(self):
        print(f'Cạnh: {self.dai}')
        print(f'Chu vi: {self.get_chu_vi()}, Diện tích: {self.get_dien_tich()}')
    
print("Nhập thông tin hình chữ nhật thứ nhất:")
dai1 = U.check_number("Nhập chiều dài: ")
rong1 = U.check_number("Nhập chiều rộng: ")
hcn1 = ChuNhat(dai1, rong1)

print("Nhập thông tin hình chữ nhật thứ hai:")
dai2 = U.check_number("Nhập chiều dài: ")
rong2 = U.check_number("Nhập chiều rộng: ")
hcn2 = ChuNhat(dai2, rong2)

print("Nhập thông tin hình vuông:")
canh = U.check_number("Nhập cạnh: ")
hv = Vuong(canh)

print("Thông tin hình chữ nhật thứ nhất:")
hcn1.xuat()
print("Thông tin hình chữ nhật thứ hai:")
hcn2.xuat()
print("Thông tin hình vuông:")
hv.xuat()

    