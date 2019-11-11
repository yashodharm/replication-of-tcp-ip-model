def parity_calculator(string):
	size=len(string)
	count =0
	for i in range (size):
		count +=int(string[i])
	return str((count+1)%2)+string

def parity_verify(string):
	size=len(string)
	count =0
	for i in range (size):
		count +=int(string[i])
	return count%2
