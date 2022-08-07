def load_file(filepath):
    data = ''
    with open(filepath,'r') as fr:
        data = fr.read()
    return data

def save_file(filepath, data):
    with open(filepath,'w') as fw:
        fw.write(data)