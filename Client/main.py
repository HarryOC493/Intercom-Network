from http import server
import time
import mysql.connector

mydb = mysql.connector.connect(user='root', password='dev22', host='some-mysql', database='CETSS')

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Messages")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)