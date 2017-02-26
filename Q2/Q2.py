
import sys


init_vec = [0,0,1]
x_vec = init_vec
mat = [[2,3,2],[10,3,4],[3,6,1]]

def matrix_X_vector(matrix,vector):
    ret_vector = [0]*len(matrix[0])
    for x in range(0,len(matrix)):
        for y in range(0,len(matrix[0])):
            ret_vector[x] = ret_vector[x] + matrix[x][y]*vector[y]
    return ret_vector

K = 15
def infini_norm_vec(vector):
    return max(vector)

def scalar_X_vector(vector,scalar):
    for val in range(0,len(vector)):
        vector[val] = vector[val]*scalar
    return vector

def add_shift_to_matrix(matrix,shift):
    for x in range(0,len(matrix)):
        matrix[x][x] = matrix[x][x]-shift

    return matrix
eigen_vec = [0,0,0]
print(infini_norm_vec(matrix_X_vector(mat,x_vec)))

def power_iteration(matrix,init_vec,iterations):
    eigen_vec = [0]*len(init_vec)
    for k in range(0,iterations):
        eigen_vec = matrix_X_vector(matrix, init_vec)
        inf_norm = infini_norm_vec(eigen_vec)
        x_vec = scalar_X_vector(eigen_vec,1.0/inf_norm)
        print(inf_norm)
        print(eigen_vec)
    return eigen_vec

def power_iteration_shift(matrix,init_vec,iterations,shift):
    eigen_vec = [0] * len(init_vec)
    matrix = add_shift_to_matrix(matrix,shift)
    for k in range(0, iterations):
        eigen_vec = matrix_X_vector(matrix, init_vec)
        inf_norm = infini_norm_vec(eigen_vec)
        x_vec = scalar_X_vector(eigen_vec, 1.0 / inf_norm)
        print(inf_norm)
        print(eigen_vec)
    return eigen_vec

print(power_iteration(mat,x_vec,10))
print(power_iteration_shift(mat,x_vec,10,-3))