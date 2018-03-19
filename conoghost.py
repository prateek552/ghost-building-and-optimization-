"""
Created on Mon Feb 12 04:18:27 2018

@author: Prateek bajaj
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
np.set_printoptions(threshold='nan')
from scipy import signal
from fractions import gcd
#default projections
a=[[-1,3],[2,3],[2,3]]
i=0
#initializing the image
image = [[0 for col in range(30)] for row in range(30)]
image[15][15]=1
#initializing dummy image to imply convo ghost
new = [[0 for col in range(30)] for row in range(30)]
#To apply all the projections
while(i<=2):
    #when p is less than or equal to 0
    if(a[i][0]<=0):
        for k in range(0,16):
            for l in range(0,25):
                new[k][l]=image[k][l]-image[(k+a[i][1])][(l+abs(a[i][0]))]
    #when p is greater than 0
    if(a[i][0]>0):
        for k in range(0,16):
            for l in range(0,25):
                new[k][l]= (image[k][l]-image[(k+a[i][1])][l-(a[i][0])])
            
    #initializing the old image to the new_image      
    i=i+1 
    image=new
print image
plt.imshow(image)
plt.savefig('f.png')