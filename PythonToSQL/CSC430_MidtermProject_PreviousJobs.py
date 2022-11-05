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
    cursor.execute("SELECT* from PreviousJobs")
    #rows contains the entire table
    rows = cursor.fetchall()
    for row in rows:
        print("PreviousJobs of:")
        print("Name: \t\t\t" ,row[0])
        print("JobPosition: \t\t",row[1])
        print("Company Name: \t\t", row[2])
        print("\n")

query1()

#disconnect from server
print("End of List/Query")
db.close()
