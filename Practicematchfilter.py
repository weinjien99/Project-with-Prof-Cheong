from typing import List, Any, Union

import numpy as np
import os
os.chdir(r'C:\Users\USER\PycharmProjects\untitled1\ProfProject\SavedFiles')
import matplotlib.pyplot as plt

#to practice
x = [0,0,0,0,0,1,1,1,1,1]
import random
random.seed(30)
x = [i + 0.05*random.randint(1,10) for i in x]
print(x)

y = np.zeros((9,10))
for i in range(9):
    y[i,i+1:] = 1

b = np.arange(0,3,0.1)
sqerrlist4 = []
for bmin in b:
    sqerr = np.linalg.norm(x - bmin*y[4])
    sqerrlist4.append(sqerr)
sqerrlist5 = []
for bmin in b:
    sqerr = np.linalg.norm(x - bmin*y[5])
    sqerrlist5.append(sqerr)
sqerrlist6= []
for bmin in b:
    sqerr = np.linalg.norm(x - bmin*y[6])
    sqerrlist6.append(sqerr)
plt.plot(b,sqerrlist4,'o-',label = '4')
plt.plot(b,sqerrlist5,'o-',label = '5')
plt.plot(b,sqerrlist6,'o-',label = '6')
plt.legend()
plt.show()
def filfun(s,b):
    f = np.zeros(10)
    f[s:] = b
    return f

jmin = 10
smin = 0
bmin1 = 0
for s in range(1,10):
    for bmin in b:
        sqerr = np.linalg.norm(x-filfun(s,bmin))
        if sqerr <= jmin:
            jmin = sqerr
            smin = s
            bmin1 = bmin
print(jmin,smin,bmin1)

jmin = 10
bmin1 = 0
alpha = 0.1
p=10
for s in range(len(y)):
    for i in range(100):
        diffp = -2*np.sum(np.inner(y[s],(x-p*y[s])))
        p = p-alpha*diffp
        sqerr = np.linalg.norm(x - p*y[s])
        if sqerr <= jmin:
            jmin = sqerr
            bmin1 = p
            smin=s
print(jmin,smin+1,bmin1)