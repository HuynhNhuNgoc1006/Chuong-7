# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:33:05 2024

@author: Huỳnh Như Ngọc
"""

#Bai 2 - 36
import math
def chuvi_dt(hinh, pheptinh, *args, **kwargs):
    if hinh == "hinhvuong":
        canh = args[0]
        return 4*canh if pheptinh == 'chuvi' else canh**2
    #tách cau return:
        #if pheptinh == "chuvi":
            #return 4*canh
        #else:
            #return canh**2
            
    elif hinh == "chunhat":
        dai = args[0]
        rong = args[1]
        return 2*(dai+rong) if pheptinh =="chuvi" else dai*rong
    
    elif hinh == 'hinhtron':
        bk = args[0]
        return 2*math.pi*bk if pheptinh =="chuvi" else math.pi *bk**2
               
    else:
        return 'hinh ko hop le'
    
if __name__=="__main__":
    print('chu vi hinh vuong:', chuvi_dt('hinhvuong','chuvi',4))
    print("chu vi hinh vuong:", chuvi_dt('hinhvuong','dientich',4))
    print("chu vi hinh chu nhat:", chuvi_dt('chunhat','chuvi',4,3))
    print("chu vi hinh chu nhat:", chuvi_dt('chunhat','dientich',4,3))
    print("chu vi hinh tron:", chuvi_dt('hinhtron','chuvi',4))
    print("chu vi hinh tron:", chuvi_dt('hinhtron','dientich',4))
    
    
    