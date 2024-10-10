# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 14:26:19 2024

@author: Huỳnh Như Ngọc
"""

#bai49_C7
#Viết phương thức kiểm tra một số nhập vào là số chẵn có giá trị âm. Đúng 
#trả về true. Sai trả về false.
#1/
def canbac_n(x,n):
    return x**(1/n)
#1/b
def binhphuong(n):
    if n>0:
        return n**2
    else:
        return "ko hop le, nhap lai n:"
#1/c
def kiemtra(n):
    return n<0 and n%2 == 0
#1/d
def ktra_so(n):
    if n<0 and n%2 != 0:
        return -1
    elif n>0 and n%2 == 0:
        return 1
    return 0
#1/e
def ktra_gtri():
    n = input("nhap n:")
    #cach 1, ktra và ép kiểu 
    if n.replace('.','',1).replace('-','',1).isdigit():
        n = float(n) 
    #cach 2, ktr và éo kiểu số nguyên int
    #lstrip: cắt dấu trừ trc 1 chuỗi: -
    # if n.lstrip('-').isdigit():
        #n = (n)
    #strip cắt dấu trừ đằng trc và sau chuỗi: -123-
    #if n.lstrip('-').isdigit():
        #n = int(n)
         
    if -89 <=n<= 90:
        return n
    print("ko hop le, nhap lai n:")
    return ktra_gtri()
    
    
if __name__=="__main__":
    print(canbac_n(8,3))
    print(binhphuong(3))
    print(kiemtra(-4))
    print(ktra_so(4))
    print(ktra_gtri())
    