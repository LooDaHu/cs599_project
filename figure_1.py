import matplotlib.pyplot as plt
from k_medoids import return_clusters
from mds import mds_plot
import numpy as np
import seaborn as sns

countries = ['BEL', 'BRA', 'CHI', 'CUB', 'EGY', 'FRA', 'IND', 'ISR', 'USA', 'USS', 'YUG', 'ZAI']


def figure1_generator(dissimilarity_matrix):
    """
    Plot the left panel of the figure according to dissimilarity matrix

    Input: dissimilarity matrix

    Output: figure 1

    """
    clusters = return_clusters(dissimilarity_matrix)  # get clusters
    new_matrix, x_axis, y_axis = rearrange_matrix(clusters,
                                                  dissimilarity_matrix)  # rearrange the matrix according to the result
    plot_figure1(new_matrix, x_axis, y_axis)


def rearrange_matrix(clusters, dissimilarity_matrix):
    """
    Rearrange the original dissimilarity matrix to the new matrix

    Input: the result of k-medoids, dissimilarity matrix

    Output: rearranged matrix, rearranged country label for x-axis and y-axis

    """
    seq = []
    re_arr_matrix = []
    x_axis_countries = []

    # Create a list of new x-axis seq according to the result
    for cluster in clusters:
        for point in cluster:
            seq.append(point)
        seq.append(" ")
    seq.pop()
    reversed_seq = list(reversed(seq))
    # Block ends here

    # Start rearranging the matrix
    for y_seq in reversed_seq:
        temp = []
        for x_seq in seq:
            if x_seq == ' ' or y_seq == ' ':
                temp.append(-1)
            else:
                temp.append(dissimilarity_matrix[y_seq][x_seq])
        re_arr_matrix.append(temp)
    # End rearranging the matrix

    # Create a list of x-axis and y-axis label
    for index in range(len(seq)):
        if seq[index] == ' ':
            x_axis_countries.append('   ')
        else:
            x_axis_countries.append(countries[seq[index]])

    y_axis_countries = list(reversed(x_axis_countries))
    # Block ends here

    # Give all unused cells -1 to keep the left-side of the matrix
    for row_index in range(len(re_arr_matrix)):
        column_index = 13 - row_index
        while column_index <= 13:
            re_arr_matrix[row_index][column_index] = -1
            column_index = column_index + 1
    # Block ends here

    return re_arr_matrix, x_axis_countries, y_axis_countries


def plot_figure1(new_matrix, x_axis, y_axis):
    """
    Plot figure1

    Input: rearranged matrix, x-axis labels, y-axis labels

    Output: figure1

    """
    np_matrix = np.matrix(new_matrix)  # tran the new matrix into numpy array
    # Start plotting
    f, ax2 = plt.subplots(figsize=(10, 8))

    # Give all necessary parameters here, including mask for all -1 cells
    p2 = sns.heatmap(np_matrix, linewidths=0.05, ax=ax2, vmax=9, vmin=0, center=None, robust=False,
                     annot=False, xticklabels=x_axis, yticklabels=y_axis, mask=np_matrix == -1)

    ax2.set_title('Reordered Dissimilarity Matrix')
    # Finish plotting
    f.savefig('figure1.png')  # Output the result figure.
