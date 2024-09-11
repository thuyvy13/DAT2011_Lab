"""
Bài 1 (1 điểm) 
Nhập họ và tên từ bàn phím. Xuất tên, họ và tên đệm ra màn hình trong đó tên và 
họ xuất IN HOA. 
HƯỚNG DẪN: 
✓ Sử dụng hàm split() để chia chuỗi thành các từ 
o Họ là từ đầu tiên 
o Tên là từ cuối cùng 
o Tên đệm là các từ còn lại, có thể không có
"""

def process_name(full_name):
    name_parts = full_name.split()
    print(name_parts)
    last_name = name_parts[0].upper()
    first_name = name_parts[-1].upper()
    middle_name = " ".join(name_parts[1:-1])

    print(f"Họ: {last_name}")
    print(f"Tên đệm: {middle_name}")
    print(f"Tên: {first_name}")

full_name = input("Nhập họ và tên: ")
process_name(full_name)
