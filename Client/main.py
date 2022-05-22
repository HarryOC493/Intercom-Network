import time
import schedule
import mysql.connector

mydb = mysql.connector.connect(user='root', password='dev22', host='some-mysql', database='CETSS')

mycursor = mydb.cursor(buffered=True)


def poll():
    myresult = mycursor.execute("SELECT * FROM Lockdowns")
    LockdownCount = mycursor.rowcount
    if LockdownCount != 0:
        #Lockdown Found
        LockdownRows = mycursor.fetchall() 
        for x in LockdownRows:
            print(x)
            print(x[0])
            print(x[2])
            if x[2] == bytearray(b'1'):
                print('This is a test')
            else:
                print('This is not a test')
    else:
        #No Lockdown found. Contine
        print('Placeholder') 

schedule.every(15).seconds.do(poll)
  


while True:
    schedule.run_pending()
    time.sleep(1)
