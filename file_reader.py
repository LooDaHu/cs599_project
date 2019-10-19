def file_reader(file_path: str):
    arr = file_reader_raw(file_path)
    res = format_tran(arr)
    return res


def file_reader_raw(file_path: str):
    file = open(file_path, "r")
    list_row = file.readlines()
    arr = []
    for index in range(len(list_row)):
        column_list = list_row[index].strip().split(" ")
        # print(column_list)
        arr.append(column_list)
    return arr


def file_reader_matrix(file_path: str):
    arr = file_reader_raw(file_path)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = float(arr[i][j])
    return arr


def format_tran(source_list):
    res = []
    for i in range(len(source_list)):
        for j in range(len(source_list[i])):
            res.append([i, j, float(source_list[i][j])])
    return res
