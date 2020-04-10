#!/usr/bin/env python3.6

import nmap
import sqlite3

file_ip_list = open("ip_list.txt","r")

insert_sql_query = """INSERT INTO scan_ip (ip,port,status) VALUES (?, ?, ?)"""
select_sql_query_count = """SELECT COUNT(*) from scan_ip where ip = ? and port = ?"""
select_sql_query_status_port = """select status from scan_ip WHERE ip = ? and port = ?"""
update_sql_query_status_port = """UPDATE scan_ip SET status = ?  where ip = ? and port = ?"""

conn = sqlite3.connect("db_scan_ip.db") 
cursor = conn.cursor()

nm = nmap.PortScanner()

with file_ip_list as data:
    for ip in data:
        ip = ip.strip()
        # nm.scan(ip, arguments='-sV -p 1-65535 -Pn')
        nm.scan(ip, arguments='-sV -p 22,80 -Pn')
        for proto in nm[ip].all_protocols():
            lport = nm[ip][proto].keys()

            for port in lport:
                status_port = nm[ip][proto][port]['state']
                data_select = [ip, port]

                count = cursor.execute(select_sql_query_count, data_select)
                data_insert = [ip, port, status_port]
                data_select_port = [ip, port]
                count = count.fetchone()[0]
                
                if count == 0:
                    cursor.execute(insert_sql_query, data_insert)
                else:
                    cursor.execute(select_sql_query_status_port, data_select_port)
                    status_port_sql = cursor.fetchone()[0]

                    if status_port_sql != status_port:
                        data_update = [status_port, ip, port]
                        cursor.execute(update_sql_query_status_port, data_update)
                        with open('scan_hosts.txt', 'a') as f:
                            f.write(f"ip: {ip}, port: {port}, status: {status_port}\n")

conn.commit()
conn.close()
