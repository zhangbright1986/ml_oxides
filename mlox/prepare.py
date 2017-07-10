#!/usr/bin/env python

from ase.io import read, write
from template import *
import numpy as np
import os
from ase import Atom

def prepare():
    pnew = ptemp.copy()
    shuffle(pnew)
    create_traj_sur(pnew)
    create_traj_ado(pnew)
    write('POSCAR.new', pnew)
    print_list(pnew)


def shuffle(pnew):
    nlist = len(list_B)
    for i in index_bulk_B:
        ran = np.random.random_integers(nlist)
        pnew[i].symbol = list_B[ran - 1]
    return


def create_traj_sur(pnew):
    cwd=os.path.abspath('.')
    if not os.path.isdir(cwd+'/sur'):
        os.mkdir("{0}/sur".format(cwd))

    write(cwd+'/sur/init.traj',pnew)

    return


def create_traj_ado(pnew):
    cwd = os.path.abspath('.')
    pos=pnew[index_ads_B].position
    print pos
    adsorbate = Atom['O',(pnew[index_ads_B].position[0],pnew[index_ads_B].position[1],pnew[index_ads_B].position[0]+1.5)]
    pnew += adsorbate

    if not os.path.isdir(cwd + '/ado'):
        os.mkdir("{0}/ado".format(cwd))

    write(cwd + '/ado/init.traj', pnew)
    return


def print_list(pnew):
    output = open('doping.log', 'w')
    for i in index_bulk_B:
        output.write(str(i) + '\t' + pnew[i].symbol + '\n')
    output.close()
    return



    # print index_sur_B, index_sur_O
    # print index_bulk_A, index_bulk_B, index_bulk_O
