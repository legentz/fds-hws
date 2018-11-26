# input()
def get_input():
	matrix = list()

	# main loop for input()
	while True:

		# getting string from input
		i = input()

		# end if empty string
		if not i: break

		# save input string and its len()
		matrix.append(list(map(int, i.split())))

	# return matrix
	return matrix

# main function
def main(matrix):

	# create a dummy empty matrix 
	# with same rows/cols size
	sum_matrix = [[0 for k in range(len(matrix[0]))] for n in range(len(matrix))]

	# iterating all over rows
	for i in range(len(matrix)):

		# iterating over columns
		for j in range(len(matrix[0])):

			# here the magic happens!
			# compute the sum of each sub_matrix
			sum_matrix[i][j] = sum([sum(x[:j + 1]) for x in matrix[:i + 1]])
	return sum_matrix


# call main
if __name__ == '__main__':

	# obtain input
	matrix = get_input()

	# get the output matrix and pretty print it nicely!
	print('\n'.join([' '.join(['{}'.format(e) for e in row]) for row in main(matrix)]))