

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

# Q1 part k

# Matrix addition of Sparse Matrices
def matrix_matrix_add_sparse_algorithm(crs1,crs2):
    i = 0
    length = len(crs1[0])-1
    crs3 = list()
    row_ptr = [0]*(length+1)
    col_ind = list()
    values = list()
    crs3.append(row_ptr)
    crs3.append(col_ind)
    crs3.append(values)
    # A zero matrix is created. Now insert element one by one.
    while(i<length):
        # Each i is now a row of the matrix.
        # Hence for each row merge the matrices
        crs1_len = crs1[0][i+1]-crs1[0][i]
        crs2_len = crs2[0][i+1]-crs2[0][i]
        j ,k= crs1[0][i],crs2[0][i]
        row_ind = 0
        if(crs2_len>0 and crs1_len >0): # Both rows are non zero
            while(j<crs1[0][i+1] or k < crs2[0][i+1]):
                if(j< crs1[0][i+1] and k<crs2[0][i+1]):
                    if(crs1[1][j] == crs2[1][k]):
                        crs3[1].append(crs2[1][k])
                        crs3[2].append(crs1[2][j]+crs2[2][k])
                        j,k = j+1,k+1
                        row_ind = row_ind +1
                    else:
                        if(crs1[1][j]<crs2[1][k]):
                            crs3[1].append(crs1[1][j])
                            crs3[2].append(crs1[2][j])
                            j = j+1
                        else:
                            crs3[1].append(crs2[1][k])
                            crs3[2].append(crs2[2][k])
                            k = k + 1
                        row_ind = row_ind + 1
                elif(j<crs1[0][i+1]):# No further elements to add in crs2
                    crs3[1].append(crs1[1][j])
                    crs3[2].append(crs1[2][j])
                    j = j+1
                    row_ind = row_ind + 1
                else:# No further elements to add in crs1
                    crs3[1].append(crs2[1][k])
                    crs3[2].append(crs2[2][k])
                    k = k+1
                    row_ind = row_ind + 1
        else:
            if(crs1_len>0): # crs1 is only non zero
                while (j < crs1[0][i + 1]):
                    # if (crs1[1][j] == crs2[1][k]):
                    crs3[1].append(crs1[1][j])
                    crs3[2].append(crs1[2][j])
                    j = j + 1
                    row_ind = row_ind + 1
            if(crs2_len>0): # only crs2 is non zero
                while (k < crs2[0][i + 1]):
                    # if (crs1[1][j] == crs2[1][k]):
                    crs3[1].append(crs2[1][k])
                    crs3[2].append(crs2[2][k])
                    k = k + 1
                    row_ind = row_ind + 1
        crs3[0][i+1] = crs3[0][i] +row_ind
        i = i +1
    return crs3
def _matrix_matrix_add_sparse_algorithm(crs1,crs2):
    t = 0
    col_ptr = [0]*len(crs1[0])
    col_ind = list()
    values= list()
    crs3 = crs1# list()
    # crs3.append(col_ptr)
    # crs3.append(col_ind)
    # crs3.append(values)
    count = 0
    time1 = time.time()
    e1,e2 = 0,0
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
                    # set_element_crs(crs3,i,p,e1)
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

# Matrix addition of Dense Matrices
def matrix_matrix_add_dense_algorithm(matrix1,matrix2):
    # time1 = time.time()
    if(len(matrix1) == len(matrix2)):
        for x in range(0,len(matrix1)):
            for y in range(0,len(matrix1[0])):
                matrix1[x][y] = matrix1[x][y] + matrix2[x][y]
    # time2 =time.time()

    return matrix1
