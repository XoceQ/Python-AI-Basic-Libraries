import numpy as np

""" #array
numbers = [1,2,3,4]

ndarray_numbers = np.array(numeros)

print(ndarray_numbers)
 
#matriz
matrix_unos = np.ones((3, 3))
print(matrix_unos)
 

#ndarray range values  0 to 9
array_1 = np.arange(0,10)
print(array_1) 

#a. random numbers
r_array = np.random.randint (0, 10, size=5)
print(r_array) 
 

#b. Matrix 3x3 boolean True value
matrix_bool = np.full((3, 3), True, dtype=bool)
print(matrix_bool) 

#c. Matrix 2x3x4 random float values
matrix_float = np.random.rand(2, 3, 4)
print(matrix_float)

#Modify elements
#a.  
r_array = np.random.randint (0, 10, size=5)
print(r_array)
print("Tercer elemento:", r_array[2])

#b. 
matrix_bool = np.full((3, 3), True, dtype=bool)
print(matrix_bool) 

matrix_bool[1][1] = False
print(matrix_bool)
 
#c. calculate the mean
matrix_float = np.random.rand(2, 3, 4)
mean_2 = np.mean(matrix_float, axis=2)
print(matrix_float)
print("mean:")
print(mean_2)

# Arithmetic operations

#1. One-dimensional arrays and element-wise addition
array1D_1 = np.random.randint(0, 10, size=5)
array1D_2 = np.random.randint(0, 10, size=5)
sum_1D = np.add(array1D_1, array1D_2)

print("1D Array - 1:", array1D_1)
print("1D Array - 2:", array1D_2)
print("Element-wise Sum (1D):", sum_1D)

#2. Two-dimensional arrays and matrix-vector multiplication
matrix_2D = np.random.randint(0, 10, size=(3, 3))
vector_2D = np.random.randint(0, 10, size=(3, 1))
product_2D = np.matmul(matrix_2D, vector_2D)

print("\n2D Matrix:\n", matrix_2D)
print("2D Vector:\n", vector_2D)
print("Matrix-Vector Multiplication (np.matmul):\n", product_2D)


#a. Maximum and Minimum
# Create a one-dimensional array with random integers
array1D = np.random.randint(0, 100, size=10)

# Use functions to find the maximum and minimum values
maximum_value = np.max(array1D)
minimum_value = np.min(array1D)

# Output the results
print("1D Array:", array1D)
print("Maximum value:", maximum_value)
print("Minimum value:", minimum_value)

#b. Create a 3x3 two-dimensional array with floating-point values
array2D = np.random.rand(3, 3)  # Generates float values between 0 and 1

# Calculate the sum of each column (axis=0 means column-wise)
column_sums = np.sum(array2D, axis=0)

# Output the results
print("2D Array (3x3):\n", array2D)
print("Sum of each column:", column_sums)

#c.
# Create a 1D array with 10 equally spaced values between 0 and 1
array_linspace = np.linspace(0, 1, num=10)

# Output the result
print("Equally spaced array using np.linspace():", array_linspace)


#indexing and slicing
#a. 
# Create a 1D array with integers from 0 to 9
array = np.arange(10)

# Get only even elements (divisible by 2)
even_elements = array[array % 2 == 0]

# Output
print("Original array:", array)
print("Even elements:", even_elements)

#b.
matrix_four = np.random.randint(0, 10, size=(4, 4))
# Get the submatrix: first 2 rows and last 2 columns

submatrix = matrix_four[:2, -2:]

print("Matrix: ", matrix_four)
print("Submatrix: ", submatrix)
"""

#c.
# Create a 3x3x3 3D array with random integers
array3D = np.random.randint(0, 10, size=(3, 3, 3))

# Get the subarray formed by the first two dimensions (e.g., the first "slice")
subarray = array3D[0]  # This gets the first 2D matrix (shape 3x3)

# Output
print("Original 3D array (3x3x3):\n", array3D)
print("\nSubarray (first 2D slice from the first dimension):\n", subarray)
