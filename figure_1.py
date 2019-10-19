import matplotlib.pyplot as plt
from k_medoids import return_clusters
from mds import mds_plot
import numpy as np
import seaborn as sns

countries = ['BEL', 'BRA', 'CHI', 'CUB', 'EGY', 'FRA', 'IND', 'ISR', 'USA', 'USS', 'YUG', 'ZAI']


def figure1_generator(dissimilarity_matrix):
    clusters = return_clusters(dissimilarity_matrix)
    new_matrix, x_axis, y_axis = rearrange_matrix(clusters, dissimilarity_matrix)
    np_matrix = np.matrix(new_matrix)
    f, ax2 = plt.subplots(figsize=(10, 8))

    p2 = sns.heatmap(np_matrix, linewidths=0.05, ax=ax2, vmax=9, vmin=0, center=None, robust=False,
                     annot=False, xticklabels=x_axis, yticklabels=y_axis, mask=np_matrix == -1)

    ax2.set_title('Reordered Dissimilarity Matrix')

    f.savefig('figure1.png')


def rearrange_matrix(clusters, dissimilarity_matrix):
    seq = []
    re_arr_matrix = []
    x_axis_countries = []
    for cluster in clusters:
        for point in cluster:
            seq.append(point)
        seq.append(" ")
    seq.pop()
    reversed_seq = list(reversed(seq))
    for y_seq in reversed_seq:
        temp = []
        for x_seq in seq:
            if x_seq == ' ' or y_seq == ' ':
                temp.append(-1)
            else:
                temp.append(dissimilarity_matrix[y_seq][x_seq])
        re_arr_matrix.append(temp)
    for index in range(len(seq)):
        if seq[index] == ' ':
            x_axis_countries.append('   ')
        else:
            x_axis_countries.append(countries[seq[index]])
    y_axis_countries = list(reversed(x_axis_countries))
    for row_index in range(len(re_arr_matrix)):
        column_index = 13 - row_index
        while column_index <= 13:
            re_arr_matrix[row_index][column_index] = -1
            column_index = column_index + 1

    return re_arr_matrix, x_axis_countries, y_axis_countries
