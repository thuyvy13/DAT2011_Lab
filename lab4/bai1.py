"""
Bài 1
Viết một hàm để tính tiền nước sinh hoạt theo phương pháp lũy tiến. Tham số 
truyền vào hàm là số nước sử dụng trong tháng. 
"""
def tinh_tien_nuoc_sinh_hoat(san_luong):
    gia_ban_nuoc = (7500, 8800, 12000, 24000)
    
    if san_luong <= 10:
        tien_nuoc = san_luong * gia_ban_nuoc[0]
    elif san_luong <= 20:
        tien_nuoc = 10 * gia_ban_nuoc[0] + (san_luong - 10) * gia_ban_nuoc[1]
    elif san_luong <= 30:
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + (san_luong - 20) * gia_ban_nuoc[2]
    else:
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + 10 * gia_ban_nuoc[2] + (san_luong - 30) * gia_ban_nuoc[3]
    
    return tien_nuoc


# print(f"Tiền nước cho 12 m3 là {tinh_tien_nuoc_sinh_hoat(12)} VND")
# print(f"Tiền nước cho 23 m3 là {tinh_tien_nuoc_sinh_hoat(23)} VND")
# print(f"Tiền nước cho 34 m3 là {tinh_tien_nuoc_sinh_hoat(34)} VND")

