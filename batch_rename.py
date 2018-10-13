#!/usr/bin/env python
from __future__ import print_function

from os import listdir, rename, stat
from os.path import isfile, join, getmtime, basename, realpath
import sys


def process_file_name(file_name, *args):
    '''
    Process the old file name along with miscellaneous arguments to return the new name.
    '''
    # Currently prefixing all the files with their index number
    # according to their rank in a time-sorted list of files in the directory.
    sorted_file_name_list = args[0]
    file_order = sorted_file_name_list.index(file_name)
    new_file_name = str(file_order + 1).rjust(3, '0') + "_" + file_name
    return new_file_name


def main():
    input_directory_path = "."
    input_directory_path = realpath(input_directory_path)
    print("Processing directory - '{}'".format(input_directory_path))

    
    # Get the list of files in the input directory
    file_name_list = [file_name for file_name in listdir(
        input_directory_path) if isfile(join(input_directory_path, file_name))]
    
    # Remove this script itself from the list (useful if this script itself is present in the directory!)
    self_name = basename(sys.argv[0])
    if self_name in file_name_list:
      file_name_list.remove(self_name)
    
    print("File list :-\n")
    for index, file_name in enumerate(file_name_list):
        print("{}. {}".format(index+1, file_name))
    
    print("\n\n")
    # Sort according to file-creation time
    get_time_of_file = lambda filename: stat(join(input_directory_path, filename)).st_mtime
    sorted_file_name_list = sorted(file_name_list, key=get_time_of_file)

    for index, file_name in enumerate(file_name_list):
        new_file_name = process_file_name(file_name, sorted_file_name_list)
        print("{}. Renaming {} to {}".format(index + 1, file_name, new_file_name))
        if isfile(join(input_directory_path, new_file_name)):
            print("Error: Target name exists already!!")
            continue
        # Uncomment the following line to actually rename instead of just a simulation.
        #rename(file_name, new_file_name)

        
if __name__ == '__main__':
    main()