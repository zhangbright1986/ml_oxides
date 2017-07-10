#!/usr/bin/env python

from ase.io import read, write

ptemp=read('template/POSCAR.temp')
index_bulk_A = [atom.index for atom in ptemp if atom.symbol == 'Sr']
index_bulk_O = [atom.index for atom in ptemp if atom.symbol == 'O' and atom.position[2] < 23]
index_bulk_B = [atom.index for atom in ptemp if atom.symbol == 'Ti' and atom.position[2] < 23]
index_sur_B = [atom.index for atom in ptemp if atom.symbol == 'Ti' and atom.position[2] > 23]
index_sur_O = [atom.index for atom in ptemp if atom.symbol == 'O' and atom.position[2] > 23]
list_B = ['Nb', 'Mo', 'Ru', 'Rh', 'Pd', 'W', 'Ag', 'Pt', 'Ir', 'Ta','Re','Zr','Ti']

