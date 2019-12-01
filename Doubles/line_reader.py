def read_from_file(file_name):
    in_file = open(file_name, 'r')
    line = in_file.readline()
    return line
