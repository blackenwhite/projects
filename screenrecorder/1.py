# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:00:29 2019

@author: LENOVO
"""
import cv2 as doki
import numpy as np
import pyscreenshot as pishu

poltu=doki.VideoWriter_fourcc(*'XVID')
keltu=doki.VideoWriter('keltu.avi',poltu,8,(1920,1080))

while(True):
    bhola=pishu.grab()
    bhola_np=np.array(bhola)
    doki.imshow('Dekho',bhola_np)
    keltu.write(bhola_np)
    
    if doki.waitKey(20) & 0xFF==ord('q'):
        break

keltu.release()
doki.destroyAllWindows()
    


