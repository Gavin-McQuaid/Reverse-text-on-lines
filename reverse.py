line = raw_input()
while line != 'end':
	new_line = ''
	i = 0
	while i < len(line):
		new_line += line[len(line)-1-i]
		i += 1

	print new_line
	line = raw_input()
	
