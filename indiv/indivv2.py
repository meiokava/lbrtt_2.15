#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    rd = str(input("source - "))
    wrt = str(input("where to write - "))
    q = ""
    with open(rd, "r", encoding="utf-8") as file:
        with open(wrt, "a", encoding="utf-8") as tw:
            for index, value in enumerate(file):
                q = '; '.join([str(index + 1), value])
                tw.write('\n'.join([q]))