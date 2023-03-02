#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


if __name__ == '__main__':
    curr_path = os.getcwd()
    n_of_d = input("Enter the name of the new directory: ")
    os.mkdir(n_of_d)

    os.chdir(curr_path + '\\' + n_of_d)
    with open("file.txt", "w", encoding="utf-8") as f:
        f.write(os.getcwd())

    n_name = input("Enter your name of the file: ")
    os.rename("file.txt", n_name)
    os.remove(n_name)

