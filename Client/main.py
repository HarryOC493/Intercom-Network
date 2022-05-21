from http import server
import time
import mysql.connector

mydb = mysql.connector.connect(user='root', password='dev22', server='some-mysql', database='CETSS')

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Messages")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)