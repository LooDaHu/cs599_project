import matplotlib.pyplot as plt
from k_medoids import return_clusters
from mds import mds_plot

countries = ['BEL', 'BRA', 'CHI', 'CUB', 'EGY', 'FRA', 'IND', 'ISR', 'USA', 'USS', 'YUG', 'ZAI']


def figure2_generator(dissimilarity_matrix):
    clusters = return_clusters(dissimilarity_matrix)
    point_color = color_label_generator(clusters)
    x, y = mds_plot(dissimilarity_matrix)
    plot_figure2(x, y, point_color)


def color_label_generator(clusters):
    colors = ['green', 'red', 'blue']
    point_colors = ["" for i in range(12)]
    for i, cluster in enumerate(clusters):
        for point_num in cluster:
            point_colors[point_num] = colors[i]
    return point_colors


def plot_figure2(x, y, point_colors):
    fig, ax = plt.subplots()
    plt.scatter(x, y)
    plt.title("Two-dimensional-MDS Plot with K-medoids")
    plt.xlabel("First MDS Coordinate")
    plt.ylabel("Second MDS Coordinate")
    for i, country in enumerate(countries):
        ax.annotate(country, (x[i], y[i]), color=point_colors[i])
    plt.savefig('figure2.png')
