#!/data/data/com.termux/files/usr/bin/python3

import os

with open ('palist','r') as pl:
    pals = [line for line in pl.readlines()
            if line.lower().split().reverse() == line.lower().split()]

print(pals)

