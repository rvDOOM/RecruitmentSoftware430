#!/usr/bin/python
# from http.server import HTTPServer
import MySQLdb
import string
#from datetime import date
# Open database connection
host = "localhost"
username = "api"
password = "password"
database = "CSC430_Midterm"
db = MySQLdb.connect(host, username, password, database)
# prepare a cursor object using cursor() method
cursor = db.cursor()

def query1():
    i = 1;
    cursor.execute("SELECT* from Recruiter")
    #rows contains the entire table
    rows = cursor.fetchall()
    for row in rows:
        print("Recruiter#", i)
        i += 1;
        print("Name: \t\t" ,row[0])
        print("Company: \t",row[1])
        print("\n")

query1()

#disconnect from server
print("End of List/Query")
db.close()