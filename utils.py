

def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines]
    
def read_whole_file_as_string(file_name):
    with open(file_name, 'r') as file:
        return file.read()