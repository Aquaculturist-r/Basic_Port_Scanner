#!/bin/python3

import sys
import socket
from datetime import datetime 

#Define our target 
if len(sys.argv) == 2: #argv is the amount of arguments we are giving (so TWO arguments).
	target = socket.gethostbyname(sys.argv[1]) #Translates hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")	

# Example: "python3 scanner.py <Hostname/IP address>" will return the IPv4
# Example: "python3 scanner.py 192.1" isnt a valid IP address. So we need to clean up function to make sure it only accepts valid inputs so people can't break it. 

#Add a pretty banner
print("-" * 50)
print("Scanning Target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,85): #for loop to cycle through ports 50 - 85
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Setting a variable to gather IPv4 address (AF_INET) and the port we are trying to connect to (SOCK_STREAM)
		socket.setdefaulttimeout(1) #Times out and moves to next port to prevent slowdown.
		result = s.connect_ex((target, port)) #Checks for error when taking a target ip (Defined earlier) and seeing if each port in range given is open(0) or closed(1).
		if result == 0:
			print(f"Port {port} is open")
		s.close() #Closes out socket connection and loops to the next port in iteration.

except KeyboardInterrupt:
	print("\nExiting Program.")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")	
	sys.exit()
	
except socket.error:
	print("Could not connect to server.")
	sys.exit()
