import socket
from middleware.string_bit import string_bits
from middleware.error_flow import parity_calculator
from middleware.physical_layer import manchencode
from middleware.error import *
s = socket.socket()          
  
port = 12347                
  
s.connect(('127.0.0.1', port)) 

print s.recv(1024) 

st=raw_input("please enter the input\n")

print(st)
st=string_bits(st)#updated to binary bits
print(st)
st=parity_calculator(st)#parity bit added to the frame
print(st)
st=manchencode(st)
print(st)
#lets induce error

st=errorgen(st)



#strin=st.encode("utf-8")#	bytes(st, encoding='utf-8')

s.send(st)	




s.close()        