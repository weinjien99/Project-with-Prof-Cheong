import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
from sklearn.cluster import KMeans
from sklearn import metrics
from mpl_toolkits.mplot3d import Axes3D

df = pd.DataFrame(pd.read_csv('C:\\Users\\USER\\Desktop\\clustering.csv'))
df["x"] = (df["cov"]-df["cov"].min()) / (df["cov"].max()-df["cov"].min())
df["y"] = (df["entropy"]-df["entropy"].min()) / (df["entropy"].max()-df["entropy"].min())
df["z"] = (df["skewness"]-df["skewness"].min()) / (df["skewness"].max()-df["skewness"].min())
print(df.head())

#Initialisation
np.random.seed(200)
k = 4
centroids = {
    i+1: [np.random.uniform(0,1),np.random.uniform(0,1),np.random.uniform(0,1)]
    for i in range (k)
}
colmap = {1: 'r', 2: 'g', 3:'b' ,4:'y'}
# 2dplot
# fig = plt.figure(figsize=(5,5))
# plt.scatter(df['cov'],df['entropy'],color='k',marker='+')
# for i in centroids.keys():
#     plt.scatter(*centroids[i],color = colmap[i],)
# plt.xlim(0,1)
# plt.ylim(0,1)
# plt.show()
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(df['x'],df['y'],df['z'],color = 'k',marker = '+')
for i in centroids.keys():
    ax.scatter3D(*centroids[i], color=colmap[i])
ax.set_xlabel('cov')
ax.set_ylabel('entropy')
ax.set_zlabel('skewness')
plt.show()

#assignment stage
def assignment(df,centroids):
    for i in centroids.keys():
        df['distance_from_{}'.format(i)] = (
            np.sqrt(
                (df['x']-centroids[i][0])**2
                + (df['y'] - centroids[i][1])**2
                + (df['z'] - centroids[i][2])**2
            )
        )
    centroids_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:,centroids_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: float(x.lstrip('distance_from')))
    df['color'] = df['closest'].map(lambda x: colmap[x])
    return df
df = assignment(df,centroids)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(df['x'], df['y'],df['z'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    ax.scatter3D(*centroids[i], color=colmap[i])
ax.set_xlabel('cov')
ax.set_ylabel('entropy')
ax.set_zlabel('skewness')
plt.show()

#update stage
import copy
old_centroids = copy.deepcopy(centroids)

def update(k):
    for i in centroids.keys():
        centroids[i][0] = np.mean(df[df['closest'] == i]['x'])
        centroids[i][1] = np.mean(df[df['closest'] == i]['y'])
        centroids[i][2] = np.mean(df[df['closest'] == i]['z'])
    return k

centroids = update(centroids)
# 2dplot
# fig = plt.figure(figsize=(5, 5))
# ax = plt.axes()
# plt.scatter(df['cov'], df['entropy'], color=df['color'], alpha=0.5, edgecolor='k')
# for i in centroids.keys():
#     plt.scatter(*centroids[i], color=colmap[i])
# plt.xlim(0, 1)
# plt.ylim(0, 1)
# plt.show()
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(df['x'], df['y'],df['z'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    ax.scatter3D(*centroids[i], color=colmap[i])
ax.set_xlabel('cov')
ax.set_ylabel('entropy')
ax.set_zlabel('skewness')
plt.show()

#repeat assignment stage
df = assignment(df,centroids)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(df['x'], df['y'],df['z'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    ax.scatter3D(*centroids[i], color=colmap[i])
ax.set_xlabel('cov')
ax.set_ylabel('entropy')
ax.set_zlabel('skewness')
plt.show()

while True:
    closest_centroids = df['closest'].copy(deep=True)
    centroids = update(centroids)
    df = assignment(df,centroids)
    if closest_centroids.equals(df['closest']):
        break

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(df['x'], df['y'],df['z'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    ax.scatter3D(*centroids[i], color=colmap[i])
ax.set_xlabel('cov')
ax.set_ylabel('entropy')
ax.set_zlabel('skewness')
plt.show()

df.to_csv('C:\\Users\\USER\\Desktop\\kmeans.csv')