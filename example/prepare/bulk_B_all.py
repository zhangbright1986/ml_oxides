#!/usr/bin/env python

from mlox.prepare import *
from ase.io import read, write
import sys
import subprocess

# customilized input

task = sys.argv[1]
print task
spath='/home1/03672/tg829713/work/stampede2/data_mlox'
infile = spath+'/POSCAR.temp'
pini = read(infile)
indices = [atom.index for atom in pini if atom.symbol == 'Ti' and atom.position[2] < 23]
ads_site_index = 72
pool = ['Nb', 'Mo', 'Ru', 'Rh', 'Pd', 'W', 'Ag', 'Pt', 'Ir', 'Ta', 'Re', 'Zr', 'Ti']
dists = list(range(11,21))

cwd=os.getcwd()


for di in dists:
    dist = str(di).zfill(3)
    if task == 'pre':
        Prepare=prepare(indices, pool, dist, ads_site_index, infile=infile)
        Prepare.run()
    
    elif task == 'submit':
        if os.path.isfile(spath+'/.script/spede.sub'):
            sur_path=cwd+'/'+dist+'/sur'
            ado_path=cwd+'/'+dist+'/ado'
        
            if os.path.isfile(sur_path+'/init.traj') and not os.path.isdir(sur_path+'/min'): 
                print sur_path
                os.chdir(sur_path)
                subprocess.call(["sbatch "+spath+'/.script/spede.sub'],shell=True)

            if os.path.isfile(ado_path+'/init.traj') and not os.path.isdir(ado_path+'/min'): 
                print ado_path
                os.chdir(ado_path)
                subprocess.call(["sbatch "+ spath+'/.script/spede.sub'],shell=True)

os.chdir(cwd)
