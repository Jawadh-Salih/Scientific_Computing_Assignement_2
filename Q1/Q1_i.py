
import Q1

print("Please enter the size of the matrix you want to generate : ")
inp = input()
n = int(inp)
# n = 0
print("Random Matrix is generating .....")
matrix_n = Q1.generate_sparse_matrix(n,90)
print(matrix_n)
print("Converting the Matrix to 'CRS' format......")
crs_n = Q1.matrix_to_crs(matrix_n)
print(crs_n)
print("Setting diagonal elements to 2016....")
for x in range(0,n):
    Q1.set_element_crs(crs_n,x,x,2016)
print(crs_n)
print("Converting the Matrix to CCS format.....")
ccs_n = Q1.crs_to_ccs(crs_n)
print(ccs_n)
# Need to be implemented.



