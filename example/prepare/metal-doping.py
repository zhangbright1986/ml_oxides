#!/usr/bin/env python

from mlox import prepare
from ase.io import read, write
import sys
import os 
import subprocess

# customilized input
task = sys.argv[1]
print task
infile = 'POSCAR.temp'
pini = read(infile)
indices = [atom.index for atom in pini if atom.symbol == 'Ir' and atom.position[2] < 10 and atom.position[2] > 8]
ads_site_index = 15
pool = ['Nb', 'Mo', 'Ru', 'Rh', 'Pd', 'Ag', 'Pt', 'Zr', 'Ti', 'W','Ta','Re','Ir']
#pool = ['Nb', 'Mo', 'Ru', 'Rh', 'Pd', 'Ag', 'Pt', 'Zr', 'W','Ta','Re','Ir']
#pool = ['Ti']
cwd=os.getcwd()
spath='/home1/03672/tg829713/work/metal-doping/'
print cwd
# Prepartion of Files
for pi in pool:
    if task == 'pre':
        dist = pi
        tmp_pool= [pi]
        print tmp_pool
        Prepare=prepare(indices, tmp_pool, dist, ads_site_index, infile=infile)
        Prepare.run()
    
    elif task == 'submit':
        sur_path=cwd+'/'+pi+'/sur'
        ado_path=cwd+'/'+pi+'/ado'
        
        if os.path.isfile(sur_path+'/init.traj'):
            os.chdir(sur_path)
            subprocess.call(["sbatch "+spath+'/.script/spede.sub'],shell=True)
    
        if os.path.isfile(ado_path+'/init.traj'):
            os.chdir(ado_path)
            subprocess.call(["sbatch "+ spath+'/.script/spede.sub'],shell=True)
        
os.chdir(cwd)
