#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 13:48:25 2018

@author: amalia
file to create input txt files for compsim
"""
import numpy as np


print("Don't forget to change the nmt= m")
m = 3200

filename = 'INFILE'

#homogeneous

k=np.ones(m)
k=k*(1.84E-11)
n = 0.36
comp = 0.0


# write permeability text file

# need to give perm.text separate name for each run 
# perm.txt needs to live in the main Csim folder
# need to check if can call Csim from one location and have Data and Out in each realz

perm_fn='perm'+filename+'.txt'

#with open(perm_fn, "w") as f:
#     f.write(" ".join([str(si) for si in s]))
     
line1 = " ".join([str(ki) for ki in k])
line1 = line1 + " kx" + "\n"
anisotropy = 1.0
line2 = " ".join([str(anisotropy * ki) for ki in k])
line2 = line2 + " kz" + "\n"
lines=line1,line2

f=open(perm_fn,"w")
f.writelines(lines)
f.flush()
f.close()

#write porosity file

por = 0.36
comp = 0.0

linepor=" ". join(str(por) for x in range(m))
linepor = linepor + "\n"
linecomp = str(m) + "*" + str(comp)
lines=linepor, linecomp
f=open("por_agu.txt","w")
f.writelines(lines)
f.flush()
f.close()

# write pd-s file

linepd="3.9 3.9 0.85 0.85 0.034 0.0699 0.042 0.87 0.034 6.65 0 0 0"
lines="\n".join(linepd for x in range(m))
f=open("pds_agu.txt","w")
f.write(lines)
f.flush()
f.close()

# write kla portion of the input file 
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




