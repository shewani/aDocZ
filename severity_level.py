import os
import cv2
import glob
import urllib
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from sklearn.neighbors import KNeighborsClassifier
col=[]
df=pd.DataFrame()
for i in range(10000):
    col.append("pixel "+str(i+1))
for i in glob.glob("E:\Injury Detection\Chot_train/*.jpg"):
    img= cv2.imread(i, 0)
    img_resized = cv2.resize(img, (100, 100))
    data = np.array( img_resized )
    data=data.ravel()  #2d to 1d image transformation
    df2 = pd.DataFrame(data.reshape(-1, len(data)),columns=col)
    df=df.append(df2)
X=np.array(df)
Y = np.array([2,1,3,1,2,1,1,3,2,3,4,1,1,1,3,4,2,1,2,1,1,1,2,4,4,4,3,4,4,2,1,2,4,2])
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X, Y)
testdat=pd.DataFrame()
for i in glob.glob("E:\Injury Detection\Chot_test/*.jpg"):
    img= cv2.imread(i, 0)
    img_resized = cv2.resize(img, (100, 100))
    data = np.array( img_resized )
    data=data.ravel()  #2d to 1d image transformation
    df2 = pd.DataFrame(data.reshape(-1, len(data)),columns=col)
    testdat=testdat.append(df2)
testdat=np.array(testdat)
pred=clf.predict(testdat)
print(pred)