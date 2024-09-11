import math
import sys
sys.path.insert(0, 'E:\FALL2024\DAT201\DAT109_Exercise\src')
from manager.utils.util import Utils as U

'''
Bài 4:Viết chương trình nhập các hệ số của phương trình bậc 2. Tính delta và xuất căn 
delta ra màn hình.
'''
a = U.check_number("Nhập hệ số a: ")
b = U.check_number("Nhập hệ số b: ")
c = U.check_number("Nhập hệ số c: ")

delta = b * b - 4 * a * c
if delta >= 0:
    sqrt_delta = math.sqrt(delta)
    print(f"Căn delta là {sqrt_delta}")
else:
    print("Phương trình vô nghiệm")

