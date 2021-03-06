#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
*********************************************
* InfoDatasets
* Info data for training databases
* version: 20181219a
* By: Nicola Ferralis <feranick@hotmail.com>
***********************************************
'''
print(__doc__)

import numpy as np
import sys, os.path, h5py
#************************************
''' Main '''
#************************************
def main():
    if len(sys.argv) < 2:
        print(' Usage:\n  python3 InfoDatasets.py <learnData>')
        print(' Requires python 3.x. Not compatible with python 2.x\n')
        return

    En, M = readLearnFile(sys.argv[1])

    numClasses = np.unique(M[:,0]).size
    indClass = np.zeros((numClasses))
    #rosterSpectra = np.zeros((M.shape[0]))
    
    print(M.shape)
    
    for i in range(M.shape[0]):
        indClass[int(M[i,0])]+=1

    for i in range(numClasses):
        print(" Class:",i, "- number per class:", int(indClass[i]))

    print("\n Number of points per spectra:", M[0,1:].size)
    print(" Number of unique classes:", numClasses)
    print(" Original number of spectra in training set:", M.shape[0],"\n")

#************************************
''' Open Learning Data '''
#************************************
def readLearnFile(learnFile):
    print(" Opening learning file: "+learnFile+"\n")
    try:
        if os.path.splitext(learnFile)[1] == ".npy":
            M = np.load(learnFile)
        elif os.path.splitext(learnFile)[1] == ".h5":
            with h5py.File(learnFile, 'r') as hf:
                M = hf["M"][:]
        else:
            with open(learnFile, 'r') as f:
                M = np.loadtxt(f, unpack =False)
    except:
        print("\033[1m" + " Learning file not found \n" + "\033[0m")
        return

    En = M[0,1:]
    A = M[1:,:]
    #Cl = M[1:,0]
    return En, A

#***************************************
''' Save new learning Data '''
#***************************************
def saveLearnFile(M, learnFile):
    if defParam.saveAsTxt == True:
        learnFile += '.txt'
        print(" Saving new training file (txt) in:", learnFile+"\n")
        with open(learnFile, 'ab') as f:
            np.savetxt(f, M, delimiter='\t', fmt='%10.6f')
    else:
        learnFile += '.h5'
        print(" Saving new training file (hdf5) in: "+learnFile+"\n")
        with h5py.File(learnFile, 'w') as hf:
            hf.create_dataset("M",  data=M)

#************************************
''' Main initialization routine '''
#************************************
if __name__ == "__main__":
    sys.exit(main())
