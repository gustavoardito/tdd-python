import os


def read_from_file(file_name):
    if not os.path.exists(file_name):
        raise Exception('Bad File')

    in_file = open(file_name, 'r')
    line = in_file.readline()
    return line
