def file_reader(file_path: str):
    file = open(file_path, "r")
    list_row = file.readlines()
    arr = []
    for index in range(len(list_row)):
        column_list = list_row[index].strip().split(" ")
        # print(column_list)
        arr.append(column_list)
    res = format_tran(arr)
    return res


def format_tran(source_list):
    res = []
    for i in range(len(source_list)):
        for j in range(len(source_list[i])):
            if not (source_list[i][j] is ' ' or source_list[i][j] is ''):
                res.append([i, j, float(source_list[i][j])])
    return res



