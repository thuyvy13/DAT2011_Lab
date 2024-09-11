import sys
sys.path.insert(0, 'E:\FALL2024\DAT201\DAT109_Exercise\src')
from manager.utils.util import Utils as U
my_list = U.check_integer_list("Nhập vào dãy số nguyên, cách nhau bằng dấu cách(hoặc 's' để dừng): ")
new_list = list(filter(lambda x: (x % 2 == 0), my_list))
print(f"Các số chẫn trong dãy số là {new_list}")