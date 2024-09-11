"""
Bài 2
Viết chương trình nhập thông tin của 2 sản phẩm từ bàn phím, sau đó gọi phương 
thức xuất để xuất thông tin 2 đối tượng sản phẩm đã tạo. 
"""
import sys
sys.path.insert(0, 'E:\FALL2024\DAT201\DAT109_Exercise\src')
from lab.lab5.bai1 import SanPham

sp1 = SanPham()
sp2 = SanPham()

print("Nhập thông tin cho sản phẩm 1: ")
sp1.nhap()
print("Nhập thông tin cho sản phẩm 2: ")
sp2.nhap()

print("Thông tin sản phẩm 1: ")
sp1.xuat_thong_tin()
print("Thông tin sản phẩm 2: ")
sp2.xuat_thong_tin()