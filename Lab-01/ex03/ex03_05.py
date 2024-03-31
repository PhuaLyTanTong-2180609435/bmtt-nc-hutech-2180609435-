def dem_so_lan_xuat_hien(lst):
    cout_dict = {} 
    for item in lst:
        if item in cout_dict:
            cout_dict[item]+=1  
        else:
            cout_dict[item] = 1
    return cout_dict
#Nhập danh sách từ người dùng
input_string =input("Nhập danh sách các từ, cách nhau bằng dấu cách: ")
word_list = input_string.split()
#Sử dụng hàm và in kết quả
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("Số lần xuất hiện của các phần tử : " , so_lan_xuat_hien)