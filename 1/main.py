# input()
def get_input():
	str_val = list()
	str_len = list()

	# main loop for input()
	while True:

		# getting string from input
		i = input()

		# end if empty string
		if not i: break

		# save input string and its len()
		str_val.append(i)
		str_len.append(len(i))

	# return input strings and
	# max len() if there's any of them or -1
	return str_val, (max(str_len) if len(str_len) > 0 else -1)

# main function
def main(str_val, str_max_len):

	# char index
	j = 0 

	# output string
	out = '' 

	# computing output
	while j < str_max_len:
		
		# for each input string, take
		# the char at index j
		for s in str_val:
			if j < len(s): out += s[j]

		# point to the next char
		j += 1

	return out


# call main
if __name__ == '__main__':

	# obtain input
	str_val, str_max_len = get_input()

	# manipolate strings and print output
	print(main(str_val, str_max_len))