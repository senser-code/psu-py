def read_file(path):
    file = open(path, "r")
    data = file.read()
    file.close()
    return data

def write_file(path, data):
    file = open(path, "w")
    file.write(data)
    file.close()