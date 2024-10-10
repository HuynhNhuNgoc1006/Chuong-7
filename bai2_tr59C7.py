# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 15:36:14 2024

@author: Huỳnh Như Ngọc
"""

#Cho danh sách sau:
#[('Tiền Giang', 63), ('Long An', 62), ('Vĩnh Long', 64), ('Bình Dương', 60)]
#Sắp xếp các phần tử trong danh sách tăng dần theo số

ds = [('Tiền Giang', 63),('Long An', 62),('Vĩnh Long', 64),('Bình Duong', 60)]
#print(sorted(ds))
print(sorted(ds, key = lambda x: x[1]))

