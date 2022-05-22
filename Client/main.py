import time
import schedule
import mysql.connector

mydb = mysql.connector.connect(user='root', password='dev22', host='some-mysql', database='CETSS')

mycursor = mydb.cursor()


def poll():
    mycursor.execute("SELECT * FROM Lockdowns")
    myresult = mycursor.fetchall()
    if myresult == 0:
        print('No Lockdown in progresss')
    else:
        print('Lockdown Found')
        for x in myresult:
        print(x)

  


schedule.every(15).seconds.do(poll)
  


while True:
    schedule.run_pending()
    time.sleep(1)
