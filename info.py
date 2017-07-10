#!/usr/bin/env python

from ase.io import read,write

Class ini_Atoms(object):

    def __init__(self):
        self.atoms=read('temp.traj')
        ptemp = self.atoms
        self.index_bulk_A = [atom.index for atom in ptemp if atom.symbol == 'Sr']
        self.index_bulk_O = [atom.index for atom in ptemp if atom.symbol == 'O' and atom.tag == 0]
        self.index_bulk_B =  [atom.index for atom in ptemp if atom.symbol == 'Ti' and atom.tag == 0] 
        self.index_sur_B = [atom.index for atom in ptemp if atom.symbol == 'Ti' and atom.tag == 1] 
        self.index_sur_O = [atom.index for atom in ptemp if atom.symbol == 'O' and atom.tag == 1] 

        #print index_sur_B, index_sur_O
        #print index_bulk_A, index_bulk_B, index_bulk_O


