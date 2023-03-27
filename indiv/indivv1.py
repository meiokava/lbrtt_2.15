#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def punk(f):
    s = ",.!;:?"
    if f in s:
        return 1


if __name__ == "__main__":
    c = 0
    h = 0
    m_punk = 0
    with open("my_file.txt", "r", encoding="utf-8") as file:
        f = file.readlines()
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
