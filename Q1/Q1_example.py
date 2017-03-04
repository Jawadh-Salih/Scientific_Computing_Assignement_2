
import Q1
import time
import sys
print("Please enter the size of the matrix you want to generate : ")
inp = input()
n = int(inp)
# n = 0
print("Random Sparse Matrix is generating .....")
matrix_1 = Q1.generate_sparse_matrix(n,90)
matrix_2 = Q1.generate_sparse_matrix(n,90)
print("Matrix 1 :")
print(matrix_1)

print("Matrix 2 :")
print(matrix_2)

print("Converting the Matrices to 'CRS' format......")
crs_1 = Q1.matrix_to_crs(matrix_1)
crs_2 = Q1.matrix_to_crs(matrix_2)

print("Random Dense Vector is Generating")
vector = Q1.generate_dense_vector(n,90)


print("Matrix Vector Multiplication Sparse Algorithm Running....")
time_sparse_start = time.time()
result_vector_sparse = Q1.matrix_X_vector_sparse_algorithm(crs_1,vector)
time_sparse_end = time.time()

elapsed_time_sparse = (time_sparse_end - time_sparse_start)*1000.0 #in ms

print("N =",n)
print("Matrix Vector Multiplication Sparse ........")
print(result_vector_sparse)
print("Execution Time for sparse algorithm : ",elapsed_time_sparse," ms" )


print("Matrix Vector Multiplication Dense Algorithm Running....")
time_dense_start = time.time()
result_vector_dense = Q1.matrix_X_vector_dense_algorithm(matrix_1,vector)
time_dense_end = time.time()

print("N =",n)
print("Matrix Vector Multiplication Dense ........")
elapsed_time_dense = (time_dense_end - time_dense_start)*1000.0 #in ms
print(result_vector_dense)
print("Execution Time for dense algorithm : ",elapsed_time_dense," ms" )


print("Matrix Matrix Addition Sparse Algorithm Running....")

print("Matrix Addition Sparse........")
time_sparse_start_add = time.time()
print("Running....... Sparse")
result_matrix_sparse_add = Q1.matrix_matrix_add_sparse_algorithm(crs_1,crs_2)
time_sparse_end_add = time.time()

print(result_matrix_sparse_add)
elapsed_time_sparse_add = (time_sparse_end_add-time_sparse_start_add)*1000.0
print("Execution Time for sparse algorithm for addition: ",elapsed_time_sparse_add," ms" )

print("Matrix Matrix Addition Dense Algorithm Running....")


time_dense_start_add = time.time()
print("Running......Dense")
result_matrix_dense_add = Q1.matrix_matrix_add_dense_algorithm(matrix_1,matrix_2)
time_dense_end_add = time.time()

print(result_matrix_dense_add)
elapsed_time_dense_add = (time_dense_end_add-time_dense_start_add)*1000.0
print("Execution Time for dense algorithm for addition: ",elapsed_time_dense_add," ms" )


