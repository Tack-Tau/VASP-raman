#!/usr/bin/env python
import re
import sys
from math import pi
from shutil import move
import os
import datetime
import time
#import argparse
import optparse

def get_epsilon_from_OUTCAR(outcar_fh):
    epsilon = []
    #
    outcar_fh.seek(0) # just in case
    while True:
        line = outcar_fh.readline()
        if not line:
            break
        #
        if "MACROSCOPIC STATIC DIELECTRIC TENSOR" in line:
            outcar_fh.readline()
            try:
                epsilon.append([float(x) for x in outcar_fh.readline().split()])
                epsilon.append([float(x) for x in outcar_fh.readline().split()])
                epsilon.append([float(x) for x in outcar_fh.readline().split()])
            except:
                import xml.etree.ElementTree as ET
                doc = ET.parse('vasprun.xml')
                root = doc.getroot()
                for v_arr in root.iter('varray'):
                    if v_arr.get('name') == 'epsilon_rpa':
                        for v_line in v_arr.findall('v'):
                            epsilon.append( [ float(x) for x in v_line.text.split() ] )
            return epsilon
    #
    raise RuntimeError("[get_epsilon_from_OUTCAR]: ERROR Couldn't find dielectric tensor in OUTCAR")
    return 1

if __name__ == '__main__':
    outcar_fh = open('OUTCAR', 'r')
    eps = get_epsilon_from_OUTCAR(outcar_fh)
    print "eps=\n", eps
    outcar_fh.close()