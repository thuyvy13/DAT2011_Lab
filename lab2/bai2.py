poem = '''Kiếp con người mỏng manh như là gió
Sống trên đời có được mấy lần vui
Sao phải đau mà không thể mỉm cười
Gắng buông nỗi ngậm ngùi nơi quá khứ

Nếu có thể sao ta không làm thử
Để tâm hồn khác hai chữ bình an
Cho đôi chân bước thanh thản nhẹ nhàng
Dù hướng đời có muôn ngàn đá sỏi'''

# Thay thế từ “bình an” bằng từ “hạnh phúc”. 
thay_the = poem.replace("bình an", "hạnh phúc")

# Ghép thêm cụm ký tự “… vào đầu bài thơ và …” vào cuối bài thơ.
poem_complete = "\"..." + thay_the +"...\""

# Xuất bài thơ đã được thay thế từ ra màn hình.
print(poem_complete)