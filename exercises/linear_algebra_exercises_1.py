# 2 generate an identity matrix given n
def generate_identity(n):
	identity = [[0 for _ in range(n)] for _ in range(n)]
	for i in range(n):
		identity[i][i] = 1

	return identity

# 3 transpose the given 2D matrix
def transpose(matrix):
	n = len(matrix)
	t = [[0 for _ in range(n)] for _ in range(n)]

	for i in range(n):
		for j in range(n):
			t[i][j] = matrix[j][i]
	
	return t

# 4 write a metheod that multiplies a 2D matrix and 1D vector
def mult_2D_1D(A, v):
	n = len(v)

	if n == 0 or n != len(A) or n != len(A[0]):
		return [[]]

	prod = []

	for i in range(n):
		temp = 0
		for j in range(n):
			temp += v[j] * A[i][j]
		prod.append(temp)
	
	return prod

# 5 add two 2D arrays
def add_2D(A, B):
	m = len(A)
	if m == 0 or m != len(B):
		return [[]]
	
	n = len(A[0])
	if n == 0 or n != len(B[0]):
		return [[]]

	C = [[] for _ in range(m)]

	for i in range(m):
		for j in range(n):
			C[i].append(A[i][j] + B[i][j])
	
	return C

# 6 standard multiply two matricies 
def std_mul(A, B):
	m = len(A)
	if m == 0 or m != len(B):
		return [[]]
	
	n = len(A[0])
	if n == 0 or n != len(B[0]):
		return [[]]

	C = [[] for _ in range(m)]

	for i in range(m):
		for j in range(n):
			C[i].append(A[i][j] * B[i][j])
	
	return C

# 7 multiply two 2D matrices
def mult_2D_2D(A, B):
	m = len(A)
	n = len(B)

	if m == 0 or n == 0: 
		return [[]]
	if A[0] != n:
		return [[]]
	
	o = len(b[0])
	
	prod = [[0 for _ in range(o)] for _ in range(m)]

	for i in range(m):
		for j in range(o):
			temp = 0
			for k in range(n):
				temp += A[i][k] * B[k][j]
			prod[i][j] = temp
	
	return prod

