def tinh_nguyen_lieu(*args):
    nguyen_lieu_banh = {
        'duong': {'banh_dau_xanh': 0.04,'banh_thap_cam': 0.06,'banh_deo': 0.05},
        'dau': {'banh_dau_xanh': 0.07,'banh_thap_cam': 0.0,'banh_deo': 0.02}
    }
    banh_dau_xanh, banh_thap_cam, banh_deo = args
    
    #tinh luong duong va dau
    duong = (banh_dau_xanh * nguyen_lieu_banh['duong']['banh_dau_xanh'] +
             banh_thap_cam * nguyen_lieu_banh['duong']['banh_thap_cam'] +
             banh_deo * nguyen_lieu_banh['duong']['banh_deo'])
    dau = (banh_dau_xanh * nguyen_lieu_banh['dau']['banh_dau_xanh'] +
             banh_thap_cam * nguyen_lieu_banh['dau']['banh_thap_cam'] +
             banh_deo * nguyen_lieu_banh['dau']['banh_deo'])
    
    nguyen_lieu = {'sugar': duong, 'bean': dau}
    return nguyen_lieu

nguyen_lieu_can = tinh_nguyen_lieu(10, 10, 5)
print(nguyen_lieu_can)

# #tinh co ban
# def tinh_nguyen_lieu(banh_dau_xanh, banh_thap_cam, banh_deo):
#     duong = banh_dau_xanh * 0.04 + banh_thap_cam * 0.06 + banh_deo * 0.05
#     dau = banh_dau_xanh * 0.07 + banh_thap_cam * 0 + banh_deo * 0.02
    
#     nguyen_lieu = {'sugar': duong, 'bean': dau}
    
#     return nguyen_lieu

# nguyen_lieu_can = tinh_nguyen_lieu(10, 10, 5)
# print(nguyen_lieu_can)


 