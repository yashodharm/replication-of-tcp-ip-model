def manchencode(string):
	size=len(string)
	out=""
	for i in range(size):
		if(string[i]=='0'):
			out+="01"
		else:
			out+="10"
	return out





def manchdecode(string):
	size=len(string)
	out=""
	for i in range(0,size,2):
		if(string[i]=='0'):
			out+="0"
		else:
			out+="1"
			
	return out

