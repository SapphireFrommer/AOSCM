
set server localhost
set my_socket [socket $server 5555]
fconfigure $my_socket -buffering none

# Initial message to Python
set initial_msg "TCL> Hello Python, I'm your TCL slave"
puts "Sent initial message: $initial_msg"
puts $my_socket "$initial_msg"

while {1} {
    puts "Waiting for remote Command ..."    
    gets $my_socket rmt_cmd
    puts "tclpy> Received remote command: $rmt_cmd"
    eval $rmt_cmd
    if {$rmt_cmd == "close \$my_socket"} {
      puts "tclpy> Closing the socket connection"
      break
    }    
    # send response message
    set rsp_msg "done"   
    puts "tclpy> Sending response message: $rsp_msg"
    puts $my_socket "$rsp_msg"
    puts ""      
}

