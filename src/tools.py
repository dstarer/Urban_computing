# -*- encoding: utf-8 -*-
'''
Created on 2014年12月11日

@author: admin
'''

import os
import sys


def listdir(path):
    fnlist = []
    
    tmp_list = os.listdir(path)
    for line in tmp_list:
        filePath = os.path.join(path, line)
        if os.path.isdir(filePath):
            t_fnlist = listdir(filePath)
            fnlist.extend(t_fnlist)
        elif os.path:
            fnlist.append(os.path.join(path, line))
    
    return fnlist


def test_listpath():
    path = raw_input("please input the path")
    myfile = listdir(path)
    
    ffiles = open("../test/tmp.txt", "w")
    ffiles.write("%d\n" % len(myfile))
    
    for line in myfile:
        ffiles.write("%s\n" % line)
    
    ffiles.close()
    
if '__main__' == __name__:
    test_listpath()