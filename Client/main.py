import time
import schedule
import mysql.connector
import pygame

#Uncomment in production, caused issues in Docker
#pygame.mixer.init()
#pygame.mixer.music.load("myFile.wav")

mydb = mysql.connector.connect(user='root', password='dev22', host='some-mysql', database='CETSS')
mycursor = mydb.cursor(buffered=True)


def poll():
    myresult = mycursor.execute("SELECT * FROM Lockdowns")
    LockdownCount = mycursor.rowcount
    
    if LockdownCount != 0:
        #Lockdown Found
        LockdownRows = mycursor.fetchall() 
        for x in LockdownRows:
            if x[2] == bytearray(b'1'):
                print('This is a test')
            else:
                #Uncomment in production, caused issues in Docker
                #pygame.mixer.music.play()
    else:
        #No Lockdown found. Contine
        print('Placeholder') 

schedule.every(15).seconds.do(poll)
  


while True:
    schedule.run_pending()
    time.sleep(1)
