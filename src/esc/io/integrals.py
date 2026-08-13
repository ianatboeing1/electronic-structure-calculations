import numpy as np

def read_nuclear_repulsion(filename):
    with open(filename, 'r') as f:
        return(float(f.read().strip()))

def read_symmetric_matrix(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

        nbf = int(lines[-1].split()[0]) if lines else None
        matrix = np.zeros((nbf,nbf))

        for line in lines:
            i, j, value = line.split()
            i, j = int(i) - 1, int(j) - 1
            value = float(value)

            matrix[i,j] = value
            matrix[j,i] = value
        return matrix

def build_core_hamiltonian(T, V):
    return(T + V)

def read_eri(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

        idx_max = 0
        for line in lines:
            i, j, l, k, value = line.split()
            i, j, l, k = int(i), int(j), int(l), int(k)
            idx_max = max(idx_max, i, j, k, l)
        nbf = idx_max
        eri = np.zeros((nbf, nbf, nbf, nbf))

        for line in lines:
            i, j, k, l, value = line.split()
            i, j, k, l, value = int(i) - 1, int(j) - 1, int(k) - 1, int(l) - 1, float(value)
            eri[i, j, k, l] = value
            eri[i, j, l, k] = value
            eri[j, i, k, l] = value
            eri[j, i, l, k] = value
            eri[k, l, i, j] = value
            eri[k, l, j, i] = value
            eri[l, k, i, j] = value
            eri[l, k, j, i] = value
        
        return eri

enuc = read_nuclear_repulsion("data/h2o-sto3g/enuc.dat")
S = read_symmetric_matrix("data/h2o-sto3g/s.dat")
T = read_symmetric_matrix("data/h2o-sto3g/t.dat")
V = read_symmetric_matrix("data/h2o-sto3g/v.dat")
H_core = build_core_hamiltonian(T, V)

eri = read_eri("data/h2o-sto3g/eri.dat")
#print(eri)

i,j,k,l = 6,0,5,2

print(eri[i,j,k,l])
print(eri[j,i,k,l])
print(eri[i,j,l,k])
print(eri[k,l,i,j])
print(eri[l,k,j,i])


# Matrix tests
# Check symmetry
assert np.allclose(T, T.T)
assert np.allclose(V, V.T)
assert np.allclose(np.diag(S), 1)
# The sum of the symmetric matrices is symmetric
assert np.allclose(H_core, H_core.T)

# print(H_core)