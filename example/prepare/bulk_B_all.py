#!/usr/bin/env python

from mlox.prepare import *
from ase.io import read, write
import sys

# customilized input

infile = 'POSCAR.temp'
pini = read(infile)
indices = [atom.index for atom in pini if atom.symbol == 'Ti' and atom.position[2] < 23]
ads_site_index = 72
pool = ['Nb', 'Mo', 'Ru', 'Rh', 'Pd', 'W', 'Ag', 'Pt', 'Ir', 'Ta', 'Re', 'Zr', 'Ti']
#nsites = len(indices)
try:
    dist = str(sys.argv[1])
except IndexError:
    print "Please give the name of the folder you would like to contain the calculations"
    dist = 'trial'
    #exit()

print dist

# Prepartion of Files
prepare=prepare(indices, pool, dist, ads_site_index, infile=infile)
prepare.run()