#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	res_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
				res_matrix[i][j] = matrix[i][j] * matrix[i][j]
	return (res_matrix)
