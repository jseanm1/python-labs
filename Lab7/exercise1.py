# Janindu Arukgoda
# L7.E1

# Function to read an n*m matrix
def read_matrix (n,m):
	matrix = []
	
	for i in range (0,n):
		row = raw_input()
		row_list = row.split()
		int_row_list = []

		for s in row_list:
			int_row_list.append(int(s))

		if (len(int_row_list) != m):
			print "ERROR!!!\nInvalid input size. Expected",n,"x",m,"matrix!!!"
			exit()

		matrix = matrix + [int_row_list]

	return matrix

# Function to multiply two matrices
def multiply_matrices (A,B):
	matrix = []

	if (len(A) != len(B[0])):
		print "ERROR!!!Matrix size mismatch!!!"
		exit()

	for i in range (0,len(A)):
		raw = []
		for j in range (0,len(B[i])):
			element = 0
			for k in range (0,len(A[i])):
				element += A[i][k] * B[k][j]				
			raw.append(element)
		matrix = matrix + [raw]
	
	return matrix

# Function to print a matrix
def print_matrix(matrix):
	for raw in matrix:
		for element in raw:
			print element,
		print

try:
	print "Matrix A:"
	matrix_A = read_matrix (3,4)
	print

	print "Matrix B:"
	matrix_B = read_matrix (4,3)
	print
	#print_matrix(matrix_A)
	#print_matrix(matrix_B)

	matrix = multiply_matrices(matrix_A,matrix_B)
	
	print "Matrix AB:"
	print_matrix(matrix)

except ValueError:
	print "ERROR!!!\nOnly integers are expected as input!!!"
