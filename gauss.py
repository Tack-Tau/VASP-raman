#!/usr/bin/env python3
# 
# This file is part of Aladdin toolbox.
#
# Copyright (C) 2012 Li Zhu < zhulipresent@gmail.com >.

import os
import math
from optparse import OptionParser

def gauss(input, A, step):

    f = open(input)
    data = []
    try:
        for line in f:
            data.append(list(map(float, line.split())))
    finally:
        f.close()

    w2 = A**2/2/math.log(2.)

    left = data[0][0]
    right = data[-1][0] * 1.1
    x = left

    while x <= right:
        y = 0.
        for i in range(len(data)):
            if (abs(x - data[i][0]) <= 3*A):
                y = data[i][1] / math.exp(2*(x-data[i][0])**2 / w2)+y
        print (str(x)+'\t'+str(y))
        x += step

    return 0

def raman():
    parser = OptionParser()
    parser.set_defaults( w = 2, s = 0.5)
    parser.add_option("-w", dest="w", type="float")
    parser.add_option("-s", dest="s", type="float")
    (options, args) = parser.parse_args()
    w = options.w
    s = options.s
   
    if len( args ) > 0:
        if os.path.exists( args[0] ):
            input = args[0]
        else:
            print ("The input file could not be found.")
            exit(0)
    else:
        print ("The input file could not be found.")
        exit(0)

    gauss(input, w, s)
    return 0

if __name__ == '__main__':
    raman()
