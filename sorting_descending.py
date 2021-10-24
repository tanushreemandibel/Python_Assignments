# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 22:51:03 2021

@author: TANUSHREE
"""

def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

dic2=dict(sorted(most_frequent('aabbbc').items(),key= lambda x:-x[1]))

print (dic2)