import time
import schedule
import mysql.connector

mydb = mysql.connector.connect(user='root', password='dev22', host='some-mysql', database='CETSS')

mycursor = mydb.cursor()


def poll():
    myresult = mycursor.execute("SELECT * FROM Lockdowns")

    if myresult != None:
        #Lockdown Found
        LockdownRows mycursor.fetchall() 
        for x in myresult:
            if LockdownRows[2] == '0x31':
                print('This is a test')
            else:
                print('This is not a test')
    else:
        #No Lockdown found. Contine


  


schedule.every(15).seconds.do(poll)
  


while True:
    schedule.run_pending()
    time.sleep(1)
