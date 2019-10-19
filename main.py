from figure_1 import figure1_generator
from figure_2 import figure2_generator
from file_reader import file_reader_matrix

if __name__ == '__main__':
    dissimilarity_matrix = file_reader_matrix('data_set.txt')  # read data from original file
    figure1_generator(dissimilarity_matrix)  # Plot the first figure(left panel)
    figure2_generator(dissimilarity_matrix)  # Plot the second figure(right panel)
