#!/usr/bin/python3.6
import nmap
import sqlite3

file_ip_list = open("ip_list.txt","r")

insert_sql_query = """INSERT INTO scan_ip (ip,port,status) VALUES (?, ?, ?)"""
select_sql_query = """SELECT COUNT(*) from scan_ip where ip = ? and port = ?"""

conn = sqlite3.connect("db_scan_ip.db") 
cursor = conn.cursor()


nm = nmap.PortScanner()

with file_ip_list as data:
    for line in data:
        line = line.strip()
        nm.scan(line, arguments='-sV -p 1-65535 -Pn')
        print(line)
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (line, nm[line].hostname()))
        print('State : %s' % nm[line].state())
        for proto in nm[line].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)
    
            lport = nm[line][proto].keys()

            for port in lport:
                print ('port : %s\tstate : %s' % (port, nm[line][proto][port]['state']))
                
                data_select = [line, port]
                count = cursor.execute(select_sql_query, data_select)
                
                print('Count: %s' % (count.fetchall())
                if count.fetchone() == 0:
                    print("ravno!!!!!!!")    
                    data_insert = [line, port, nm[line][proto][port]['state']]
                    cursor.execute(insert_sql_query, data_insert)
conn.commit()
conn.close()