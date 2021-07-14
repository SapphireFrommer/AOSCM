import sys
sys.path.append('./') # change to relevant path in case socket_master_server.py is not locally located
import socket_master_server as sms

# establish socket
sock = sms.set_server_socket(port=5555,host='')  # port 5555 on localhost

# Will wait till  remote tcl session is invoked

# Issue a request
print ("Requesting remote tcl to execute command: date")
msg_to_socket = "date"
rsp_msg = sms.req_msg(sock,msg_to_socket)
print ("Remote tcl response is: %s" % rsp_msg)

# close socket on remote session
sms.req_close(sock)
