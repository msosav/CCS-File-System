import os


def partition_file(input_file, output_prefix, partition_size):
    """
    Partitions a file into smaller files of a given size.
    param input_file: The file to be partitioned.
    param output_prefix: The prefix of the output files.
    param partition_size: The size of the output files in bytes.
    """

    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"File '{input_file}' not found.")

    storage = "Storage"

    path = os.path.join(storage, input_file)

    os.makedirs(path, exist_ok=True)

    with open(input_file, 'r') as f:
        content = f.read()

    num_partitions = (len(content) + partition_size - 1) // partition_size

    for i in range(num_partitions):
        partition_content = content[i *
                                    partition_size: (i + 1) * partition_size]

        output_file = f"{path}/{partition_name(i)}_{i + 1}.txt"
        with open(output_file, 'w') as f:
            f.write(partition_content)

    print(f"File '{input_file}' partitioned into {num_partitions} files.")


def partition_name(i):
    length = len(str(i))
    serial = '0' * (4 - length) + str(i)
    name = f"part-{serial}.txt"
    return name


# Example usage
input_file = 'input.txt'
output_prefix = 'partitioned_file'
partition_size = 1000  # In bites

partition_file(input_file, output_prefix, partition_size)
