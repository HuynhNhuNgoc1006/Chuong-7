# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 15:53:36 2024

@author: Huỳnh Như Ngọc
"""

#1. Viết hàm khởi tạo giá trị tự động cho seqA gồm N phần tử các số nguyên
#(âm, dương) và số thực (âm, dương).
#• N chọn ngẫu nhiên từ 30 đến 80.
#• Các giá trị số nguyên, số thực chọn ngẫu nghiên từ -79 đến 39. Giá trị số thực
#được làm tròn 2 số thập phân
import random
def tao_seqA():
    n = random.randint(30,80)
    seqA = []
    for i in range(n+1):
        if random.randint(0, 1) == 0:
            seqA.append(round(random.uniform(-79,39),2))
        else:
            seqA.append(random.randint(-79,39))
    return seqA

#2. Viết hàm kiểm tra kiểu dữ liệu từng phần tử
def ktra_dulieu(seqA):
    return [type(i).__name__ for i in seqA]

#3. Viết hàm thống kê số lượng phần tử có trong seqA


def thongke(seqA):
    return len(seqA)
               
#4. Viết hàm sắp xếp dãy seqA thành dãy seqB tăng dần

def sapxep_sepB(seqA):
    return sorted(seqA)


#5. Viết hàm tính trung bình các phần tử trong seqA

def trungbinh(seqA):
    return sum(seqA)/len(seqA)

#6. Viết hàm tính giá trị trung bình giữa hai phần tử nằm giữa trong dãy seqB
#khi N chẵn. Khi N lẻ, thì hàm tính trả về giá trị nằm giữa

def trungbinh_seqB(seqB): 
#vi du chẳn: [1,2,3,4] => (2+3)/2 = ?
# lẻ: [1,2,3] => 2
    n = len(seqB)
    return (seqB[n//2-1] + seqB[n//2])/2 if n%2 ==0 else seqB[n//2] 



# cách 2: if n%2 == 0:
    # return (seqB[n//2-1 + seqB[n//2])/2
    #else:
        #return seqB[n//2]

#7. Viết hàm tính khoảng cách giữa hai giá trị max, min trong dãy seqA hoặc
#seqB

def khoangcach(seq):
    return max(seq)-min(seq)

#8. Viết hàm so sánh các kết quả của của câu 5 và câu 6

def sosanh(seqA, seqB):
    return trungbinh(seqA), trungbinh_seqB(seqB), trungbinh(seqA) == trungbinh_seqB(seqB)


if __name__=="__main__":
    seqA = tao_seqA()
    print(seqA) 
    print(ktra_dulieu(seqA)) 
    print(thongke(seqA)) 
    seqB = sapxep_sepB(seqA)
    print(seqB)
    print(trungbinh(seqA))
    print(trungbinh_seqB(seqB))
    print(khoangcach(seqA))  
    print(khoangcach(seqB))   
    trungbinh(seqA), trungbinh_seqB(seqB)
    sosanhAB = sosanh(seqA, seqB)
    print(sosanhAB) 