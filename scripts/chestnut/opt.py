from ase import optimize
from ase.io import write,read
from espresso import espresso
from ase.io.trajectory import PickleTrajectory
import numpy as np

posin=read("init.traj")
p=posin.copy()

convergence = {'energy':1e-5,
                'mixing':0.1,
                'nmix':10,
                'maxsteps':500,
                'diag':'david'
                }

output = {'avoidio':False,
        'removewf':True,
        'wf_collect':False}

calc = espresso(pw=600 , # Plane wave cutoff
    dw=6000, # Density wave cutoff
    spinpol=False,
    nbands=-100,
    smearing='gauss',
    kpts=(3,3,1), # (rather sparse) k-point (Brillouin) sampling
    xc='RPBE', #Exchange-correlation functional
    dipole={'status':True}, # Includes dipole correction (necessary for asymmetric slabs)
    #psppath='/global/homes/b/brightzh/eds_scratch/perovsike/quanesp/SFO/cell_opt/',
    parflags='-npool 2',
    convergence=convergence,
    #U={'Ti':3.0},
    #U_projection_type='atomic',
    outdir = 'esp.log',
    output = output,) # Espresso-generated files will be put here

calc.calculation_required = lambda x, y: True
#mag0=40*[0]
#mag_afm=[4, -4, 4, -4, 4, -4, 4, -4, 4, -4, 4 , -4]+48*[0]
#p.set_initial_magnetic_moments(mag_afm)

p.set_calculator(calc)
qn = optimize.BFGS(p,trajectory='relax.traj')
qn.run(fmax=0.03)
pe=p.get_potential_energy()
write('fin.traj',p)
write('POSCAR.F',p)

print "[Energy] = "+str(pe)

del p



