from pyclustering.cluster.kmedoids import kmedoids


def return_clusters(matrix):
    initial_medoids = [1, 3, 5]
    # matrix = file_reader_matrix('data_set.txt')
    kmedoids_instance = kmedoids(matrix, initial_medoids, data_type='distance_matrix')
    # run cluster analysis and obtain results
    kmedoids_instance.process()
    clusters = kmedoids_instance.get_clusters()
    return clusters
