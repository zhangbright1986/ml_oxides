#!/usr/bin/env python

from ase.io import read, write
import numpy as np
import os
from ase import Atoms
import shutil
from ase.constraints import FixAtoms


class prepare:
    def __init__(self, indices, pool, dist, ads_site, nsites=None, infile='POSCAR.temp'):

        self.indices = indices
        self.pool = pool
        self.ads_site = ads_site
        self.pnew = read(infile)

        if nsites is None or nsites > len(self.indices):
            self.nsites = len(self.indices)
        else:
            self.nsites = nsites

        print str(self.nsites) + ' of ' + str(self.indices) + ' will be randomly replaced by elements from ' + str(
            self.pool) + '\n'
        cwd = os.path.abspath('.')
        self.dist_path = cwd + '/' + str(dist)

    def preOpt(self):
        self.shuffle()
        self.create_traj_sur()
        self.create_traj_ado()
        self.print_list()

    def shuffle(self):
        tmp_pool = self.pool[:] #copy self.pool
        tmp_indices=self.indices[:] #copy self.indices

        for i in range(10):   # shuffle 10 times
            np.random.shuffle(tmp_indices)
            np.random.shuffle(tmp_pool)

        nelm_pnew=len(np.unique(self.pnew.get_chemical_symbols()))
        print nelm_pnew
        nlist=len(tmp_pool)  

        if  nlist > 9 - nelm_pnew :  # avoid the ntype error for QE calculator 
            nlist = 9 - nelm_pnew

        indices=tmp_indices[:self.nsites] # randomly pick nsites sites to be replaced 
        pool=tmp_pool[:nlist] # randomly pick 6 elements from pool
        for i in indices:
            ran = np.random.random_integers(nlist)
            self.pnew[i].symbol = pool[ran - 1]
        return


    def create_traj_sur(self):
        sur_path = self.dist_path + '/sur'
        if not os.path.isdir(sur_path):
            os.makedirs(sur_path)

        write(sur_path + '/init.traj', self.pnew)
        write(sur_path + '/POSCAR', self.pnew)
        write(self.dist_path + '/POSCAR.sur', self.pnew)
        return


    def create_traj_ado(self):
        pos = self.pnew[self.ads_site].position
        # print pos
        adsorbate = Atoms('O', positions=[(pos[0], pos[1], pos[2] + 1.5)])
        pads = self.pnew + adsorbate

        ads_path = self.dist_path + '/ado'
        if not os.path.isdir(ads_path):
            os.makedirs(ads_path)

        write(ads_path + '/init.traj', pads)
        write(ads_path + '/POSCAR', pads)
        write(self.dist_path + '/POSCAR.ads', pads)
        return


    def print_list(self):
        output = open(self.dist_path + '/doping.log', 'w')
        output.write(
            str(self.nsites) + ' of ' + str(self.indices) + ' is randomly replaced by elements from ' + str(self.pool) + '\n')
        for i in self.indices:
            output.write(str(i) + '\t' + self.pnew[i].symbol + '\n')

        output.close()
        return

def preSP(di):
    cwd = os.path.abspath('.')
    dist = cwd + '/' + str(di)
        
    sur_path = dist + '/sur'
    sp_path = dist + '/estr'

    if not os.path.isdir(sp_path):
        os.makedirs(sp_path)
        
    if os.path.isdir(sur_path+'/min') and os.path.isfile(sur_path+'/init.traj'):
        print sp_path
        shutil.copyfile(sur_path+'/init.traj', sp_path+'/init.traj')

def preFro(di, site):
    cwd = os.path.abspath('.')
    dist = cwd + '/' + str(di)
        
    sur_path = dist + '/sur'
    fro_path = dist + '/frado'

    if not os.path.isdir(fro_path):
        os.makedirs(fro_path)
    
    try:
        psur=read(sur_path+'/init.traj')
    except:
        psur=read(sur_path+'/POSCAR.F')

    pos=psur[site].position
    
    adsorbate = Atoms('O', positions=[(pos[0], pos[1], pos[2] + 1.5)])
    ptmp = psur.copy()
    c = FixAtoms(mask=[True for p in ptmp])
    ptmp.set_constraint(c)
    pads = ptmp + adsorbate
    
    write(fro_path + '/init.traj', pads)
    write(fro_path + '/POSCAR', pads)


    

