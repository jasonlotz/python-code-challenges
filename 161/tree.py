import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    dirs_count = 0
    files_count = 0
    for _, dirs, files in os.walk(directory):
        dirs_count += len(dirs)
        files_count += len(files)

    return (dirs_count, files_count)
