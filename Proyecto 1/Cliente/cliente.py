"""
Cliente
"""

import os


def partition_file(input_file):
    """
    Divide el archivo en partes de 1000 bytes
    param file: El archivo a dividir
    return: None
    """
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"File '{input_file}' not found.")

    partition_size = 1000
    storage = "Storage"
    path = os.path.join(storage, input_file)
    os.makedirs(path, exist_ok=True)

    with open(input_file, 'r') as file:
        content = file.read()

    num_partitions = (len(content) + partition_size - 1) // partition_size

    for i in range(num_partitions):
        partition_content = content[i *
                                    partition_size: (i + 1) * partition_size]
        output_file = f"{path}/{partition_name(i)}"
        with open(output_file, 'w') as file:
            file.write(partition_content)

    print(f"File '{input_file}' partitioned into {num_partitions} files.")


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


if __name__ == '__main__':
    while True:
        command = input()
        command_args = command.split(" ")
        instruction = command_args[0]
        if instruction == 'exit':
            break
        elif instruction == 'open':
            file = command_args[1]
            print(f"Opening file '{file}'")
            partition_file(file)
