# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 21:15:18 2019

@author: LENOVO
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

myimage='jko.jpg'
X=cv2.imread(myimage,1)
X_origin=X.copy()
X=cv2.cvtColor(X,cv2.COLOR_BGR2GRAY)
plt.rcParams["figure.figsize"]=(16,9)
plt.imshow(X,cmap='gray')

X=cv2.GaussianBlur(X,(21,21),cv2.BORDER_DEFAULT)
plt.rcParams["figure.figsize"]=(16,9)
plt.imshow(X,cmap='gray')

my_gollas=cv2.HoughCircles(X,cv2.HOUGH_GRADIENT,0.9,120,param1=110,
                           param2=35,minRadius=70,maxRadius=400)
all_gollas_rounded=np.uint16(np.around(my_gollas))

print(all_gollas_rounded)
print(all_gollas_rounded.shape())
print("there are "+str(all_gollas_rounded.shape[1])+" coins")








