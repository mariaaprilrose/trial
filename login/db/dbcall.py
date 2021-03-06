#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = None

try:
     
    con = psycopg2.connect(database='testdb', user='dyosa', password = 'dyosa', host='127.0.0.1', port=5432)
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM person")

    rows = cur.fetchall()

    for row in rows:
        print row
    

except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()