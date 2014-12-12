# -*- encoding: utf-8 -*-
'''
Created on 2014��12��12��

@author: admin
'''

import TaxiPath as TP
import tools
from matplotlib.figure import Figure
from matplotlib.axes._axes import Axes

def get_statistics(store_file):
    file_list = tools.listdir("E:\Code\python\data\gps_data\track_exp")
    for filename in file_list:
        taxi = TP.TaxiPath(filename)
        taxi.get_start_point()
        taxi.get_moved_distance()
        taxi.restore_data(store_file)
        del taxi
    return
    
def get_stored_data(filename):
    fp = open(filename)
    start_point_set = []
    for line in fp.readlines():
        lineArr = line.strip().split(',')
        name = lineArr[0]
        moment = lineArr[1]
        longtitude = float(lineArr[2])
        latitude = float(lineArr[3])
        start_point_set.extend([name, moment, longtitude, latitude])
    
    fp.close() 
    return start_point_set

import matplotlib.pyplot as plt

def plot3D(pointset):
    X = []
    Y = []
    Z = []
    for point in pointset:
        X = point[2]
        Y = point[3]
        Z = point[1]
    ax = plt.subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, rstride=2, cstride=1)
    ax.set_xlabel('longitude')
    ax.set_ylabel('latitude')
    ax.set_zlabel('moment')
    plt.show()

def test():
    store_file = []
    store_file.append('../data/start_point.txt')
    store_file.append('../data/no_electric.txt')
    get_statistics(store_file)
    point_set = get_stored_data(store_file[0])
    plot3D(point_set)