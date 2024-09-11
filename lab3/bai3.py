import sys
sys.path.insert(0, 'E:\FALL 2024\DAT201 - Python\DAT109_Exercise\src')
from manager.utils.util import Utils as U
'''
Bài 3 (2 điểm)
Viết chương trình nhập một số nguyên từ bàn phím và cho biết số đó có phải là số
nguyên tố hay không (số nguyên tố là số chỉ chia hết cho 1 và chính nó).
'''

def is_prime(n):
    if n <= 1:
        return False
    
    ok = True
    i = 2
    while i < (n-1):
        if n % i == 0:
            ok = False
            break
        i += 1
    return ok

def main():
    try:
        number = int(input("Nhập vào số nguyên: "))
        if is_prime(number):
            print(f"Số {number} là số nguyên tố")
        else:
            print(f"Số {number} không phải là số nguyên tố")
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên")    
        
if __name__ == "__main__":
    main()
    





















