import numpy as np
import scipy
import os

def read_nuclear_repulsion(filename):
    with open(filename, 'r') as f:
        return(f.read().strip())

def read_overlap_matrix(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

        nbf = int(lines[-1].split()[0]) if lines else None
        ao_matrix = np.zeros((nbf,nbf))

        for line in lines:
            i, j, value = line.split()
            i, j = int(i) - 1, int(j) - 1
            value = float(value)

            ao_matrix[i,j] = value
            ao_matrix[j,i] = value
        return ao_matrix

def read_kinetic_energy_matrix(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        nbf = int(lines[-1].split()[0]) if lines else None
        ke_matrix = np.zeros((nbf,nbf))

        for line in lines:
            i, j, value = line.split()
            i, j = int(i) - 1, int(j) - 1
            value = float(value)

            ke_matrix[i,j] = value
            ke_matrix[j,i] = value
        return(ke_matrix)

#print(read_nuclear_repulsion("data/h2o-sto3g/enuc.dat"))
print(read_kinetic_energy_matrix("data/h2o-sto3g/s.dat"))