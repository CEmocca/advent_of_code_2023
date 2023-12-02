

def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines]