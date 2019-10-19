from sklearn import manifold


def mds_plot(dissimilarities):
    """
    Get mds plot

    Input: dissimilarity matrix

    Output: lists of Xs and Ys of MDS plot

    """
    x = []
    y = []
    mds = manifold.MDS(n_components=2, dissimilarity="precomputed", random_state=10000000)
    pos = mds.fit(dissimilarities).embedding_
    for point in pos:
        x.append(point[0])
    for point in pos:
        y.append(point[1])
    return y, x
