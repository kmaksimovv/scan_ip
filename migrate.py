#!/usr/bin/env python3.6

import sqlite3

conn = sqlite3.connect("db_scan_ip.db") 
cursor = conn.cursor()

# sql_create_scan_ip_table = """ CREATE TABLE IF NOT EXISTS scan_ip (
#                                         `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#                                         `ip` varchar(25),
#                                         `port` varchar(25),
#                                         `status` varchar(25)
#                                         )"""

# cursor.execute(sql_create_scan_ip_table)


