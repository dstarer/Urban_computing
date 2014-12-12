# -*- encoding: utf-8 -*-
'''
Created on 2014年12月11日

@author: admin
'''
import time
import math


def time2int(string):
    return time.mktime(time.strptime(string, "%Y/%m%d %H:%M:%S"))


class TaxiPath(object):
    '''
    classdocs
    '''
    def __init__(self, filePath):
        '''
        Constructor
        '''
        self.pointSet = []
        self.read_file(filePath)
    
    def read_file(self, filePath):
        fr = open(filePath, 'r')
        title = fr.readline()
        for line in fr.readlines():
            vector = line.strip().split(',')
            self.name = vector[0]
            cur = dict()
            cur.setdefault('moment', time2int(vector[1]))
#             moments = time2int(vector[1])
            cur.setdefault('longitude', float(vector[2]))
#             longitude = float(vector[2])
            cur.setdefault('latitude', float(vector[3]))
#             latitude = float(vector[3])
            cur.setdefault('state', int(vector[4]))
#             state = int(vector[4])
            cur.setdefault('v', int(vector[5]))
#             v = int(vector[5])
            cur.setdefault('angle', int(vector[6]))
#             angle = int(vector[6])
            self.pointSet.append(cur);
            
        fr.close()
        
    def get_start_point(self):
        self.start_point = []
        b = 0
        for item in self.pointSet:
            if item['state'] != b:
                if b == 0:
                    self.start_point.append(item)
                    b = 1
                else:
                    b = 0
    
    def dist2points(self, x, y):
        
        absx = abs(x['longitude'] - y['longitude'])
        absy = abs(x['latitude'] - y['latitude'])
        
        LONGITUDE_PER_DEGREE = 102834.74258026089786013677476285
        LATITUDE_PER_DEGREE = 111712.69150641055729984301412873
        
        absx = absx * LONGITUDE_PER_DEGREE
        absy = absy * LATITUDE_PER_DEGREE
        
        distance = math.sqrt(absx**2 + absy**2)
        
        return distance
    
    def get_moved_distance(self, threshold=60000):
        self.total_distance = 0
        last_point = self.pointSet[0]
        self.no_electri_point = []
        tmp_distance = 0
        for item in self.pointSet:
            tmp = self.dist2points(last_point, item)
            self.total_distance += tmp
            tmp_distance += tmp
            if tmp_distance >= threshold:
                self.no_electri_point.append(item)
        return self.total_distance
    
    def pt2str(self, point):
        string = self.name + ","
        string = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(point['moment'])) + ","
        string += str(point['longitude']) + "," + str(point('latitude'))
        return string
    
    def restore_data(self, flist):
        '''
            restore all the caculated data into file
        '''
        #first restore the start_point set
        
        fp_start_point = open(flist[0], 'a')
        for point in self.start_point:
            fp_start_point.write('%s\n', self.pt2str(point))
        fp_start_point.close()
        
        
        #then restore the no_electri_point set
        fp_no_electri_point = open(flist[1], 'a')
        for point in self.no_electri_point:
            fp_no_electri_point.write('%s\n', self.pt2str(point))
        fp_start_point.close()
        

