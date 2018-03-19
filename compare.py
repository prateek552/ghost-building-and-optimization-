"""
Created on Thu Feb 15 20:17:04 2018

@author: Prateek bajaj
"""

import sys
import random
import cv2
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import numpy as np
from scipy import signal
from fractions import gcd
np.set_printoptions(threshold='nan')
from scipy import signal
m=0
a=[[0 for col in range(2)] for row in range(7)]
b=[[0 for col in range(2)] for row in range(6)]
c=[[0 for col in range(2)] for row in range(6)]
d=[[0 for col in range(2)] for row in range(5)]
for i in range(1,5):
    for j in range(i+1,5):
        if (gcd(i,j)==1):
            a[m]=[i,j]
            b[m]=[j,i]
            c[m]=[-j,i]
            d[m]=[-i,j]
            m=m+1
a[m]=[0,1]
b[m]=[1,0]
c[m]=[-1,1]
a[m+1]=[1,1]
e=[[0 for col in range(2)] for row in range(24)]

for i in range(0,24):
    if(i<7):
        e[i]=a[i]
    if(i>=7 and i<13):
        e[i]=b[i-7]
    if(i>=13 and i<19):
        e[i]=c[i-13]
    if(i>=19):
        e[i]=d[i-19]
f=random.sample(range(0, 24), 4)
i=0
print e
image = [[0 for col in range(30)] for row in range(30)]
image[15][15]=1
#convolution default
while(i<4):
    #prints all the projections on the image
    #calculate the maximaum value to which a kernal can be set
    if(e[f[i]][0]<e[f[i]][1]):
        ma=e[f[i]][1]+1
    else:
        ma=e[f[i]][0]+1
    #initializing each kernal
    array=[[0 for col in range(ma+1)] for row in range(ma+1)]
    #if p is negative
    if(e[f[i]][0]<0):
        array[0][ma]=1
        array[e[f[i]][1]][(ma)-abs(e[f[i]][0])]=-1
    else:
        #if p is possitive
        array[0][0]=1
        array[e[f[i]][1]][abs(e[f[i]][0])]=-1
    #flipping the image to change the initial value of 0,0
    array=np.flip(array,0)
    #applying default concolve2d function
    image=signal.convolve2d(image,array,boundary='fill',mode='full')
    i=i+1
#print image
image2 = [[0 for col in range(image.shape[0])] for row in range(image.shape[1])]
image2[image.shape[0]/2][image.shape[0]/2]=1
i=0
print f
#initializing dummy image to imply convo ghost
new_image = [[0 for col in range(image.shape[0])] for row in range(image.shape[1])]
#To apply all the projections

while(i<=3):
    new_image=image2
    print e[f[i]][0]
    #when p is less than or equal to 0
    if(e[f[i]][0]<=0):
        for k in range(0,image.shape[0]/2):
            for l in range(0,image.shape[0]-4):
                new_image[k][l]=image2[k][l]-image2[(k+e[f[i]][1])][(l+abs(e[f[i]][0]))]
    #when p is greater than 0
    if(e[f[i]][0]>0):
        for k in range(0,image.shape[0]/2):
            for l in range(0,image.shape[0]-4):
                new_image[k][l]=image2[k][l]-image2[(k+e[f[i]][1])][(l-(e[f[i]][0]))]
    """else:    
        for k in range(0,44):
            for l in range(0,83):
                new_image[k][l]=image[k][l]-image[(k+a[i][1])][(l+a[i][0])]"""
    #initializing the old image to the new_image
    image2=new_image        
    i=i+1
plt.imshow(image2)
plt.savefig('ghost.png')
image=image[~np.all(image == 0, 1)]
image=np.transpose(image)
image=image[~np.all(image == 0, 1)]
image=np.transpose(image)
plt.imshow(image)
plt.savefig('convo.png')
g=np.shape(image2)
k=np.shape(image)
t='unmatch'
for i in range(0, g[0]):
    for j in range(0,g[1]):
        for b in range(0, k[0]):
            for h in range(0, k[1]):
                if((i+b)>=g[0] or (j+h)>=g[1]):
                    break
                    print 'f'
                if(image2[i+b][j+h] != image[b][h]):
                    break
        if(b==k[0]-1 and h==k[1]-1):
            t='match'
print t