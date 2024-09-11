import sys
sys.path.insert(0, 'E:\FALL 2024\DAT201 - Python\DAT109_Exercise\src')
from manager.utils.util import Utils as U

"""Viết chương trình cho phép giải phương trình bậc nhất trong đó các hệ số a và b 
nhập từ bàn phím."""
a = U.check_number("Nhập hệ số a: ")
b = U.check_number("Nhập hệ số b: ")

if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = round(-b/a, 2) 
    print(f"Phương trình có nghiệm là x = {x}")
    