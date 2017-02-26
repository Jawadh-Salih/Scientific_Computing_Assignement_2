

 # Answer to question 1 part d.
 # Generating randome matrix.
import random
import sys
import time
def generate_sparse_matrix(n,percentage):

    # Creating a n x n matrix.
    Matrix = [[0 for x in range(n)]for y in range(n)]

    # print(Matrix)
    val = 0
    no_percentage = int((100-percentage)*(n**2)/100)
    # print(no_percentage)
    vv = 0
    uu = 0
    while(val != no_percentage):
        v = random.randint(0,n-1)
        u = random.randint(0,n-1)
        if(vv != v or uu != u):
            Matrix[v][u] = random.randint(1,1000)
            val = val +1
        vv = v
        uu = u
    # print(Matrix)
    return Matrix



# print(generate_sparse_matrix(10,90))
#Answer for question 1 part edef matrix_to_CRS(matrix):
def matrix_to_crs(matrix):
    crs = list()
    n = len(matrix)
    row_ptr = list()
    col_ind = list()
    values = list()
    row_ptr.append(0)
    count = 0
    for row in matrix:
        inc = 0
        for val in row:
            if(val != 0 ):
                count = count +1
                col_ind.append(inc)
                values.append(val)
            inc = inc + 1
        # Each row has a row ptr.
        row_ptr.append(count)
    crs.append(row_ptr)
    crs.append(col_ind)
    crs.append(values)

    # print(crs)
    return  crs


#Answer question 1 part f
def get_element_crs(crs,i,j):
    element_val = 0
    # Worst case gives n iterations.
    for x in range(crs[0][i],crs[0][i+1]):
        if(len(crs[1])!= 0):
            if(j != crs[1][x]):
                element_val = 0
            else:
                element_val = crs[2][x]
                break
        else:
            element_val = 0
    return element_val

# get_element_crs(CRS,4,1)
#Answer for question 1 part g
def set_element_crs(crs,i,j,e):
    if(e != 0):
        element = get_element_crs(crs,i,j)
        if(element == 0):
            val = crs[0][i+1]- crs[0][i]
            if(val == 0):
                crs[1].insert(crs[0][i],j)
                crs[2].insert(crs[0][i],e)
            else:
                for x in range(crs[0][i],crs[0][i+1]):
                    if (j < crs[1][x] or x == crs[0][i+1]-1): # find the appropriate place to insert the new value.
                        # now insert the element into the array
                        if(x == crs[0][i+1]-1 and j>= crs[1][x]):
                            crs[1].insert(x+1, j)
                            crs[2].insert(x+1, e)
                            break
                        else:
                            crs[1].insert(x, j)
                            crs[2].insert(x, e)
                            break
            for y in range(i+1,len(crs[0])):
                crs[0][y] = crs[0][y] + 1
        else:
            for x in range(crs[0][i],crs[0][i+1]):
                if (j == crs[1][x]):
                    crs[1][x] = j
                    crs[2][x] = e
                    break
                else:
                    continue
        return 1
    else:
        return 0
# set_element_crs(CRS,1,2,0)
# print(CRS)
# print(mat)
# get_element_crs(CRS,4,1)

def crs_to_ccs(crs):
    ccs = list()
    col_ptr = [0]* len(crs[0])
    row_ind = list()
    values = list()
    ccs.append(col_ptr)
    ccs.append(row_ind)
    ccs.append(values)
    i,y,k  = 0,0,0
    length = crs[0][len(crs[0]) - 1]
    for x in range(0, length):
        j = crs[1][x]
        e = crs[2][x]
        k = crs[0][i + 1] - crs[0][i]
        set_element_crs(ccs, j, i, e)
        if(y == k-1):
            i = i + 1
            y = 0
            continue
        y = y+1
    # print(ccs)
    return ccs


# CCS = crs_to_ccs(CRS)
def generate_dense_vector(n,percentage):
    # Creating a n x n matrix.
    Vector = [0 for x in range(n)]

    # print(Matrix)
    val = 0
    no_percentage = int((100 - percentage) * (n ** 2) / 100)
    # print(no_percentage)
    vv = 0
    while (val != percentage):
        v = random.randint(0, n - 1)
        if (vv != v):
            Vector[v] = random.randint(1, 1000)
            val = val + 1
        vv = v
    # print(Matrix)
    return Vector
    #
# print(generate_dense_vector(10,90))

def matrix_X_vector_sparse_algorithm(crs,vector):

    # time1 = time.time()
    if(len(crs[0])-1 != len(vector)):
        print("Vector are Matrix lenghts are mismatching. Please input new elements.")
        return
    else:
        return_vector = [0]*len(vector)
        t, k = 0, 0
        for i in range(0,len(crs[0])-1):
            c_i = crs[0][i]
            c_i1 = crs[0][i+1]
            for y in range(c_i,c_i1):
                j = crs[1][y]
                e = crs[2][y]
                return_vector[i] = return_vector[i] + e*vector[j]
                k = c_i1 - c_i
                if(t == k-1):
                    t = 0
                    break
                t = t+1
        # time2 = time.time()
        # print((time2-time1)*1000)

    return  return_vector

def matrix_X_vector_dense_algorithm(matrix,vector):
    # time1 = time.time()
    if (len(matrix[0]) != len(vector)):
        print("Vector are Matrix lenghts are mismatching. Please input new elements.")
        return
    else:
        ret_vector = [0]*len(vector)
        i = 0
        for row in matrix:
            local_vec_element = 0
            j = 0
            for val in row:
                local_vec_element = local_vec_element + val*vector[j]
                j = j+1
            ret_vector[i] = local_vec_element
            i = i+1
    # time2 = time.time()
    # print((time2 - time1) * 1000)
    return ret_vector

def matrix_matrix_add_sparse_algorithm(crs1,crs2):
    t = 0
    crs3 = crs1
    count = 0
    time1 = time.time()
    for i in range(0,len(crs1[0])-1):# Set of rows are selected.
        flag = False
        k = crs1[0][i+1]
        m = crs2[0][i+1]
        l = crs1[0][i]
        n = crs2[0][i]
        p,q = -1,-1
        while(l<k or n<m):

            if(l<k):
                p = crs1[1][l]
                e1 = crs1[2][l]
            if(n<m):
                q = crs2[1][n]
                e2 = crs2[2][n]
            if(p!=-1 or q!=-1):
                if(p == q):
                    e1 = e1+e2
                    # set_element_crs(crs3,i,p,e1)
                    crs3[2][p] = e1
                elif(q!=-1):
                    # set_element_crs(crs3,i,q,e2)
                    crs3[1].insert(n,q)
                    crs3[2].insert(n,e2)
                    count  = count +1
                    # for j in range(i+1,len(crs3[0])):
                    #     crs3[0][j] = crs3[0][j]+1
            l,n = l+1,n+1
    for i in range(1,len(crs3[0])):
        crs3[0][i] = crs3[0][i] + count

    time2 = time.time()
    print((time2-time1)*1000)
    return crs3

def matrix_matrix_add_dense_algorithm(matrix1,matrix2):
    time1 = time.time()
    if(len(matrix1) == len(matrix2)):
        for x in range(0,len(matrix1)):
            for y in range(0,len(matrix1[0])):
                matrix1[x][y] = matrix1[x][y] + matrix2[x][y]
    time2 = time.time()
    print((time2-time1)*1000)

    return matrix1
n = 5
# vec = generate_dense_vector(n,90)
# mat = generate_sparse_matrix(n,90)
# CRS = matrix_to_crs(mat)
# print("Matrix is ",mat)
# print("Matix in CRS format ", CRS)
# print("Vector is ",vec)

# time_dense_start = time.time()
# result_vector_dense = matrix_X_vector_dense_algorithm(mat,vec)
# time_dense_end = time.time()

# time_sparse_start = time.time()
# result_vector_sparse = matrix_X_vector_sparse_algorithm(CRS,vec)
# time_sparse_end = time.time()

# elapsed_time_sparse = (time_sparse_end - time_sparse_start)*1000.0 #in ms

# print(result_vector_sparse)
# print("Execution Time for sparse algorithm : ",elapsed_time_sparse," ms" )


# elapsed_time_dense = (time_dense_end - time_dense_start)*1000.0 #in ms

# print(result_vector_dense)
# print("Execution Time for dense algorithm : ",elapsed_time_dense," ms" )

#Genarate Matrix1
# print("Running...")
mat1 = generate_sparse_matrix(n,90)
mat2 = generate_sparse_matrix(n,90)
# print("Running...")
crs1 = matrix_to_crs(mat1)
crs2 = matrix_to_crs(mat2)
print(mat1)
print(mat2)
print(crs1)
print(crs2)


time_sparse_start_add = time.time()
print("Running....... Sparse")
result_matrix_sparse_add = matrix_matrix_add_sparse_algorithm(crs1,crs2)
time_sparse_end_add = time.time()

time_dense_start_add = time.time()
print("Running......Dense")
result_matrix_dense_add = matrix_matrix_add_dense_algorithm(mat1,mat2)
time_dense_end_add = time.time()
# print(result_matrix_dense_add)
elapsed_time_dense_add = (time_dense_end_add-time_dense_start_add)*1000.0
print("Execution Time for dense algorithm for addition: ",elapsed_time_dense_add," ms" )

print(result_matrix_sparse_add)
elapsed_time_sparse_add = (time_sparse_end_add-time_sparse_start_add)*1000.0
print("Execution Time for sparse algorithm for addition: ",elapsed_time_sparse_add," ms" )

# print(get_element_crs(CCS,1,4))
print("Please enter the size of the matrix you want to generate : ")
inp = input()
n = int(inp)
# n = 0
print("Random Matrix is generating .....")
matrix_n = generate_sparse_matrix(n,90)
print(matrix_n)
print("Converting the Matrix to 'CRS' format......")
crs_n = matrix_to_crs(matrix_n)
print(crs_n)
print("Setting diagonal elements to 2016....")
for x in range(0,n):
    set_element_crs(crs_n,x,x,2016)
print(crs_n)
print("Converting the Matrix to CCS format.....")
ccs_n = crs_to_ccs(crs_n)
print(ccs_n)
# Need to be implemented.

