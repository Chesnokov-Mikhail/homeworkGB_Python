def load_from_file(path_file):
    with open(path_file, 'r') as fr:
        line = fr.readline()
    return line
