import sys
import socket

def set_server_socket(port,host) :
   s = socket.socket()
   s.bind((host, port))
   s.listen(1)
   print "Listening on port %d" % port
   sock, addr = s.accept()
   print "Connection from", sock.getpeername()
   msg_from_socket = get_next_data(sock)   # get initial message 
   print "Initial Message from TCL: %s\n" % (msg_from_socket)     
   return sock

def get_next_data(sock) :
     try :
       data = sock.recv(4096)
     except socket.error, ex:
       print 'Socket Error while receiving%s' % ex
       exit()       
     # Check if still alive
     if len(data) == 0:
         print("ERROR: socket received data length is 0")
         exit()
     # Ignore new lines
     msg_from_socket = data.strip() # all leading and trailing white-spaces are removed from the string
     if len(msg_from_socket) == 0:
         print("ERROR: socket received an illegal message of only white-spaces")
         exit()
     return msg_from_socket

def send_msg(sock,msg_to_socket) :
   try:
     sock.sendall(msg_to_socket)
   except socket.error, ex:
     print 'Socket Error while sending%s' % ex 
     exit()           

def req_msg(sock,msg_to_socket) :
     print 'tclpy> Request to remote TCL: %s' % msg_to_socket
     send_msg(sock,msg_to_socket+'\n')  # appending '\n' is needed, not sure why
     msg_from_socket = get_next_data(sock) 
     print 'tclpy> Response from remote TCL: %s\n' % msg_from_socket
     return msg_from_socket
  
def req_close(sock) :
     msg_to_socket =  "close $my_socket"    
     print 'tclpy> Request to remote TCL: %s' % msg_to_socket
     send_msg(sock,msg_to_socket+'\n')  # appending '\n' is needed, not sure why

          
        