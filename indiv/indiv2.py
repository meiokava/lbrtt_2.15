#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    rd = str(input("source - "))
    wrt = str(input("where to write - "))
    with open(rd, "r", encoding="utf-8") as file:
        tw = open(wrt, "a")
        s_ind = 1
        q = ""
        for i in file:
            q = str(s_ind) + "; " + i
            s_ind += 1
            tw.write(q+"\n")
        tw.close()
