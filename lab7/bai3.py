"""
Bài 3 (2 điểm) 
Viết chương trình để nhập thông tin của 5 bài thơ từ bàn phím và ghi vào file theo 
định dạng csv. Thông tin của bài hát bao gồm: tiêu đề, tác giả và năm sáng tác.  
"""

import csv

poems = []
for i in range(5):
    title = input(f"Nhập tiêu đề bài thơ {i+1}: ")
    author = input(f"Nhập tên tác giả bài thơ {i+1}: ")
    year = input(f"Nhập năm sáng tác bài thơ {i+1}: ")
    poems.append([title, author, year])

file = open("poems.csv", "w", newline='', encoding="utf-8")
writer = csv.writer(file)
writer.writerow(["Tiêu đề", "Tác giả", "Năm sáng tác"])
writer.writerows(poems)
    
