#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

if __name__ == "__main__":

    # creation of the new directory that the user chooses
    directory = input('Enter the name of your new directory: ')
    parent_dir = "C:\\OPI"
    path = os.path.join(parent_dir, directory)
    os.makedirs(path)
    print(f'Directory {directory} was created')
    dir_list = os.listdir(parent_dir)

    # displaying files and directories in the OPI directory
    print(f'\nFiles and directories in OPI directory: {dir_list}')

    # creation and filling of the file
    os.chdir(path)
    fd = input("\nCreate your file, enter it's name: ")
    wr_in_file = input('Write something in your file: ')
    with open(fd, "w+", encoding="utf-8") as f:
        f.write(wr_in_file)

