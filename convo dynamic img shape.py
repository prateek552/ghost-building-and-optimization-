import sys
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(threshold='nan')
from scipy import signal
import cv2 
import matplotlib as  mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from fractions import gcd
np.set_printoptions(threshold='nan')
from scipy import signal
e=[[0,1], [1,4], [1,3], [1,2], [2,3], [3,4], [1,1]]
#initializing image
i=0
image = [[0 for col in range(10)] for row in range(10)]
#setting the mid of image to 1 to provide a base for convolutin
image[5][5]=1
#Loop to apply all the projections
while(i<7):
    #prints all the projections on the image
    print e[i]
    #calculate the maximaum value to which a kernal can be set
    if(e[i][0]<e[i][1]):
        max=e[i][1]+1
    else:
        max=e[i][0]+1
    #initializing each kernal
    array=[[0 for col in range(max+1)] for row in range(max+1)]
    #if p is negative
    if(e[i][0]<0):
        array[0][max]=1
        array[e[i][1]][(max)-abs(e[i][0])]=-1
    else:
        #if p is possitive
        array[0][0]=1
        array[e[i][1]][abs(e[i][0])]=-1
    #flipping the image to change the initial value of 0,0
    array=np.flip(array,0)
    #applying default concolve2d function
    image=signal.convolve2d(image,array,boundary='fill',mode='full')
    i=i+1
print image