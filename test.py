# -*- coding: utf-8 -*-
import numpy as np
from random import randint
import scipy.ndimage as ndimage
a = [int(x) for x in input('Podaj wymiary tablicy: ').split()]

tab = np.random.randint(10,size = (a[0], a[1]))
tab=np.array(tab, dtype = float)


footprint = np.array([[0,1,0],
                      [1,1,1],
                      [0,1,0]])

tabMean=ndimage.generic_filter(tab, np.mean,
                       footprint = footprint)
        
