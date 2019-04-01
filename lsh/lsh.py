from scipy.io import mmread

import numpy as np
from sklearn.neighbors import NearestNeighbors, LSHForest

from igraph import Graph, EdgeSeq
from timeit import timeit
import random


random.seed(100)

#robjects.r['load']('../processed_sub_Data.RData')
print "Reading sparce matrix..."
matrix = mmread("sub_matrix")
print "Converting matrix to dense format..."
a = np.array(matrix.todense())
print a.shape
print "Initialize LSH..."
lshf = LSHForest(n_neighbors=10,random_state=1, n_estimators = 10)
print "fit LSH..."
lshf.fit(a)

K= lshf.kneighbors_graph(a)

print "convert into adjacency matrix..."
K = K.toarray()

g = Graph.Adjacency(K.tolist())
es = EdgeSeq(g)

print "writing graph edgelist..."
g.write_edgelist("src_dst_lsh.csv")
