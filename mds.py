from sklearn import manifold
from file_reader import file_reader_matrix
import matplotlib.pyplot as plt
from k_medoids import return_clusters


# dissimilarities = file_reader_matrix('data_set.txt')

# mds = manifold.MDS(n_components=2, dissimilarity="precomputed", random_state=10000000)

# countries = ['BEL', 'BRA', 'CHI', 'CUB', 'EGY', 'FRA', 'IND', 'ISR', 'USA', 'USS', 'YUG', 'ZAI']

# pos = mds.fit(dissimilarities).embedding_

# print(pos)
# x = []
# y = []
#
# for point in pos:
#     x.append(point[0])
# for point in pos:
#     y.append(point[1])


# print(point_colors)


def mds_plot(dissimilarities):
    x = []
    y = []
    mds = manifold.MDS(n_components=2, dissimilarity="precomputed", random_state=10000000)
    pos = mds.fit(dissimilarities).embedding_
    for point in pos:
        x.append(point[0])
    for point in pos:
        y.append(point[1])
    return y, x
