import socket   
from middleware.string_bit import bits_string
from middleware.error_flow import parity_verify
from middleware.physical_layer import manchdecode
from middleware.error import *            
  
s = socket.socket()          
print("Server Side Socket successfully created")
  
port = 12347                
 
s.bind(('', port))         
print("Socket is binded to" +(port))
  
s.listen(5)      
print("Socket is listening")          
  
while True: 
  
   c, addr = s.accept()      
   print("Got connection from"+ addr) 
  
   c.send('Thank you for connecting') 
   data=c.recv(1024)
   #d=data.decode("utf-8")
   print(data)
   d=manchdecode(data)
   print(d)
   check=parity_verify(d)
   if check==1:
   		d=d[1:]
   else:
   		print("The error is found")
   print(d)
   d=bits_string(d)
   print("the output received on other end is " + d)

   break
