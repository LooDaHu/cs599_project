import matplotlib.pyplot as plt
from k_medoids import return_clusters
from mds import mds_plot

countries = ['BEL', 'BRA', 'CHI', 'CUB', 'EGY', 'FRA', 'IND', 'ISR', 'USA', 'USS', 'YUG', 'ZAI']


def figure2_generator(dissimilarity_matrix):
    """
    Plot the right panel of the figure according to dissimilarity matrix

    Input: dissimilarity matrix

    Output: figure 2

    """
    clusters = return_clusters(dissimilarity_matrix)  # get clusters
    point_color = color_label_generator(clusters)  # give all labels a color according to the clusters
    x, y = mds_plot(dissimilarity_matrix)  # Get positions of labels by MDS
    plot_figure2(x, y, point_color)  # Plot figure2


def color_label_generator(clusters):
    """
    Create a list of colors corresponding to the countries list

    Input: clusters

    Output: list of colors of babels

    """
    colors = ['green', 'red', 'blue']
    point_colors = ["" for i in range(12)]
    for i, cluster in enumerate(clusters):
        for point_num in cluster:
            point_colors[point_num] = colors[i]
    return point_colors


def plot_figure2(x, y, point_colors):
    """
    Plot figure2

    Input: list of x, y and colors

    Output: figure2

    """
    fig, ax = plt.subplots()
    plt.scatter(x, y)
    plt.title("Two-dimensional-MDS Plot with K-medoids")
    plt.xlabel("First MDS Coordinate")
    plt.ylabel("Second MDS Coordinate")
    for i, country in enumerate(countries):
        ax.annotate(country, (x[i], y[i]), color=point_colors[i])
    plt.savefig('figure2.png')
