import math
import sys
sys.path.insert(0, 'E:\FALL 2024\DAT201 - Python\DAT109_Exercise\src')
from manager.utils.util import Utils as U

"""Viết chương trình cho phép giải phương trình bậc hai trong đó các hệ số a, b và c 
nhập từ bàn phím."""
a = U.check_number("Nhập hệ số a: ")
b = U.check_number("Nhập hệ số b: ")
c = U.check_number("Nhập hệ số c: ")

if a == 0 :
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = round(-c/b, 2)
        print(f"Phương trình bậc nhất có nghiệm là x = {x}")
        
else:
    delta = b**2 - 4*a*c
    
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = round(-b/(2*a), 2)
        print(f"Phương trình có nghiệm kép là x = {x}")
    else:
        x1 = round((-b + math.sqrt(delta)) / (2*a), 2)
        x2 = round((-b - math.sqrt(delta)) / (2*a), 2)
        print(f"Phương trình có 2 nghiệm phan biệt là x1 = {x1}, x2 = {x2}")
        
        
    
