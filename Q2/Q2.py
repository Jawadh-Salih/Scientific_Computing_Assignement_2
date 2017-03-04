
import sys
import random

sys.path.append('../')

from Q1 import Q1
init_vec = [0,0,1]
x_vec = init_vec
mat = [[2,3,2],[10,3,4],[3,6,1]]

def infini_norm(vec):
    max = 0
    n = len(vec)
    for i in range (0,n):
        if(max<abs(vec[i])):
            max = abs(vec[i])
    return max

def l1_norm(vec):
    norm = 0
    for val in vec:
        norm += abs(val)
    return norm
def normalize_vector(vec):
    norm = infini_norm(vec)
    i = 0
    for val in vec:
        vec[i] = round(val/norm,4)
        i = i+1
    return vec

def substract_vecotrs(vec1,vec2):
    length = len(vec1)
    for i in range(0,length):
        vec1[i] -= vec2[i]
    return vec1

def shift_matrix(mat,shift):
    n = len(mat)
    for x in range(0, n):
        mat[x][x] -= shift
    return mat
def normalized_power_iteration(crs,vec,tolarance):
    eigen_vec = vec
    real_vec = vec
    temp_vec = vec
    max_eigen = 0
    tolaranc,iter = 1,0
    while(tolaranc != 0):
        eigen_vec = Q1.matrix_X_vector_sparse_algorithm(crs,eigen_vec) # Yk = AXk-1
        max_eigen = infini_norm(eigen_vec)
        real_vec = eigen_vec
        eigen_vec = normalize_vector(eigen_vec)# Xk = Yk/|Yk|
        sub_vec = substract_vecotrs(temp_vec, eigen_vec)
        temp_vec = eigen_vec
        tolaranc = round(l1_norm(sub_vec), tolarance)
        iter += 1
        vec = eigen_vec
        # print(eigen_vec, max_eigen, tolarance,iter)
    value_pair = list()
    value_pair.append(eigen_vec)
    # real_vec = demormalize_vector(eigen_vec,max_eigen)
    # value_pair.append(real_vec)
    value_pair.append(eigen_vec.index(1.0))
    value_pair.append(round(max_eigen,4))

    return value_pair
# crs = Q1.matrix_to_crs(mat)

def shifted_normalized_power_iteration(mat,vec,shift,tolarance):
    crs_new = shift_matrix(mat,shift)
    crs_new = Q1.matrix_to_crs(crs_new)
    normalized_power_iteration(crs_new,vec,tolarance)

# Q2 part e. The Pagerank algorithm


def pagerank(matrix,tolrance):
    n = len(matrix)
    vec = [round(1/n,3)]*n
    crs = Q1.matrix_to_crs(matrix)
    pages = normalized_power_iteration(crs,vec,tolrance)

    return pages

    # print(matrix)

def generate_sparse_matrix(n):
    # Creating a n x n matrix.
    Matrix = [[0 for x in range(n)] for y in range(n)]
    r1,r2  =1,4
    if(n == 1000):
        r1,r2 = 5,20
    for row in Matrix:
        no_percentage = int(random.randint(r1, r2))

        value = round(1/no_percentage,3)
        x = 0
        while(x <no_percentage):
            v = random.randint(0, n - 1)
            if(row[v]!=0):
                continue
            row[v] = value
            x = x+1
    matrix = [[0 for x in range(n)] for y in range(n)]
    for x in range(0,n):
        for y in range(0,n):
            matrix[x][y] = Matrix[y][x]
    return matrix

web_page_matrix = generate_sparse_matrix(1000)

result = pagerank(web_page_matrix,1)
print("Number 1 ranked web page is web page number",result[1]+1)

print("-----------------------------Ranked Web Pages-------------------------------")
pages = len(result[0])
for i in range(0,pages):
    max_val = max(result[0])
    max_index = result[0].index(max_val)
    print("Rank ",(i+1)," is ",(max_index+1),"th Page")
    result[0][max_index] = 0
# print(result)




