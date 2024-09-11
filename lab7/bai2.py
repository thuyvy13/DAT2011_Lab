"""
Bài 2 (2 điểm) 
Tạo 1 file mới, đặt tên file là Lab7-Exercise2.txt. Ghi nội dung sau vào file: 
“… 
Nếu một mai tôi có bay lên trời 
Thì người ơi tôi đã sống rất thảnh thơi 
Nếu một mai tôi có đi qua đời 
Thì người ơi tôi đã sống rất tuyệt vời 
…” 
"""

file_path = 'Lab7-Exercise2.txt'

file = open(file_path, 'w', encoding='utf-8')
poem = """
Nếu một mai tôi có bay lên trời 
Thì người ơi tôi đã sống rất thảnh thơi 
Nếu một mai tôi có đi qua đời 
Thì người ơi tôi đã sống rất tuyệt vời 
"""
    
file.write(poem)


