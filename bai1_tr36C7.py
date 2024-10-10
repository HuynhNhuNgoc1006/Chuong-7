# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:14:14 2024

@author: Huỳnh Như Ngọc
"""

#Bài 1 trang 36

def tinhtong(*args, **kwargs):
    return sum(args)
def tinh_tich(*args, **kwargs):
    tich = 1
    for i in args:
        tich *= i
    return tich
#def tinhtong_(*args, **kwargs):
#  tong = 0
#  for i in args:
#     tong += i
#  return tong    
if __name__=="main__":
    ds=[1,2,3,4,5]
    print(tinhtong(*ds))
    print(tinh_tich(*ds))
    