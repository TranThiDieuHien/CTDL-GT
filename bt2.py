# -*- coding: utf-8 -*-
"""
Created on Mon May 10 10:15:05 2021

@author: Hien
"""

a = int(input("Nhập số a="))
b = int(input("Nhập số b="))


def uscln(a, b):
    while (a != b):
        if (a > b):
            a -= b
        else:
            b -= a
    uscln = a
    return uscln