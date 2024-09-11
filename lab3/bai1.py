"""
Bài 1: (2 điểm)
Viết chương trình thực hiện các thao tác sau với một dãy số nguyên.
✓ Sắp xếp theo thứ tự tăng dần và xuất dãy số nguyên ra màn hình.
✓ Xuất phần tử có giá trị nhỏ nhất ra màn hình
✓ Tính và xuất ra màn hình trung bình cộng các phần tử chia hết cho 3
"""

# numbers_list = [3, 5, 77, 13, 90, 15, 23, 27, 30, 9, 21]
# sort_number = sorted(numbers_list)
# print(sort_number)
# print(numbers_list[0])

# sum = 0
# count = 0
# for i in sort_number:
#     if i % 3 == 0:
#         sum += i
#         count+=1
#     else :
#         continue
    
# if count > 0:
#     average = sum / count
#     print(round(average, 2))
# else:
#     print("Không có số chia hết cho 3.")
   

numbers_list = [3, 5, 77, 13, 90, 15, 23, 27, 30, 9, 21]
# Sắp xếp theo thứ tự tăng dần và xuất dãy số nguyên ra màn hình
numbers_list.sort(reverse=False)
print("Dãy số theo thứ tự tăng dần:", numbers_list)
#Xuất phần tử có giá trị nhỏ nhất ra màn hình
min_value = min(numbers_list)
print("Phần tử có giá trị nhỏ nhất là:", min_value)
#Tính và xuất ra màn hình trung bình cộng các phần tử chia hết cho 3
divisible_by_3 = [number for number in numbers_list if number % 3 == 0]
sum_divisible_by_3 = sum(divisible_by_3)
count_divisible_by_3 = len(divisible_by_3)

if count_divisible_by_3 > 0:
    average = round(sum_divisible_by_3 / count_divisible_by_3, 2)
    print("Trung bình cộng các phần tử chia hết cho 3 là:", average)
else:
    print("Không có phần tử chia hết cho 3")



"""
CÁC YÊU CẦU NÂNG CAO (KHÔNG BẮT BUỘC)
✓ Thay đổi sắp xếp theo thứ tự giảm dần, khi đó phần tử nhỏ nhất trong danh 
sách sẽ là phần tử thứ mấy?
"""
numbers_list = [3, 5, 77, 13, 90, 15, 23, 27, 30, 9, 21]
# Thay đổi sắp xếp theo thứ tự giảm dần
numbers_list.sort(reverse=True)
print("Dãy số theo thứ tự giảm dần:", numbers_list)
#Tìm phần tử nhỏ nhất và xác định vị trí
min_value = min(numbers_list)
min_index = numbers_list.index(min_value) + 1 
print(f"Phần tử có giá trị nhỏ nhất là: {min_value} và nó ở vị trí trí thứ {min_index}")
#Tính và xuất ra màn hình trung bình cộng các phần tử chia hết cho 3
divisible_by_3 = [number for number in numbers_list if number % 3 == 0]
sum_divisible_by_3 = sum(divisible_by_3)
count_divisible_by_3 = len(divisible_by_3)

if count_divisible_by_3 > 0:
    average = round(sum_divisible_by_3 / count_divisible_by_3, 2)
    print("Trung bình cộng các phần tử chia hết cho 3 là:", average)
else:
    print("Không có phần tử chia hết cho 3")
