# -*- coding: utf-8 -*-
"""
Created on Mon May 10 10:15:48 2021

@author: Hien
"""

n = int(input("Nhập số cần tính giai thừa: "))
 
def giaiThua(n):
    if n == 0:
        return 1
    return n * giaiThua(n - 1)
 
print (giaiThua(n))