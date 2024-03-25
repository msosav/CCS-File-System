"""
NameNode
"""

# Diccionario que almacena los datanodes y los archivos que contienen
datanodes = {}
active_datanodes = []
files = {}


def distribute_file(file_name, num_partitions, size):
    """
    Distribuye un archivo en los datanodes
    param file_name: El nombre del archivo
    param num_partitions: La lista de partes del archivo
    return: El diccionario de datanodes
    """
    datanodes[file_name] = {}
    datanode_index = 0
    for i in range(num_partitions):
        if datanode_index >= len(active_datanodes):
            datanode_index = 0
        datanodes[file_name][partition_name(
            i)] = [active_datanodes[datanode_index]]
        datanode_index += 1
    files[file_name] = size
    return datanodes[file_name]


def partition_name(i):
    """
    Genera el nombre de la partición
    param i: El número de la partición
    return: El nombre de la partición
    """
    length = len(str(i))
    serial = '0' * (4 - length) + str(i)
    name = f"part-{serial}"
    return name


def locate_file(file_name):
    """
    Localiza un archivo
    param file_name: El nombre del archivo
    return: La lista de ubicaciones del archivo
    """
    if file_name not in datanodes:
        return []
    return datanodes[file_name]


if __name__ == "__main__":
    active_datanodes = ["Datanode1", "Datanode2"]
    print(distribute_file("file4", 3, 3000))
