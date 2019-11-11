from random import randint

def errorgen(string):
	size=len(string)
	out =""
	p=randint(0,1)
	n=randint(0,size-1)
	for i in range (size):
		if(i==n):
			out+='p'
		else:
			out+=string[i]

	return out
