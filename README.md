# Project-with-Prof-Cheong

The project is still in progress. I will disclose all of the python code once the project is published.

This project aims to explore the hot topics, and detect topic switches. One way to do this, is to analyse all the words in the conference paper by relying on Natural Language Processing to identify keywords cluster.

AKWhidR.py helps to organize the words significance and store them.

So far, we have developed two ways to cluster the identified keywords based on the words significance. One way is to cluster them by k-means clustering using some important factors such as entropy, covariance, and skewness of words over years. The code is included in Clustering.py and KMeansClustering.py

The other way is to first cluster all the keywords according to their time behaviours, and then apply partial hierarchical clustering to do cluster the small clusters. The code is included in PracticematchFiltering.py and PartialHierarchicalClusteringAlgo.py
