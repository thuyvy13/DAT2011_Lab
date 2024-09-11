import sys
sys.path.insert(0, 'E:\FALL2024\DAT201\DAT109_Exercise\src')
from manager.utils.util import Utils as U
"""
Bài 2:Viết chương trình nhập từ bàn phím 2 cạnh của hình chữ nhật. Tính và xuất ra 
màn hình chu vi và diện tích của hình chữ nhật.
"""     

# number_first = U.check_dimensions("Nhập vào chiều dài: ")
# number_second = U.check_dimensions("Nhập vào chiều rộng: ")
number_first, number_second = U.check_dimensions("Nhập vào chiều dài: ", "Nhập vào chiều rộng: ")
chuVi = (number_first + number_second) * 2
dienTich = number_first * number_second
print(f"Chu vi hình chữ nhật là {chuVi}")
print(f"Diện tích hình chữ nhật là {dienTich}")