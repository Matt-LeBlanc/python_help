#!/usr/bin/env python3
import sys
if len(sys.argv) > 1:
    io = sys.argv[1]
elif len(sys.argv) == 1:
    io = input("Enter the file name: ")
help(io)
