#!/usr/bin/env python

from ase.io import read, write
import numpy as np
import os
from ase import Atoms


def prepare(indices, pool, dist, ads_site, infile='POSCAR.temp', ):
    cwd = os.path.abspath('.')
    dist_path = cwd + '/' + str(dist)
    pnew = read(infile)
    shuffle(pnew, indices, pool)
    create_traj_sur(pnew, dist_path)
    create_traj_ado(pnew, ads_site, dist_path)
    print_list(pnew, indices, dist_path)


def shuffle(pnew, indeices, pool):
    nlist = len(pool)
    for i in indeices:
        ran = np.random.random_integers(nlist)
        pnew[i].symbol = pool[ran - 1]
    return


def create_traj_sur(pnew, dist_path):
    sur_path = dist_path + '/sur'
    if not os.path.isdir(sur_path):
        os.makedirs(sur_path)

    write(sur_path + '/init.traj', pnew)
    write(dist_path + '/POSCAR.sur', pnew)
    return


def create_traj_ado(pnew, ads_site, dist_path):
    pos = pnew[ads_site].position
    # print pos
    adsorbate = Atoms('O', positions=[(pos[0], pos[1], pos[2] + 1.5)])
    pads = pnew + adsorbate

    ads_path = dist_path + '/ado'
    if not os.path.isdir(ads_path):
        os.makedirs(ads_path)

    write(ads_path + '/init.traj', pads)
    write(dist_path + '/POSCAR.ads', pads)
    return


def print_list(pnew, indices, dist_path):
    output = open(dist_path + '/doping.log', 'w')
    for i in indices:
        output.write(str(i) + '\t' + pnew[i].symbol + '\n')
    output.close()
    return
