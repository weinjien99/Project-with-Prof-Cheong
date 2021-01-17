import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import stats
os.chdir(r'C:\Users\USER\PycharmProjects\untitled1\ProfProject\SavedFiles')
import pandas as pd

sorted_list = np.load('stemmedsortedlist.npy',allow_pickle=True).tolist()
normalized_freq = np.load('stemmednormalizedfreq.npy',allow_pickle=True).tolist()

#compute probability
prob = []
for list in normalized_freq:
    pb=[]
    for j in range(len(list)):
        pb.append(list[j]/sum(list))
    prob.append(pb)

#method 1: finding coefficient of variation(ratio of sd and mean)
cov=[]
for i in range(len(normalized_freq)):
    sd = np.std(normalized_freq[i])
    mean = np.mean(normalized_freq[i])
    cov.append(sd/mean)

#method 2: method of entropy
def Ix (probability):
    if probability == 0:
        return 0
    else:
        return (np.log(probability))

def entropy(probability):
    sum = 0
    for p in probability:
        sum = sum + p*(Ix(p))
    return (sum*-1)

E = []
for p in prob:
    E.append(entropy(p))

#method 3: skewness of graphs
skewness = []
for p in prob:
    skewness.append(stats.skew(p))

#to plot
years = np.arange(2001,2017).tolist()
# for i in range(79,200):
i=0
plt.plot(years,prob[i],'r-')
plt.title(sorted_list[i])
plt.xlabel('Years')
plt.ylabel('Frequency per article')
plt.ylim(0,1)
plt.show()

# filename = 'CIKM'+sorted_list[i]+'.pdf'
# plt.savefig('C:\\Users\\USER\\PycharmProjects\\untitled1\\ProfProject\\WordsPlot\\'+filename)
# plt.clf()


# # to save in csv
df = pd.DataFrame({'words':sorted_list,'cov':cov,'entropy':E,'skewness':skewness})
df.to_csv(r'C:\Users\USER\Desktop\stemmedoutput1.csv')



