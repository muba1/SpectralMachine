#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
'''
# **************************************
#
# SpectraExtractorSVM.py
# Extract spectra of specific phases
# version: 20160916d
#
# By: Nicola Ferralis <feranick@hotmail.com>
#
#***************************************
'''
print(__doc__)

import numpy as np
from sklearn import svm
from sklearn.externals import joblib

phaseColumn = 8
selPhase = 6
labelColumn = 2

mapfile = "Dracken-7-tracky_map1_bs_fit2_despiked.txt"
clustfile = "Draken_map1_fit3-den_ratio-d1g-col-clust-all.txt"
newMapFile = "Dracken-7-tracky_map1_bs_fit2_selected.txt"

with open(mapfile, 'r') as f:
    En = np.array(f.readline().split(), dtype=np.dtype(float))


f = open(mapfile, 'r')
A = np.loadtxt(f, unpack =False, skiprows=1)
A = np.delete(A, np.s_[0:2], 1)
f.close()
print(' Shape map: ' + str(A.shape))

f = open(clustfile, 'r')
Cl = np.loadtxt(f, unpack =False, skiprows=1, usecols = range(phaseColumn-1,phaseColumn))
f.close()
print(' Shape cluster vector: ' + str(Cl.shape))

f = open(clustfile, 'r')
L = np.loadtxt(f, unpack =False, skiprows=1, usecols = range(labelColumn-1,labelColumn))
f.close()
print(' Shape label vector: ' + str(L.shape))

phaseMap = np.append([0], En)

for i in range(0,A.shape[0]):
    if Cl[i] == selPhase:
        temp = np.append(L[i], A[i,:])
        phaseMap = np.vstack((phaseMap, temp))

print(' Shape new map: ' + str(phaseMap.shape) + '\n')
#print(phaseMap)

np.savetxt(newMapFile, phaseMap, delimiter='\t', fmt='%10.6f')

#f = open(newMapFile, 'r')
#B = np.loadtxt(f, unpack =False)
#f.close()

#print(B.shape)
#print(B)