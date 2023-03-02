#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def punk(f):
    if ((f == ",") or (f == ".") or (f == "!") or (f == ";") or
            (f == ":") or (f == "?")):
        return 1


if __name__ == "__main__":
    file = open("my_file.txt", encoding='UTF')
    f = file.readlines()
    c = 0
    h = 0
    m_punk = 0
    for sim in f:
        c = 0
        for i in sim:
            if punk(i) == 1:
                c += 1
        if c < h:
            h = c
            m_punk = sim
    for sim in f:
        c = 0
        for i in sim:
            if punk(i) == 1:
                c += 1
        if c == h:
            print(sim)
