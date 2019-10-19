from pyclustering.cluster.kmedoids import kmedoids


def return_clusters(matrix):
    """
    Get clusters from dissimilarity matrix

    Input: dissimilarity matrix

    Output: clusters

    """
    initial_medoids = [1, 3, 5]  # initialize the 3 medoids
    kmedoids_instance = kmedoids(matrix, initial_medoids, data_type='distance_matrix')  # create a kmedoids instance
    kmedoids_instance.process()  # Go k-medoids
    clusters = kmedoids_instance.get_clusters()  # Get clusters
    return clusters  # return the result
