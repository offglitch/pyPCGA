#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 12:14:55 2018

@author: amalia
"""

m = 3200
dm = '%3.2e' % 0.0546
linedm=" ". join(str(dm) for x in range(m))
linedm = linedm + " 1.5 1 1 1 kla \n" 

f = open("Case1_NAPLh.dat","r")
contents = f.readlines()
f.close()
print('deleting... kla line')
print(contents[38])
del contents[38]
contents.insert(38,linedm)

f = open("Case1_NAPLh_kla.dat","w")
contents="".join(contents)
f.write(contents)
f.flush()
f.close()