"""
Bài 4 (2 điểm)
Viết chương trình xuất ra màn hình bảng cửu chương
"""
# x = 7
# for i in range(1,10):
#     print("%d x %d = %d" %(x, i, x*i))

# for i in range(1,11):
#     for j in range(1, 10):
#         print("%d x %d = %d" %(i, j, i*j), end='\t')
#     print()
    

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{i} x {j} = {i * j}", end='\t')  
#     print()  

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j:2}", end='    ')
    print()  

