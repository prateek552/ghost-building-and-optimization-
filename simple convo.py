"""
Created on Mon Feb 12 04:18:29 2018

@author: Prateek bajaj
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(threshold='nan')
from scipy import signal
#giving the three projection
a=[[-1,0],[-1,1],[0,1],[1,1]]
i=0
#initializing the image matrix
image = [[0 for col in range(30)] for row in range(30)]
image[15][15]=1
while(i<=3):
    #initializing the kernal:
    array=[[0,0,0],[0,0,0],[0,0,0]]
    #giving values to the kernal
    if(a[i][0]<0):
        array[0][2]=1
    else:
        array[0][0]=1
    array[a[i][1]][abs(a[i][0])]=-1
    array=np.flip(array,0)
    #using convolve default function
    image=signal.convolve2d(image,array,boundary='fill',mode='full')
    i=i+1
plt.imshow(image);
print image 