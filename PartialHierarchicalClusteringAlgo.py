#to import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
os.chdir(r'C:\Users\USER\PycharmProjects\untitled1\ProfProject\SavedFiles')

#to load files
matrix = np.load('latesingleemptymatrix.npy')
word = pd.read_csv(r'C:\Users\USER\Desktop\Document (Odyssey Project)\latesingle.csv')
words = np.array(list(word['word']))
orimatrix = np.copy(matrix)

for i in range(len(matrix)):
    matrix[i][i] = 0

d0 = np.arange(len(words))
z0 = np.amax(matrix)
c0 = np.argwhere(matrix ==z0)[0]

def phclc(c,d,z,matrix):
    l=np.min(matrix[c,:][:,d],axis = 0)
    lmax = np.max(l)
    kmax = np.argwhere(l==lmax)
    jmax = d[kmax[0][0]]
    cc = np.append(c,jmax)
    dd = list(set(d).difference(set(cc)))
    zz = np.append(z,lmax)
    return cc,dd,zz

cluster = []
def propagate(c,d0,z1,matrix):
    c1 = list(c[:len(z1)+1])
    print('index of new cluster:',c1)
    print('word of new cluster:',words[c1])
    cluster.append(c1)
    d0 = list(set(d0).difference(set(c1)))
    matrix[c1,:] = 0
    matrix[:,c1] = 0
    z0 = np.amax(matrix)
    c0 = np.argwhere(matrix == z0)[0]
    return c0,d0,z0,z1,matrix


def visualize(c,d,z,matrix):
    for i in range(20):
        c,d,z = phclc(c,d,z,matrix)
    print(words[c])
    plt.plot(z,'o-')
    plt.show()
    count = 0
    for j in range(len(z)-2):
        count += 1
        if z[j+1]-z[j] != 0:
            if (z[j+2] - z[j+1])/(z[j+1] - z[j]) >2:
                break
        else:
            break
    z1 = z[:count+1]
    return c,z,z1
