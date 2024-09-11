poem = '''Kiếp con người mỏng manh như là gió
Sống trên đời có được mấy lần vui
Sao phải đau mà không thể mỉm cười
Gắng buông nỗi ngậm ngùi nơi quá khứ

Nếu có thể sao ta không làm thử
Để tâm hồn khác hai chữ bình an
Cho đôi chân bước thanh thản nhẹ nhàng
Dù hướng đời có muôn ngàn đá sỏi'''

print(poem)

#Kiểm tra từ “con người” có trong chuỗi hay không?
kiem_tra = "con người" in poem
print(kiem_tra)
# Sử dụng cú pháp trích ra 1 phần của chuỗi để lấy từ “con người” trong câu đầu tiên
tu_con_nguoi = (poem[5:14])
print(tu_con_nguoi)
#Chuyển từ “con người” thành chữ hoa
chuyen_doi = tu_con_nguoi.upper()
print(chuyen_doi)
