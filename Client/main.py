import time
import schedule
import mysql.connector

mydb = mysql.connector.connect(user='root', password='dev22', host='some-mysql', database='CETSS')

mycursor = mydb.cursor()


def poll():
    myresult = mycursor.execute("SELECT * FROM Lockdowns")
    print('Result: ' + str(myresult))
    if myresult == None:
        print('No Lockdown in progresss')
    else:
        print('Lockdown Found') 


schedule.every(15).seconds.do(poll)
  


while True:
    schedule.run_pending()
    time.sleep(1)
