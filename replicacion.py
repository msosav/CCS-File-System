import os
import shutil

def replicate_file(input_file, output_dirs):
    """
    Replicates a file into three new files in specified directories.
    param input_file: The file to be replicated.
    param output_dirs: A list of two directories where the files will be copied.
    """

    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"File '{input_file}' not found.")

    for i in range(3):
        os.makedirs(output_dirs[i], exist_ok=True)
        shutil.copy(input_file, os.path.join(output_dirs[i], f"{os.path.basename(input_file)}_copy{i+1}"))

# Example usage
input_file = 'input.txt'
output_dirs = ['dir1', 'dir2', 'dir3']
replicate_file(input_file, output_dirs)