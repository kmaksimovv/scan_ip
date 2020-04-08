#!/usr/bin/python3.6
import nmap

file_ip_list = open("ip_list.txt","r")

nm = nmap.PortScanner()

# with file_ip_list as data:
#     for line in data:
#         line = line.strip()
#         nm.scan(line, arguments='-sV -p 1-65535 -Pn')
#         print(line)
#         print('----------------------------------------------------')
#         print('Host : %s (%s)' % (line, nm[line].hostname()))
#         print('State : %s' % nm[line].state())
#         for proto in nm[line].all_protocols():
#             print('----------')
#             print('Protocol : %s' % proto)
    
#             lport = nm[line][proto].keys()

#             for port in lport:
#                 print ('port : %s\tstate : %s' % (port, nm[line][proto][port]['state']))
