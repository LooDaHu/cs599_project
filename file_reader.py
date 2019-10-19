def file_reader(file_path: str):
    """
    Read  data from txt file

    Input: file path

    Output: the array of data(float)

    """
    arr = file_reader_raw(file_path)
    res = format_tran(arr)
    return res


def file_reader_raw(file_path: str):
    """
    Read  data from txt file

    Input: file path

    Output: the array of data(String)

    """
    file = open(file_path, "r")
    list_row = file.readlines()
    arr = []
    for index in range(len(list_row)):
        column_list = list_row[index].strip().split(" ")
        # print(column_list)
        arr.append(column_list)
    return arr


def file_reader_matrix(file_path: str):
    """
    Read  data from txt file

    Input: file path

    Output: the array of data(matrix format)

    """
    arr = file_reader_raw(file_path)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = float(arr[i][j])
    return arr


def format_tran(source_list):
    """
      Change the type of every element in the array

      Input: source array

      Output: processed array

      """
    res = []
    for i in range(len(source_list)):
        for j in range(len(source_list[i])):
            res.append([i, j, float(source_list[i][j])])
    return res
