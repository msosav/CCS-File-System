"""
NameNode
"""

# Diccionario que almacena los datanodes y los archivos que contienen
datanodes = {}


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
    datanodes = {
        "file1": {
            "part-0000": ["Datanode1"],
            "part-0001": ["Datanode2"]
        },
        "file2": ["Datanode1"],
        "file3": ["Datanode2"]
    }
    print(locate_file("file1"))
